import streamlit as st
import pandas as pd
from io import StringIO

# Load CSVs in background
api_df = pd.read_csv("api_cert_data.csv")
wildcard_df = pd.read_csv("wildcard_cert_data.csv")

st.title("Certificate Data Fetcher")

# Input fields
url_input = st.text_input("Enter API or Wildcard URL")
month_input = st.text_input("Enter Expire Month (e.g. January)")
year_input = st.text_input("Enter Expire Year (e.g. 2025)")

if st.button("Fetch"):
    if not url_input or not month_input or not year_input:
        st.error("Please fill all the input fields.")
    else:
        # Select which df to search in based on input URL presence in either df
        if url_input in api_df['URL_name'].values:
            df = api_df
        elif url_input in wildcard_df['Common_name'].values:
            df = wildcard_df
        else:
            st.warning("URL not found in any data.")
            st.stop()

        # Filter dataframe on month and year too (case insensitive)
        filtered_df = df[
            (df['URL_name'].str.contains(url_input, case=False, na=False) | 
             df['Common_name'].str.contains(url_input, case=False, na=False))
            & (df['Expire_Month'].str.lower() == month_input.lower())
            & (df['Expire_Year'].astype(str) == year_input)
        ]

        if filtered_df.empty:
            st.info("No records found for this input.")
        else:
            st.dataframe(filtered_df)

            # CSV download
            csv_data = filtered_df.to_csv(index=False)
            st.download_button("Download CSV", data=csv_data, file_name="filtered_cert_data.csv", mime="text/csv")
