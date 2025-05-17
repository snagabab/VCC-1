import streamlit as st
import pandas as pd
import socket
import ssl
from OpenSSL import crypto
import io

def get_cert_info(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert_bin = ssock.getpeercert(True)
                x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_bin)
                subject = dict(x509.get_subject().get_components())
                issuer = dict(x509.get_issuer().get_components())
                not_before = x509.get_notBefore().decode('ascii')
                not_after = x509.get_notAfter().decode('ascii')
                common_name = subject.get(b'CN', b'').decode('utf-8')

                # Parse dates: format is YYYYMMDDHHMMSSZ
                not_before_date = f"{not_before[0:4]}-{not_before[4:6]}-{not_before[6:8]}"
                not_after_date = f"{not_after[0:4]}-{not_after[4:6]}-{not_after[6:8]}"
                expire_month = not_after[4:6]
                expire_year = not_after[0:4]

                return {
                    "URL_name": hostname,
                    "Issue_date": not_before_date,
                    "Expire_Date": not_after_date,
                    "Expire_Month": expire_month,
                    "Expire_Year": expire_year,
                    "Common_name": common_name,
                    "Error": ""
                }
    except Exception as e:
        return {
            "URL_name": hostname,
            "Issue_date": "Error",
            "Expire_Date": "Error",
            "Expire_Month": "Error",
            "Expire_Year": "Error",
            "Common_name": "Error",
            "Error": str(e)
        }

def main():
    st.title("SSL Certificate Info Fetcher")

    st.markdown("""
    Upload a CSV/Excel/TXT/DOC file with a column of URLs, or paste URLs (one per line).
    Then click Fetch to get SSL certificate details.
    """)

    uploaded_file = st.file_uploader("Upload file (csv, xlsx, txt, doc)", type=["csv", "xlsx", "xls", "txt", "doc", "docx"])
    url_text = st.text_area("Or paste URLs here (one per line)")

    fetch_button = st.button("Fetch")

    if fetch_button:
        urls = []

        # Extract URLs from file
        if uploaded_file:
            try:
                if uploaded_file.name.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(uploaded_file)
                elif uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith('.txt'):
                    content = uploaded_file.getvalue().decode('utf-8')
                    urls = content.strip().splitlines()
                elif uploaded_file.name.endswith(('.doc', '.docx')):
                    import docx
                    doc = docx.Document(uploaded_file)
                    urls = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
                else:
                    st.error("Unsupported file type")
                    return
                if not urls and 'API' in df.columns:
                    urls = df['API'].dropna().astype(str).tolist()
                elif not urls:
                    # If no 'API' column, try first column
                    urls = df.iloc[:,0].dropna().astype(str).tolist()
            except Exception as e:
                st.error(f"Error reading file: {e}")
                return

        # Extract URLs from pasted text
        if url_text.strip():
            urls_from_text = [line.strip() for line in url_text.strip().splitlines() if line.strip()]
            urls.extend(urls_from_text)

        # Remove duplicates & empty
        urls = list({u for u in urls if u})

        if not urls:
            st.error("No URLs provided!")
            return

        # Clean URLs: remove protocol and port if present to get hostname only
        def clean_url(u):
            try:
                if u.startswith("http"):
                    from urllib.parse import urlparse
                    p = urlparse(u)
                    return p.hostname or u
                else:
                    # might just be hostname or ip
                    return u.split(":")[0]
            except:
                return u

        hostnames = [clean_url(u) for u in urls]

        results = []
        with st.spinner("Fetching SSL info..."):
            for host in hostnames:
                res = get_cert_info(host)
                results.append(res)

        df_results = pd.DataFrame(results)
        st.success("Done!")

        st.dataframe(df_results)

        # Provide download CSV
        csv = df_results.to_csv(index=False)
        st.download_button(label="Download results as CSV", data=csv, file_name="ssl_cert_info.csv", mime="text/csv")

if __name__ == "__main__":
    main()
