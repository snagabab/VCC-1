import streamlit as st
import pandas as pd

st.title("Certificate Viewer - OCP | VCC")

# Upload files
api_file = st.file_uploader("Upload API Certificate CSV", type="csv")
wildcard_file = st.file_uploader("Upload Wildcard Certificate CSV", type="csv")

if api_file is not None and wildcard_file is not None:
    api_df = pd.read_csv(api_file)
    wildcard_df = pd.read_csv(wildcard_file)

    # Clean column names
    api_df.columns = api_df.columns.str.strip()
    wildcard_df.columns = wildcard_df.columns.str.strip()

    # Add certificate type
    api_df['Certificate_Type'] = 'API'
    wildcard_df['Certificate_Type'] = 'Wildcard'

    # Combine
    combined_df = pd.concat([api_df, wildcard_df], ignore_index=True)
    combined_df['Expire_Month'] = pd.to_numeric(combined_df['Expire_Month'], errors='coerce')
    combined_df['Expire_Year'] = pd.to_numeric(combined_df['Expire_Year'], errors='coerce')

    # Sidebar filters
    st.sidebar.header("Filter Certificates")

    cert_types = ["All", "API", "Wildcard"]
    selected_cert_type = st.sidebar.selectbox("Select Cluster", cert_types)

    years = sorted(combined_df['Expire_Year'].dropna().unique())
    selected_year = st.sidebar.selectbox("Select Expire Year", ["All"] + list(map(int, years)))

    months = sorted(combined_df['Expire_Month'].dropna().unique())
    selected_month = st.sidebar.selectbox("Select Expire Month", ["All"] + list(map(int, months)))

    # Filter
    filtered_df = combined_df.copy()

    if selected_cert_type != "All":
        filtered_df = filtered_df[filtered_df['Certificate_Type'] == selected_cert_type]

    if selected_year != "All":
        filtered_df = filtered_df[filtered_df['Expire_Year'] == int(selected_year)]

    if selected_month != "All":
        filtered_df = filtered_df[filtered_df['Expire_Month'] == int(selected_month)]

    # Show result
    st.subheader(f"Filtered Certificates ({len(filtered_df)})")
    st.dataframe(filtered_df)

else:
    st.warning("Please upload both API and Wildcard certificate CSV files.")
