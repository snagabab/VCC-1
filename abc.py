import streamlit as st
import pandas as pd

st.title("Certificate Viewer - OCP | VCC")

# Load your CSVs (from local directory or path in deployment)
api_df = pd.read_csv("api_cert_data.csv")
wildcard_df = pd.read_csv("wildcard_cert_data.csv")

# Clean column names (remove leading/trailing whitespace just in case)
api_df.columns = api_df.columns.str.strip()
wildcard_df.columns = wildcard_df.columns.str.strip()

# Add certificate type to differentiate
api_df['Certificate_Type'] = 'API Certificate'
wildcard_df['Certificate_Type'] = 'Wildcard Certificate'

# Combine
combined_df = pd.concat([api_df, wildcard_df], ignore_index=True)

# Convert Month and Year to numeric
combined_df['Expire_Month'] = pd.to_numeric(combined_df['Expire_Month'], errors='coerce')
combined_df['Expire_Year'] = pd.to_numeric(combined_df['Expire_Year'], errors='coerce')

# Sidebar filters
st.sidebar.header("Filter Certificates")

# Cluster (URL_name)
clusters = sorted(combined_df['URL_name'].dropna().unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", ["All"] + list(clusters))

# Year
years = sorted(combined_df['Expire_Year'].dropna().unique())
selected_year = st.sidebar.selectbox("Select Expire Year", ["All"] + list(map(int, years)))

# Month
months = sorted(combined_df['Expire_Month'].dropna().unique())
selected_month = st.sidebar.selectbox("Select Expire Month", ["All"] + list(map(int, months)))

# Filter logic
filtered_df = combined_df.copy()

if selected_cluster != "All":
    filtered_df = filtered_df[filtered_df['URL_name'] == selected_cluster]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df['Expire_Year'] == int(selected_year)]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df['Expire_Month'] == int(selected_month)]

# Display result
st.subheader(f"Filtered Certificates ({len(filtered_df)})")
st.dataframe(filtered_df)
