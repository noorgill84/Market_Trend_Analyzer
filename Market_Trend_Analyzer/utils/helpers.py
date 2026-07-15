"""
=========================================================
Market Trend Analyzer
Helper Functions
=========================================================
"""

import pandas as pd


# --------------------------------------------------
# Currency Formatter
# --------------------------------------------------

def format_currency(value):
    """
    Convert numbers into readable currency format.

    Example:
    2500 -> $2,500
    2500000 -> $2.50 M
    """

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f} M"

    elif value >= 1_000:
        return f"${value/1_000:.2f} K"

    return f"${value:.2f}"


# --------------------------------------------------
# Percentage Formatter
# --------------------------------------------------

def format_percentage(value):

    return f"{value:.2f}%"


# --------------------------------------------------
# KPI Calculator
# --------------------------------------------------

def calculate_kpis(df):

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order ID"].nunique()

    total_customers = df["Customer ID"].nunique()

    average_order_value = total_sales / total_orders

    return {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Total Orders": total_orders,
        "Total Customers": total_customers,
        "Average Order Value": average_order_value,
    }


# --------------------------------------------------
# Monthly Sales
# --------------------------------------------------

def monthly_sales(df):

    monthly = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )

    monthly["Order Date"] = monthly["Order Date"].astype(str)

    return monthly


# --------------------------------------------------
# Category Sales
# --------------------------------------------------

def category_sales(df):

    return (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


# --------------------------------------------------
# Region Sales
# --------------------------------------------------

def region_sales(df):

    return (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


# --------------------------------------------------
# Top Products
# --------------------------------------------------

def top_products(df, n=10):

    return (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


# --------------------------------------------------
# Top States
# --------------------------------------------------

def top_states(df, n=10):

    return (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


# --------------------------------------------------
# Customer Segments
# --------------------------------------------------

def segment_sales(df):

    return (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )


# --------------------------------------------------
# Shipping Days
# --------------------------------------------------

def average_shipping_days(df):

    shipping = (df["Ship Date"] - df["Order Date"]).dt.days

    return round(shipping.mean(), 2)


# --------------------------------------------------
# Business Summary
# --------------------------------------------------

def business_summary(df):

    best_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    best_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    best_segment = (
        df.groupby("Segment")["Sales"]
        .sum()
        .idxmax()
    )

    best_month = (
        df.groupby(df["Order Date"].dt.month_name())["Sales"]
        .sum()
        .idxmax()
    )

    return {
        "Top Category": best_category,
        "Top Region": best_region,
        "Top Segment": best_segment,
        "Best Month": best_month,
        "Average Shipping Days": average_shipping_days(df),
    }
