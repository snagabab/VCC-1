import streamlit as st
import pandas as pd

st.set_page_config(page_title="Certificate Data Fetcher", layout="centered")

# Load your CSVs
api_df = pd.read_csv("api_cert_data.csv")
wildcard_df = pd.read_csv("wildcard_cert_data.csv")

# Combine and clean
combined_df = pd.concat([api_df, wildcard_df], ignore_index=True)
combined_df.columns = combined_df.columns.str.strip()  # Remove any trailing spaces

# Sidebar Title
st.title("🔐 Certificate Data Fetcher")

# Dropdowns
urls = sorted(combined_df['URL_name'].dropna().unique())
months = sorted(combined_df['Expire_Month'].dropna().unique())
years = sorted(combined_df['Expire_Year'].dropna().astype(str).unique())

selected_url = st.selectbox("🌐 Select API/Wildcard URL", urls)
selected_month = st.selectbox("📅 Select Expiry Month", months)
selected_year = st.selectbox("📆 Select Expiry Year", years)

if st.button("🚀 Fetch Certificate Details"):
    filtered = combined_df[
        (combined_df['URL_name'] == selected_url) &
        (combined_df['Expire_Month'] == selected_month) &
        (combined_df['Expire_Year'].astype(str) == selected_year)
    ]

    if filtered.empty:
        st.warning("⚠️ No matching certificate records found.")
    else:
        st.success("✅ Certificate details found below:")
        st.dataframe(filtered, use_container_width=True)

        # Download button
        csv = filtered.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="filtered_cert_data.csv",
            mime="text/csv"
        )
