"""
=========================================================
Market Trend Analyzer
Sales Analysis
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_dashboard_data

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

df = load_dashboard_data()

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("Sales Analysis")

st.write(
    "Analyze sales performance using interactive charts and filters."
)

st.divider()

# ---------------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------------

st.sidebar.header("Filters")

years = sorted(df["Order Date"].dt.year.unique())

selected_year = st.sidebar.selectbox(
    "Year",
    options=["All"] + years
)

regions = sorted(df["Region"].unique())

selected_region = st.sidebar.selectbox(
    "Region",
    options=["All"] + regions
)

# ---------------------------------------------------------
# Apply Filters
# ---------------------------------------------------------

filtered_df = df.copy()

if selected_year != "All":

    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.year == selected_year
    ]

if selected_region != "All":

    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

# ---------------------------------------------------------
# KPI Section
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"${filtered_df['Sales'].sum():,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${filtered_df['Profit'].sum():,.2f}"
    )

with col3:
    st.metric(
        "Total Orders",
        filtered_df["Order ID"].nunique()
    )

st.divider()

# ---------------------------------------------------------
# Monthly Sales Trend
# ---------------------------------------------------------

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Yearly Sales Trend
# ---------------------------------------------------------

yearly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.year)["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    yearly_sales,
    x="Order Date",
    y="Sales",
    text_auto=".2s",
    title="Yearly Sales"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Category Performance
# ---------------------------------------------------------

left, right = st.columns(2)

with left:

    category = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category,
        x="Category",
        y="Sales",
        color="Category",
        text_auto=".2s",
        title="Sales by Category"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.histogram(
        filtered_df,
        x="Sales",
        nbins=40,
        title="Sales Distribution"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Discount vs Profit
# ---------------------------------------------------------

fig = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    color="Category",
    hover_name="Product Name",
    title="Discount vs Profit"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Sales Summary Table
# ---------------------------------------------------------

st.subheader("Sales Summary")

summary = (
    filtered_df
    .groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("Order ID", "count")
    )
    .reset_index()
)

st.dataframe(
    summary,
    use_container_width=True
)

# ---------------------------------------------------------
# Download Filtered Data
# ---------------------------------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="sales_analysis.csv",
    mime="text/csv"
)
