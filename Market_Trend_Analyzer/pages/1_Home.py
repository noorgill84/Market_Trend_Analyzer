"""
=========================================================
Market Trend Analyzer
Home Dashboard
=========================================================
"""

import streamlit as st

from utils.data_loader import load_dashboard_data
from utils.helpers import (
    calculate_kpis,
    format_currency,
    monthly_sales,
    top_products
)

from utils.charts import (
    monthly_sales_chart,
    category_chart,
    region_chart,
    top_products_chart
)

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = load_dashboard_data()

kpi = calculate_kpis(df)

# -----------------------------------------------------
# Header
# -----------------------------------------------------

st.title("Dashboard")

st.write(
    "Executive overview of sales performance, regional performance, "
    "product performance, and key business metrics."
)

st.divider()

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(
        f"""
        <div class="metric-card">

        <div class="metric-title">
        Total Sales
        </div>

        <div class="metric-value">
        {format_currency(kpi["Total Sales"])}
        </div>

        <div class="metric-desc">
        Overall Revenue
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class="metric-card">

        <div class="metric-title">
        Total Profit
        </div>

        <div class="metric-value">
        {format_currency(kpi["Total Profit"])}
        </div>

        <div class="metric-desc">
        Net Profit
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        f"""
        <div class="metric-card">

        <div class="metric-title">
        Orders
        </div>

        <div class="metric-value">
        {kpi["Total Orders"]:,}
        </div>

        <div class="metric-desc">
        Unique Orders
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c4:

    st.markdown(
        f"""
        <div class="metric-card">

        <div class="metric-title">
        Customers
        </div>

        <div class="metric-value">
        {kpi["Total Customers"]:,}
        </div>

        <div class="metric-desc">
        Active Customers
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# -----------------------------------------------------
# Monthly Trend
# -----------------------------------------------------

st.subheader("Monthly Sales Trend")

monthly = monthly_sales(df)

fig = monthly_sales_chart(monthly)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Category & Region
# -----------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("Category Performance")

    fig = category_chart(df)

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Regional Performance")

    fig = region_chart(df)

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Top Products
# -----------------------------------------------------

st.subheader("Top Selling Products")

products = top_products(df)

fig = top_products_chart(products)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Business Snapshot
# -----------------------------------------------------

st.subheader("Business Snapshot")

col1, col2 = st.columns(2)

with col1:

    st.dataframe(

        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index(),

        use_container_width=True

    )

with col2:

    st.dataframe(

        df.groupby("Region")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .reset_index(),

        use_container_width=True

    )

# -----------------------------------------------------
# Footer
# -----------------------------------------------------

st.divider()

st.caption(
    "Market Trend Analyzer | Dashboard Overview"
)
