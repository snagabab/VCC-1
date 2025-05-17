import streamlit as st
import pandas as pd

# Load CSVs
api_df = pd.read_csv("api_cert_data.csv")
wildcard_df = pd.read_csv("wildcard_cert_data.csv")

# Combine dataframes
combined_df = pd.concat([api_df, wildcard_df], ignore_index=True)

# Clean column names
combined_df.columns = combined_df.columns.str.strip()  # Remove extra spaces

# Debug: See what columns we have
st.write("Columns in the combined DataFrame:", combined_df.columns.tolist())

# Now safely access the columns
urls = sorted(combined_df['URL_name'].dropna().unique())
months = sorted(combined_df['Expire_Month'].dropna().unique())
years = sorted(combined_df['Expire_Year'].dropna().astype(str).unique())

st.title("Certificate Data Fetcher")

selected_url = st.selectbox("Select URL", urls)
selected_month = st.selectbox("Select Expire Month", months)
selected_year = st.selectbox("Select Expire Year", years)

if st.button("Fetch"):
    filtered = combined_df[
        (combined_df['URL_name'] == selected_url) &
        (combined_df['Expire_Month'] == selected_month) &
        (combined_df['Expire_Year'].astype(str) == selected_year)
    ]

    if filtered.empty:
        st.info("No matching records found.")
    else:
        st.dataframe(filtered)
        csv = filtered.to_csv(index=False)
        st.download_button("Download CSV", data=csv, file_name="filtered_cert_data.csv", mime="text/csv")
