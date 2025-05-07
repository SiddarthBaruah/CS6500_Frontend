import streamlit as st
from pages.base_class.page import GeneralPage
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from utilities.messages.retrive_messages import retrieve_messages
from utilities.messages.send_messages import send_message
from utilities.digital_certificates.get_certificate import get_certificate
from pages.assets.certificate import show_certificate_compact
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import ec
from pages.utilities.decrypt import decrypt_message
from pages.utilities.encrypt import encrypt_message


class ChatPage(GeneralPage):
    def __init__(self, name, reciever_name):
        super().__init__(name)
        self.reciever_name= reciever_name
        self.certificate: x509.Certificate = get_certificate(username=reciever_name)
        self.all_messages= self.get_all_messages()
        self.shared_key = self.derive_shared_key()
        self.chain_keys= []
        self.iter=0
        self.protocol_root_key()

    def derive_shared_key(self):
        reciever_public_key = self.certificate.public_key()
        my_private_key: ec.EllipticCurvePrivateKey = st.session_state["user_private_key"]
        shared_key = my_private_key.exchange(ec.ECDH(), reciever_public_key)
        return shared_key
    
    def protocol_root_key(self):
        hkdf_chain = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=f'protocol root key'.encode(),
        )
        ck = hkdf_chain.derive(self.shared_key)
        self.chain_keys.append(ck)
        self.iter+=1

    def get_all_messages(self):
        sender_messages, \
        reciever_messages = retrieve_messages(
                                st.session_state['username'], 
                                self.reciever_name
                            )
        all_messages = list(sender_messages) + list(reciever_messages)
        all_messages.sort(key=lambda msg: int(msg['id']))
        return all_messages
    
    def send_chat_message(self, msg):
        encrypted_msg= encrypt_message(msg=msg,
                                       aes_key=self.chain_keys[self.iter-1],
                                       iter=self.iter+1)
        send_message(
            st.session_state["username"], 
            self.reciever_name, 
            encrypted_msg
        )


    def chat_page(self, page: st._DeltaGenerator):
        with page.container():
            for message in self.all_messages:
                try:
                    self.iter = max(self.iter, message["signedMessage"]["iter"])
                    if message["sender"] == st.session_state["username"]:
                        with st.chat_message("user"):
                            plaintext, self.chain_keys = decrypt_message(encrypted_message=message["signedMessage"],
                                                     chain_keys=self.chain_keys
                                                     )
                            st.write(plaintext)
                    else:
                        with st.chat_message(self.reciever_name):
                            plaintext, self.chain_keys = decrypt_message(encrypted_message=message["signedMessage"],
                                                     chain_keys=self.chain_keys
                                                     )
                            st.write(plaintext)
                except Exception as e:
                    st.write(message)
                    st.write(e)
            if message := st.chat_input("Type here"):
                self.send_chat_message(message)
                with self.sidebar.container():
                    for key in self.chain_keys:
                        st.write(key.hex())
                st.rerun()


    def page_structure(self):
        main_page, right_hamburger = st.columns([5,1])
        right_section = right_hamburger.empty()
        self.sidebar= st.sidebar.empty()
        with right_section.container():
            if st.button(label="Reload Chats"):
                st.rerun()
            show_certificate_compact(self.certificate)
            st.write("Shared Key")
            st.write(self.shared_key)
            with st.expander(label="Chain_key"):
                st.write(self.chain_keys[self.iter-1])
        with self.sidebar.container():
            for key in self.chain_keys:
                st.write(key.hex())

        self.chat_page(main_page.empty())



