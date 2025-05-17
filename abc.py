import streamlit as st
import pandas as pd
import socket
import ssl
from urllib.parse import urlparse
from datetime import datetime
from OpenSSL import crypto
import io
import docx

st.set_page_config(page_title="SSL Certificate Checker", layout="wide")
st.title("🔐 SSL Certificate Details Extractor")

# Function to extract certificate details
def get_certificate_info(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        port = parsed_url.port or 443

        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert_bin = ssock.getpeercert(True)
                x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_bin)

                issue_date = datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
                expire_date = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')

                return {
                    "URL_name": url,
                    "Issue_date": issue_date.strftime("%Y-%m-%d"),
                    "Expire_Date": expire_date.strftime("%Y-%m-%d"),
                    "Expire_Month": expire_date.strftime("%B"),
                    "Expire_Year": expire_date.year,
                    "Common_name": x509.get_subject().CN
                }
    except Exception as e:
        return {
            "URL_name": url,
            "Issue_date": "Error",
            "Expire_Date": "Error",
            "Expire_Month": "Error",
            "Expire_Year": "Error",
            "Common_name": f"Error: {e}"
        }

# File uploader
uploaded_file = st.file_uploader("📁 Upload a file (.csv, .xlsx, .txt, .doc, .docx)", type=["csv", "xlsx", "txt", "doc", "docx"])

# Paste box
st.markdown("### 📥 Or Paste URLs below (one per line)")
pasted_urls = st.text_area("Enter URLs here")

urls = []

# Read from uploaded file
if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    if file_type == 'csv':
        df = pd.read_csv(uploaded_file)
        urls = df.iloc[:, 0].dropna().tolist()
    elif file_type == 'xlsx':
        df = pd.read_excel(uploaded_file)
        urls = df.iloc[:, 0].dropna().tolist()
    elif file_type == 'txt':
        content = uploaded_file.read().decode('utf-8')
        urls = content.strip().splitlines()
    elif file_type in ['doc', 'docx']:
        doc = docx.Document(uploaded_file)
        urls = [para.text for para in doc.paragraphs if para.text.strip()]
else:
    # If no file uploaded, read from pasted text
    if pasted_urls:
        urls = [u.strip() for u in pasted_urls.splitlines() if u.strip()]

# Fetch button
if st.button("🔍 Fetch Certificate Details"):
    if urls:
        with st.spinner("Fetching certificate details..."):
            results = [get_certificate_info(url) for url in urls]
            result_df = pd.DataFrame(results)
            st.success("✅ Done! Here are the results:")
            st.dataframe(result_df)

            # CSV download
            csv_buffer = io.StringIO()
            result_df.to_csv(csv_buffer, index=False)
            st.download_button("📥 Download CSV", data=csv_buffer.getvalue(),
                               file_name="certificate_details.csv", mime="text/csv")
    else:
        st.warning("⚠️ Please upload a file or paste URLs to continue.")
