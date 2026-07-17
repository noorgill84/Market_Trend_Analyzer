"""
=========================================================
Market Trend Analyzer
Regional Analysis
=========================================================
"""

import streamlit as st
import plotly.express as px

from utils.data_loader import load_dashboard_data

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

df = load_dashboard_data()

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("Regional Analysis")

st.write(
    "Analyze sales and profit performance across different regions and states."
)

st.divider()

# ---------------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------------

st.sidebar.header("Regional Filters")

regions = sorted(df["Region"].unique())

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + regions
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

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]

# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Regions",
        filtered_df["Region"].nunique()
    )

with col2:
    st.metric(
        "States",
        filtered_df["State"].nunique()
    )

with col3:
    st.metric(
        "Sales",
        f"${filtered_df['Sales'].sum():,.2f}"
    )

with col4:
    st.metric(
        "Profit",
        f"${filtered_df['Profit'].sum():,.2f}"
    )

st.divider()

# ---------------------------------------------------------
# Sales by Region
# ---------------------------------------------------------

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    text_auto=".2s",
    title="Sales by Region"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Profit by Region
# ---------------------------------------------------------

region_profit = (
    filtered_df
    .groupby("Region")["Profit"]
    .sum()
    .reset_index()
)

fig = px.pie(
    region_profit,
    names="Region",
    values="Profit",
    title="Profit Distribution by Region"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Top States by Sales
# ---------------------------------------------------------

top_states = (
    filtered_df
    .groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_states,
    x="Sales",
    y="State",
    orientation="h",
    color="Sales",
    title="Top 10 States by Sales"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Top States by Profit
# ---------------------------------------------------------

profit_states = (
    filtered_df
    .groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    profit_states,
    x="Profit",
    y="State",
    orientation="h",
    color="Profit",
    title="Top 10 States by Profit"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Sales vs Profit
# ---------------------------------------------------------

comparison = (
    filtered_df
    .groupby("State")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

fig = px.scatter(
    comparison,
    x="Sales",
    y="Profit",
    hover_name="State",
    size="Sales",
    title="Sales vs Profit by State"
)

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Regional Summary Table
# ---------------------------------------------------------

st.subheader("Regional Summary")

summary = (
    filtered_df
    .groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("Order ID", "count"),
        States=("State", "nunique")
    )
    .reset_index()
)

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------------------------
# Download Report
# ---------------------------------------------------------

csv = summary.to_csv(index=False)

st.download_button(
    "Download Regional Report",
    csv,
    file_name="regional_analysis.csv",
    mime="text/csv"
)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Market Trend Analyzer | Regional Analysis"
)
