"""
=========================================================
Market Trend Analyzer
Charts Module
=========================================================
Reusable Plotly Charts
=========================================================
"""

import plotly.express as px


# =========================================================
# Common Layout
# =========================================================

def apply_layout(fig, title):

    fig.update_layout(

        title=title,

        title_font_size=22,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            family="Arial",
            size=13,
            color="#1F2937"
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        height=450,

        legend_title_text="",

        title_x=0.02

    )

    return fig


# =========================================================
# Monthly Sales Trend
# =========================================================

def monthly_sales_chart(monthly_df):

    fig = px.line(

        monthly_df,

        x="Order Date",

        y="Sales",

        markers=True

    )

    fig.update_traces(line=dict(width=3))

    return apply_layout(fig, "Monthly Sales Trend")


# =========================================================
# Sales by Category
# =========================================================

def category_chart(df):

    category = (

        df.groupby("Category")["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.bar(

        category,

        x="Category",

        y="Sales",

        color="Category",

        text_auto=".2s"

    )

    return apply_layout(fig, "Sales by Category")


# =========================================================
# Profit by Category
# =========================================================

def profit_category_chart(df):

    category = (

        df.groupby("Category")["Profit"]

        .sum()

        .reset_index()

    )

    fig = px.bar(

        category,

        x="Category",

        y="Profit",

        color="Category",

        text_auto=".2s"

    )

    return apply_layout(fig, "Profit by Category")


# =========================================================
# Region Sales
# =========================================================

def region_chart(df):

    region = (

        df.groupby("Region")["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.pie(

        region,

        names="Region",

        values="Sales"

    )

    return apply_layout(fig, "Regional Sales Distribution")


# =========================================================
# Segment Sales
# =========================================================

def segment_chart(df):

    segment = (

        df.groupby("Segment")["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.pie(

        segment,

        names="Segment",

        values="Sales"

    )

    return apply_layout(fig, "Sales by Customer Segment")


# =========================================================
# Top Products
# =========================================================

def top_products_chart(products_df):

    fig = px.bar(

        products_df,

        x="Sales",

        y="Product Name",

        orientation="h",

        text_auto=".2s"

    )

    return apply_layout(fig, "Top Selling Products")


# =========================================================
# Top States
# =========================================================

def state_chart(states_df):

    fig = px.bar(

        states_df,

        x="State",

        y="Sales",

        color="Sales",

        text_auto=".2s"

    )

    return apply_layout(fig, "Top States by Sales")


# =========================================================
# Discount vs Profit
# =========================================================

def discount_profit_chart(df):

    fig = px.scatter(

        df,

        x="Discount",

        y="Profit",

        color="Category",

        hover_name="Product Name"

    )

    return apply_layout(fig, "Discount vs Profit")


# =========================================================
# Sales Distribution
# =========================================================

def sales_distribution(df):

    fig = px.histogram(

        df,

        x="Sales",

        nbins=40

    )

    return apply_layout(fig, "Sales Distribution")


# =========================================================
# Profit Distribution
# =========================================================

def profit_distribution(df):

    fig = px.histogram(

        df,

        x="Profit",

        nbins=40

    )

    return apply_layout(fig, "Profit Distribution")


# =========================================================
# Shipping Mode
# =========================================================

def shipping_chart(df):

    ship = (

        df.groupby("Ship Mode")["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.bar(

        ship,

        x="Ship Mode",

        y="Sales",

        color="Ship Mode",

        text_auto=".2s"

    )

    return apply_layout(fig, "Sales by Shipping Mode")
