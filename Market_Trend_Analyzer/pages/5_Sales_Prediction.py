"""
=========================================================
Market Trend Analyzer
Sales Prediction
=========================================================
"""

import pandas as pd
import streamlit as st

from utils.data_loader import (
    load_dashboard_data,
    load_model
)

# ---------------------------------------------------------
# Load Data & Model
# ---------------------------------------------------------

df = load_dashboard_data()
model = load_model()

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("Sales Prediction")

st.write(
    "Predict the expected sales amount based on order details."
)

st.divider()

# ---------------------------------------------------------
# Input Form
# ---------------------------------------------------------

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        ship_mode = st.selectbox(
            "Ship Mode",
            sorted(df["Ship Mode"].unique())
        )

        segment = st.selectbox(
            "Segment",
            sorted(df["Segment"].unique())
        )

        city = st.selectbox(
            "City",
            sorted(df["City"].unique())
        )

        state = st.selectbox(
            "State",
            sorted(df["State"].unique())
        )

        region = st.selectbox(
            "Region",
            sorted(df["Region"].unique())
        )

        category = st.selectbox(
            "Category",
            sorted(df["Category"].unique())
        )

    with col2:

        sub_category = st.selectbox(
            "Sub-Category",
            sorted(df["Sub-Category"].unique())
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=20,
            value=2
        )

        discount = st.number_input(
            "Discount",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            step=0.05
        )

        shipping_days = st.number_input(
            "Shipping Days",
            min_value=0,
            max_value=30,
            value=4
        )

        year = st.selectbox(
            "Year",
            sorted(df["Year"].unique())
        )

        month = st.selectbox(
            "Month",
            sorted(df["Month"].unique())
        )

    submitted = st.form_submit_button("Predict Sales")

# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if submitted:

    input_data = pd.DataFrame({

        "Ship Mode":[ship_mode],

        "Segment":[segment],

        "City":[city],

        "State":[state],

        "Region":[region],

        "Category":[category],

        "Sub-Category":[sub_category],

        "Quantity":[quantity],

        "Discount":[discount],

        "Shipping Days":[shipping_days],

        "Year":[year],

        "Month":[month]

    })

    prediction = model.predict(input_data)[0]

    st.divider()

    st.subheader("Prediction Result")

    st.metric(
        label="Predicted Sales",
        value=f"${prediction:,.2f}"
    )

    # -----------------------------------------------------
    # Simple Business Interpretation
    # -----------------------------------------------------

    if prediction >= 1000:

        st.success(
            "This order is expected to generate high sales."
        )

    elif prediction >= 500:

        st.info(
            "This order is expected to generate moderate sales."
        )

    else:

        st.warning(
            "This order is expected to generate relatively low sales."
        )

    # -----------------------------------------------------
    # Prediction Summary
    # -----------------------------------------------------

    st.subheader("Prediction Summary")

    summary = input_data.copy()

    summary["Predicted Sales"] = round(prediction,2)

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    csv = summary.to_csv(index=False)

    st.download_button(

        "Download Prediction",

        data=csv,

        file_name="sales_prediction.csv",

        mime="text/csv"

    )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Market Trend Analyzer | Sales Prediction"
)
