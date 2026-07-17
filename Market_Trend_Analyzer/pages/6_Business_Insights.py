"""
=========================================================
Market Trend Analyzer
Business Insights
=========================================================
Executive Business Summary
=========================================================
"""

import streamlit as st
import pandas as pd

from utils.data_loader import (
    load_dashboard_data,
    load_business_summary
)

from utils.helpers import (
    calculate_kpis,
    format_currency,
    average_shipping_days
)

# =========================================================
# Load Data
# =========================================================

df = load_dashboard_data()

summary_file = load_business_summary()

kpis = calculate_kpis(df)

# =========================================================
# Header
# =========================================================

st.title("Business Insights")

st.write(
    "Executive summary of key business performance indicators and recommendations."
)

st.divider()

# =========================================================
# KPI Cards
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Sales",
        format_currency(kpis["Total Sales"])
    )

with col2:

    st.metric(
        "Total Profit",
        format_currency(kpis["Total Profit"])
    )

with col3:

    st.metric(
        "Orders",
        f"{kpis['Total Orders']:,}"
    )

with col4:

    st.metric(
        "Customers",
        f"{kpis['Total Customers']:,}"
    )

st.divider()

# =========================================================
# Business Highlights
# =========================================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
)

best_category = category_sales.idxmax()

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

best_region = region_sales.idxmax()

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
)

best_segment = segment_sales.idxmax()

best_month = (
    df.groupby(df["Order Date"].dt.month_name())["Sales"]
    .sum()
    .idxmax()
)

avg_shipping = average_shipping_days(df)

left, right = st.columns(2)

with left:

    st.subheader("Business Highlights")

    st.info(f"Top Category : {best_category}")

    st.info(f"Top Region : {best_region}")

    st.info(f"Top Customer Segment : {best_segment}")

    st.info(f"Highest Sales Month : {best_month}")

with right:

    st.subheader("Operational Summary")

    st.info(f"Average Shipping Time : {avg_shipping} Days")

    st.info(
        f"Average Order Value : {format_currency(kpis['Average Order Value'])}"
    )

    st.info(
        f"Categories Available : {df['Category'].nunique()}"
    )

    st.info(
        f"States Covered : {df['State'].nunique()}"
    )

st.divider()

# =========================================================
# Market Trend
# =========================================================

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

growth = monthly_sales.pct_change().iloc[-1] * 100

if growth > 10:

    trend = "Growing"

    message = (
        "Sales are increasing steadily. "
        "Current market conditions are favorable."
    )

elif growth < -10:

    trend = "Declining"

    message = (
        "Sales have declined compared to the previous period. "
        "Review pricing, promotions, and inventory planning."
    )

else:

    trend = "Stable"

    message = (
        "Sales remain relatively stable with no significant changes."
    )

st.subheader("Market Trend")

col1, col2 = st.columns([1, 3])

with col1:

    st.metric(
        "Current Trend",
        trend
    )

with col2:

    st.write(message)

st.divider()

# =========================================================
# Business Recommendations
# =========================================================

st.subheader("Business Recommendations")

recommendations = [

    f"Increase inventory for the **{best_category}** category.",

    f"Focus marketing campaigns in the **{best_region}** region.",

    f"Target **{best_segment}** customers with personalized offers.",

    f"Prepare inventory before **{best_month}** due to higher sales demand.",

    "Monitor discount levels to maintain healthy profit margins.",

    "Continue tracking monthly sales trends for better forecasting."

]

for rec in recommendations:

    st.write(f"• {rec}")

st.divider()

# =========================================================
# Dataset Summary
# =========================================================

st.subheader("Dataset Summary")

dataset_summary = pd.DataFrame({

    "Metric":[

        "Rows",

        "Columns",

        "Regions",

        "States",

        "Categories",

        "Sub-Categories"

    ],

    "Value":[

        len(df),

        len(df.columns),

        df["Region"].nunique(),

        df["State"].nunique(),

        df["Category"].nunique(),

        df["Sub-Category"].nunique()

    ]

})

st.dataframe(

    dataset_summary,

    use_container_width=True,

    hide_index=True

)

st.divider()

# =========================================================
# Business Summary File
# =========================================================

if summary_file is not None:

    st.subheader("Generated Business Summary")

    st.dataframe(

        summary_file,

        use_container_width=True,

        hide_index=True

    )

st.divider()

# =========================================================
# Download Report
# =========================================================

report = pd.DataFrame({

    "Metric":[

        "Total Sales",

        "Total Profit",

        "Orders",

        "Customers",

        "Top Category",

        "Top Region",

        "Top Segment",

        "Highest Sales Month",

        "Average Shipping Days",

        "Market Trend"

    ],

    "Value":[

        kpis["Total Sales"],

        kpis["Total Profit"],

        kpis["Total Orders"],

        kpis["Total Customers"],

        best_category,

        best_region,

        best_segment,

        best_month,

        avg_shipping,

        trend

    ]

})

csv = report.to_csv(index=False)

st.download_button(

    label="Download Business Report",

    data=csv,

    file_name="business_insights.csv",

    mime="text/csv"

)

st.divider()

st.caption("Market Trend Analyzer | Business Insights")
