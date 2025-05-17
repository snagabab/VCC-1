import streamlit as st
import pandas as pd

st.title("Certificate Viewer - OCP | VCC")

# Load CSV files in the background
api_df = pd.read_csv("api_cert_data.csv")
wildcard_df = pd.read_csv("wildcard_cert_data.csv")

# Add a column to identify certificate type
api_df['Certificate_Type'] = 'API Certificate'
wildcard_df['Certificate_Type'] = 'Wildcard Certificate'

# Combine both dataframes
cert_df = pd.concat([api_df, wildcard_df], ignore_index=True)

# Assume 'URL_name' or 'Cluster' column represents cluster? 
# If you want to filter by cluster, we need a column name for it.
# Assuming you want to filter by 'URL_name' as cluster proxy
clusters = cert_df['URL_name'].unique()
clusters = sorted(clusters)

# Sidebar filters
st.sidebar.header("Filter Certificates")

# Cluster filter (All or specific)
selected_cluster = st.sidebar.selectbox("Select Cluster", options=["All"] + list(clusters))

# Year filter
years = sorted(cert_df['Expire_Year'].dropna().unique())
selected_year = st.sidebar.selectbox("Select Expire Year", options=["All"] + list(years))

# Month filter
months = sorted(cert_df['Expire_Month'].dropna().unique())
selected_month = st.sidebar.selectbox("Select Expire Month", options=["All"] + list(months))

# Apply filters
filtered_df = cert_df.copy()

if selected_cluster != "All":
    filtered_df = filtered_df[filtered_df['URL_name'] == selected_cluster]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df['Expire_Year'] == selected_year]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df['Expire_Month'] == selected_month]

st.subheader(f"Filtered Certificates ({len(filtered_df)})")
st.dataframe(filtered_df)
import streamlit as st
import pandas as pd

st.title("Certificate Viewer - OCP | VCC")

# Load CSV files in the background
api_df = pd.read_csv("api_certificate.csv")
wildcard_df = pd.read_csv("wildcard_certificate.csv")

# Add a column to identify certificate type
api_df['Certificate_Type'] = 'API Certificate'
wildcard_df['Certificate_Type'] = 'Wildcard Certificate'

# Combine both dataframes
cert_df = pd.concat([api_df, wildcard_df], ignore_index=True)

# Assume 'URL_name' or 'Cluster' column represents cluster? 
# If you want to filter by cluster, we need a column name for it.
# Assuming you want to filter by 'URL_name' as cluster proxy
clusters = cert_df['URL_name'].unique()
clusters = sorted(clusters)

# Sidebar filters
st.sidebar.header("Filter Certificates")

# Cluster filter (All or specific)
selected_cluster = st.sidebar.selectbox("Select Cluster", options=["All"] + list(clusters))

# Year filter
years = sorted(cert_df['Expire_Year'].dropna().unique())
selected_year = st.sidebar.selectbox("Select Expire Year", options=["All"] + list(years))

# Month filter
months = sorted(cert_df['Expire_Month'].dropna().unique())
selected_month = st.sidebar.selectbox("Select Expire Month", options=["All"] + list(months))

# Apply filters
filtered_df = cert_df.copy()

if selected_cluster != "All":
    filtered_df = filtered_df[filtered_df['URL_name'] == selected_cluster]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df['Expire_Year'] == selected_year]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df['Expire_Month'] == selected_month]

st.subheader(f"Filtered Certificates ({len(filtered_df)})")
st.dataframe(filtered_df)
