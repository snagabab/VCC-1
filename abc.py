import streamlit as st
import pandas as pd

st.title("Certificate Viewer - OCP | VCC")

# Upload CSV files
st.sidebar.header("Upload Certificate CSV Files")
api_cert_file = st.sidebar.file_uploader("Upload API Certificate CSV", type=["csv"])
wildcard_cert_file = st.sidebar.file_uploader("Upload Wildcard Certificate CSV", type=["csv"])

if api_cert_file and wildcard_cert_file:
    # Read CSVs
    api_df = pd.read_csv(api_cert_file)
    wildcard_df = pd.read_csv(wildcard_cert_file)

    # Add a source column to distinguish
    api_df['Certificate_Type'] = 'API Certificate'
    wildcard_df['Certificate_Type'] = 'Wildcard Certificate'

    # Combine both DataFrames
    cert_df = pd.concat([api_df, wildcard_df], ignore_index=True)

    # Sidebar filters
    st.sidebar.header("Filter Certificates")

    # Unique years and months from data
    years = cert_df['Expire_Year'].dropna().unique()
    months = cert_df['Expire_Month'].dropna().unique()

    # Select year filter (allow multi-select)
    selected_years = st.sidebar.multiselect("Select Expire Year(s)", options=sorted(years), default=sorted(years))

    # Select month filter (allow multi-select)
    selected_months = st.sidebar.multiselect("Select Expire Month(s)", options=sorted(months), default=sorted(months))

    # Filter dataframe based on selections
    filtered_df = cert_df[
        (cert_df['Expire_Year'].isin(selected_years)) &
        (cert_df['Expire_Month'].isin(selected_months))
    ]

    # Show filtered data
    st.subheader(f"Filtered Certificates ({len(filtered_df)} results)")
    st.dataframe(filtered_df)

else:
    st.info("Please upload both API Certificate CSV and Wildcard Certificate CSV files from the sidebar.")
