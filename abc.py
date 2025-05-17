import streamlit as st
import pandas as pd

# Load CSV files in the background
api_df = pd.read_csv("api_cert_data.csv")
wildcard_df = pd.read_csv("wildcard_cert_data.csv")

# Combine URLs from both dataframes for dropdown (unique)
urls_api = api_df['URL_name'].dropna().unique().tolist()
urls_wildcard = wildcard_df['Common_name'].dropna().unique().tolist()
all_urls = sorted(set(urls_api + urls_wildcard))

# Unique months and years from both dfs combined
all_months = sorted(set(api_df['Expire_Month'].dropna().unique()) | set(wildcard_df['Expire_Month'].dropna().unique()))
all_years = sorted(set(api_df['Expire_Year'].dropna().astype(str).unique()) | set(wildcard_df['Expire_Year'].dropna().astype(str).unique()))

st.title("Certificate Data Fetcher")

# Dropdown inputs
selected_url = st.selectbox("Select API or Wildcard URL", options=all_urls)
selected_month = st.selectbox("Select Expire Month", options=all_months)
selected_year = st.selectbox("Select Expire Year", options=all_years)

if st.button("Fetch"):
    # Filter both dataframes for matches
    filtered_api = api_df[
        (api_df['URL_name'] == selected_url) &
        (api_df['Expire_Month'] == selected_month) &
        (api_df['Expire_Year'].astype(str) == selected_year)
    ]
    filtered_wildcard = wildcard_df[
        (wildcard_df['Common_name'] == selected_url) &
        (wildcard_df['Expire_Month'] == selected_month) &
        (wildcard_df['Expire_Year'].astype(str) == selected_year)
    ]

    # Combine results
    filtered_df = pd.concat([filtered_api, filtered_wildcard], ignore_index=True)

    if filtered_df.empty:
        st.info("No records found for the selected inputs.")
    else:
        st.dataframe(filtered_df)

        # Download CSV button
        csv_data = filtered_df.to_csv(index=False)
        st.download_button("Download CSV", data=csv_data, file_name="filtered_cert_data.csv", mime="text/csv")
