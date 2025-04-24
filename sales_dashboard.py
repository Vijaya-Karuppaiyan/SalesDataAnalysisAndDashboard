import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data_sample.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Revenue'] = df['Units Sold'] * df['Unit Price']

st.set_page_config(layout="wide")
st.title("📊 Sales Dashboard")

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")
product = st.sidebar.multiselect("Select Product(s):", df['Product'].unique(), default=df['Product'].unique())
region = st.sidebar.multiselect("Select Region(s):", df['Region'].unique(), default=df['Region'].unique())

# Date range filter
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input("Select Date Range:", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filtered Data
filtered_df = df[
    (df['Product'].isin(product)) &
    (df['Region'].isin(region)) &
    (df['Date'] >= pd.to_datetime(date_range[0])) &
    (df['Date'] <= pd.to_datetime(date_range[1]))
]

# KPIs
col1, col2 = st.columns(2)
col1.metric("🛒 Total Units Sold", filtered_df['Units Sold'].sum())
col2.metric("💰 Total Revenue", f"${filtered_df['Revenue'].sum():,.2f}")

# Line Chart - Monthly Sales Trend
st.subheader("📅 Monthly Revenue Trend")
monthly = filtered_df.groupby(filtered_df['Date'].dt.to_period('M')).agg({'Revenue': 'sum'})
monthly.index = monthly.index.astype(str)
st.line_chart(monthly)

# Bar Chart - Product Comparison
st.subheader("📦 Product-wise Revenue Comparison")
product_revenue = filtered_df.groupby('Product')['Revenue'].sum().sort_values()
fig1, ax1 = plt.subplots()
product_revenue.plot(kind='barh', color='orange', ax=ax1)
ax1.set_xlabel("Revenue")
st.pyplot(fig1)

# Pie Chart - Revenue by Category
st.subheader("🎯 Revenue by Category")
category_revenue = filtered_df.groupby('Category')['Revenue'].sum()
fig2, ax2 = plt.subplots()
category_revenue.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel('')
st.pyplot(fig2)

# Download Button
st.subheader("⬇️ Download Filtered Report")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", data=csv, file_name='filtered_sales_report.csv', mime='text/csv')
