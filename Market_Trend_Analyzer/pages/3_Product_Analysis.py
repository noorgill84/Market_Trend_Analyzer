"""
=========================================================
Market Trend Analyzer
Product Analysis
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_dashboard_data

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.title("Product Analysis")

st.write(
    "Analyze product, category, and sub-category performance."
)

st.divider()

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

df = load_dashboard_data()

# ---------------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------------

st.sidebar.header("Product Filters")

categories = sorted(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + categories
)

segments = sorted(df["Segment"].unique())

selected_segment = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + segments
)

# ---------------------------------------------------------
# Apply Filters
# ---------------------------------------------------------

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]

# ---------------------------------------------------------
# KPIs
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Products",
        filtered_df["Product Name"].nunique()
    )

with col2:
    st.metric(
        "Categories",
        filtered_df["Category"].nunique()
    )

with col3:
    st.metric(
        "Sub-Categories",
        filtered_df["Sub-Category"].nunique()
    )

with col4:
    st.metric(
        "Total Quantity",
        int(filtered_df["Quantity"].sum())
    )

st.divider()

# ---------------------------------------------------------
# Category Sales
# ---------------------------------------------------------

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    text_auto=".2s",
    title="Sales by Category"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Sub Category Sales
# ---------------------------------------------------------

subcategory_sales = (
    filtered_df
    .groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    subcategory_sales,
    x="Sales",
    y="Sub-Category",
    orientation="h",
    color="Sales",
    title="Sales by Sub-Category"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Top Products
# ---------------------------------------------------------

st.subheader("Top 10 Products")

top_products = (
    filtered_df
    .groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values(
        by="Sales",
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    text_auto=".2s",
    title="Top Selling Products"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Profit by Category
# ---------------------------------------------------------

profit_category = (
    filtered_df
    .groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig = px.pie(
    profit_category,
    names="Category",
    values="Profit",
    title="Profit Distribution by Category"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Quantity Sold
# ---------------------------------------------------------

quantity = (
    filtered_df
    .groupby("Sub-Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    quantity,
    x="Sub-Category",
    y="Quantity",
    color="Quantity",
    title="Quantity Sold by Sub-Category"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Product Performance Table
# ---------------------------------------------------------

st.subheader("Product Performance")

performance = (
    filtered_df
    .groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"),
        Orders=("Order ID", "count")
    )
    .sort_values(
        by="Sales",
        ascending=False
    )
    .reset_index()
)

st.dataframe(
    performance,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------------------------
# Download Report
# ---------------------------------------------------------

csv = performance.to_csv(index=False)

st.download_button(
    "Download Product Report",
    csv,
    "product_analysis.csv",
    "text/csv"
)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Market Trend Analyzer | Product Analysis"
)
