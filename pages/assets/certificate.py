import streamlit as st
from cryptography.x509 import Certificate

def show_certificate(cert: Certificate):
    # Extract values
    subject = cert.subject.rfc4514_string()
    issuer  = cert.issuer.rfc4514_string()
    serial  = cert.serial_number
    version = cert.version.name
    nbf     = cert.not_valid_before.strftime("%Y-%m-%d %H:%M:%S")
    naf     = cert.not_valid_after.strftime("%Y-%m-%d %H:%M:%S")

    st.markdown(
        f"""
        <div class="card">
        <div style="
            background-color: #1e1e1e;
            border: 2px solid #444;
            border-radius: 12px;
            padding: 20px;
            max-width: 700px;
            margin: auto;
        ">
            <h2 style="
                text-align:center;
                color:#FFD700;
                margin-bottom: 12px;
                font-family: sans-serif;
            ">
                🔒 Digital Certificate 🔒
            </h2>
            <table style="
                width:100%;
                font-family: sans-serif;
                color: #ddd;
                border-collapse: collapse;
            ">
                <tr>
                    <th style="
                        text-align:left;
                        padding:8px;
                        color:#FFD700;
                        width: 30%;
                    ">Subject:</th>
                    <td style="padding:8px;">{subject}</td>
                </tr>
                <tr style="background-color:#2a2a2a;">
                    <th style="text-align:left; padding:8px; color:#FFD700;">Issuer:</th>
                    <td style="padding:8px;">{issuer}</td>
                </tr>
                <tr>
                    <th style="text-align:left; padding:8px; color:#FFD700;">Serial No.:</th>
                    <td style="padding:8px;">{serial}</td>
                </tr>
                <tr style="background-color:#2a2a2a;">
                    <th style="text-align:left; padding:8px; color:#FFD700;">Version:</th>
                    <td style="padding:8px;">{version}</td>
                </tr>
                <tr>
                    <th style="text-align:left; padding:8px; color:#FFD700;">Valid From:</th>
                    <td style="padding:8px;">{nbf}</td>
                </tr>
                <tr style="background-color:#2a2a2a;">
                    <th style="text-align:left; padding:8px; color:#FFD700;">Valid To:</th>
                    <td style="padding:8px;">{naf}</td>
                </tr>
            </table>
        </div></div>
        """,
        unsafe_allow_html=True
    )


def show_certificate_compact(cert: Certificate):
    # Extract values
    subject = cert.subject.rfc4514_string()
    issuer  = cert.issuer.rfc4514_string()
    nbf     = cert.not_valid_before.strftime("%Y-%m-%d")
    naf     = cert.not_valid_after.strftime("%Y-%m-%d")

    # Put it in the sidebar under an expander
    with st.expander("🔒 Certificate", expanded=False):
        st.markdown(
            f"""
            <div style="
                font-family: sans-serif;
                font-size: 0.85rem;
                line-height:1.2;
                max-width: 250px;
                color: #eee;
            ">
                - **Subject:** {subject}<br/>
                - **Issuer:** {issuer}<br/>
                - **Valid:** {nbf} → {naf}
            </div>
            """,
            unsafe_allow_html=True
        )

