import streamlit as st
import pandas as pd

st.title("Certificate Viewer - OCP | VCC")

# Load your CSVs
api_df = pd.read_csv("api_certificate.csv")
wildcard_df = pd.read_csv("wildcard_certificate.csv")

# Clean column names
api_df.columns = api_df.columns.str.strip()
wildcard_df.columns = wildcard_df.columns.str.strip()

# Add certificate type
api_df['Certificate_Type'] = 'API Certificate'
wildcard_df['Certificate_Type'] = 'Wildcard Certificate'

# Combine both
combined_df = pd.concat([api_df, wildcard_df], ignore_index=True)

# Convert month and year columns to numeric
combined_df['Expire_Month'] = pd.to_numeric(combined_df['Expire_Month'], errors='coerce')
combined_df['Expire_Year'] = pd.to_numeric(combined_df['Expire_Year'], errors='coerce')

# Sidebar filters
st.sidebar.header("Filter Certificates")

# ✅ Filter by Certificate Type (not URL_name)
cert_types = sorted(combined_df['Certificate_Type'].dropna().unique())
selected_cluster = st.sidebar.selectbox("Select Certificate Type", ["All"] + list(cert_types))

# Year filter
years = sorted(combined_df['Expire_Year'].dropna().unique())
selected_year = st.sidebar.selectbox("Select Expire Year", ["All"] + list(map(int, years)))

# Month filter
months = sorted(combined_df['Expire_Month'].dropna().unique())
selected_month = st.sidebar.selectbox("Select Expire Month", ["All"] + list(map(int, months)))

# Apply filters
filtered_df = combined_df.copy()

if selected_cluster != "All":
    filtered_df = filtered_df[filtered_df['Certificate_Type'] == selected_cluster]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df['Expire_Year'] == int(selected_year)]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df['Expire_Month'] == int(selected_month)]

# Display results
st.subheader(f"Filtered Certificates ({len(filtered_df)})")
st.dataframe(filtered_df)
