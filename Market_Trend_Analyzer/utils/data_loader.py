"""
=========================================================
Market Trend Analyzer
Data Loader Module
=========================================================
Loads datasets and trained ML model.

Author : Your Name
=========================================================
"""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# =========================================================
# Project Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

MODEL_DIR = BASE_DIR /"models"

# =========================================================
# Dashboard Dataset
# =========================================================

@st.cache_data
def load_dashboard_data():
    """
    Load cleaned dashboard dataset.
    """

    file_path = DATA_DIR / "Dashboard_Data.csv"

    if not file_path.exists():
        st.error(f"Dashboard dataset not found:\n{file_path}")
        st.stop()

    df = pd.read_csv(file_path)

    # Convert dates
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"])

    if "Ship Date" in df.columns:
        df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    return df


# =========================================================
# ML Dataset
# =========================================================

@st.cache_data
def load_ml_data():
    """
    Load machine learning dataset.
    """

    file_path = DATA_DIR / "ML_Data.csv"

    if not file_path.exists():
        st.error(f"ML dataset not found:\n{file_path}")
        st.stop()

    return pd.read_csv(file_path)


# =========================================================
# Business Summary
# =========================================================

@st.cache_data
def load_business_summary():
    """
    Load business summary generated from notebook.
    """

    file_path = DATA_DIR / "business_summary.csv"

    if not file_path.exists():
        return None

    return pd.read_csv(file_path)


# =========================================================
# Model Loader
# =========================================================

@st.cache_resource
def load_model():
    """
    Load trained Sales Prediction model.
    """

    model_path = MODEL_DIR / "sales_prediction_model.pkl"

    if not model_path.exists():
        st.error(f"Model not found:\n{model_path}")
        st.stop()

    model = joblib.load(model_path)

    return model


# =========================================================
# Dataset Information
# =========================================================

@st.cache_data
def dataset_information():

    df = load_dashboard_data()

    info = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Sales": df["Sales"].sum(),
        "Profit": df["Profit"].sum(),
        "Orders": df["Order ID"].nunique(),
        "Customers": df["Customer ID"].nunique(),
        "Regions": df["Region"].nunique(),
        "States": df["State"].nunique(),
        "Categories": df["Category"].nunique(),
        "Sub Categories": df["Sub-Category"].nunique()
    }

    return info


# =========================================================
# Filter Dataset
# =========================================================

def filter_dataset(
    df,
    year=None,
    region=None,
    category=None,
    segment=None
):
    """
    Generic dataset filter used across dashboard pages.
    """

    filtered_df = df.copy()

    if year and year != "All":
        filtered_df = filtered_df[
            filtered_df["Order Date"].dt.year == year
        ]

    if region and region != "All":
        filtered_df = filtered_df[
            filtered_df["Region"] == region
        ]

    if category and category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    if segment and segment != "All":
        filtered_df = filtered_df[
            filtered_df["Segment"] == segment
        ]

    return filtered_df


# =========================================================
# Dropdown Options
# =========================================================

@st.cache_data
def get_dropdown_options():

    df = load_dashboard_data()

    return {
        "ship_modes": sorted(df["Ship Mode"].dropna().unique()),
        "segments": sorted(df["Segment"].dropna().unique()),
        "cities": sorted(df["City"].dropna().unique()),
        "states": sorted(df["State"].dropna().unique()),
        "regions": sorted(df["Region"].dropna().unique()),
        "categories": sorted(df["Category"].dropna().unique()),
        "sub_categories": sorted(df["Sub-Category"].dropna().unique()),
        "years": sorted(df["Year"].dropna().unique()),
        "months": sorted(df["Month"].dropna().unique())
    }
