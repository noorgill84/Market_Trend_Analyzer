"""
=========================================================
Market Trend Analyzer
About
=========================================================
"""

import streamlit as st

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("About")

st.write(
    "Information about the project, dataset, technology stack, "
    "and implementation."
)

st.divider()

# ---------------------------------------------------------
# Project Overview
# ---------------------------------------------------------

st.header("Project Overview")

st.write(
"""
The **Market Trend Analyzer** is a Business Intelligence and Data Analytics
dashboard developed to analyze historical sales data and generate meaningful
business insights.

The application combines descriptive analytics, interactive visualizations,
and machine learning to help organizations understand sales performance,
customer behavior, product trends, and regional performance.
"""
)

# ---------------------------------------------------------
# Objectives
# ---------------------------------------------------------

st.header("Project Objectives")

objectives = [

    "Analyze historical sales data.",

    "Identify product and regional trends.",

    "Generate business insights.",

    "Predict future sales using Machine Learning.",

    "Support business decision making through interactive dashboards."

]

for item in objectives:
    st.write(f"• {item}")

st.divider()

# ---------------------------------------------------------
# Dataset
# ---------------------------------------------------------

st.header("Dataset")

dataset = {

    "Dataset Name": "Sample Superstore",

    "Records": "Approximately 10,000",

    "Domain": "Retail",

    "Target Variable": "Sales"

}

for key, value in dataset.items():

    col1, col2 = st.columns([1,2])

    with col1:
        st.write(f"**{key}**")

    with col2:
        st.write(value)

st.divider()

# ---------------------------------------------------------
# Dashboard Modules
# ---------------------------------------------------------

st.header("Dashboard Modules")

modules = [

    "Home Dashboard",

    "Sales Analysis",

    "Product Analysis",

    "Regional Analysis",

    "Sales Prediction",

    "Business Insights"

]

for module in modules:

    st.write(f"• {module}")

st.divider()

# ---------------------------------------------------------
# Machine Learning
# ---------------------------------------------------------

st.header("Machine Learning")

st.write(
"""
The project includes a Sales Prediction module built using
supervised machine learning techniques.

Multiple regression models were evaluated and the best-performing
model was selected based on prediction accuracy.
"""
)

ml_table = {

    "Task": "Regression",

    "Target": "Sales",

    "Algorithms":

        "Linear Regression, Decision Tree, Random Forest, Gradient Boosting"

}

for key, value in ml_table.items():

    col1, col2 = st.columns([1,2])

    with col1:
        st.write(f"**{key}**")

    with col2:
        st.write(value)

st.divider()

# ---------------------------------------------------------
# Technology Stack
# ---------------------------------------------------------

st.header("Technology Stack")

tech = [

    "Python",

    "Pandas",

    "NumPy",

    "Scikit-learn",

    "Plotly",

    "Streamlit",

    "Joblib"

]

left, right = st.columns(2)

mid = (len(tech)+1)//2

with left:

    for item in tech[:mid]:

        st.write(f"• {item}")

with right:

    for item in tech[mid:]:

        st.write(f"• {item}")

st.divider()

# ---------------------------------------------------------
# Project Workflow
# ---------------------------------------------------------

st.header("Project Workflow")

workflow = [

    "Data Collection",

    "Data Cleaning",

    "Feature Engineering",

    "Exploratory Data Analysis",

    "Business Insights",

    "Machine Learning",

    "Dashboard Development",

    "Deployment"

]

for i, step in enumerate(workflow, start=1):

    st.write(f"{i}. {step}")

st.divider()

# ---------------------------------------------------------
# Folder Structure
# ---------------------------------------------------------

st.header("Project Structure")

st.code("""
Market_Trend_Analyzer/

│── app.py

│── assets/

│── data/

│── models/

│── notebooks/

│── pages/

│── utils/

│── requirements.txt

└── README.md
""")

st.divider()

# ---------------------------------------------------------
# Future Enhancements
# ---------------------------------------------------------

st.header("Future Enhancements")

future = [

    "Sales Forecasting",

    "Customer Segmentation",

    "Inventory Analytics",

    "Geographical Mapping",

    "Real-time Database Integration",

    "Role-based Login System"

]

for item in future:

    st.write(f"• {item}")

st.divider()

# ---------------------------------------------------------
# Developer
# ---------------------------------------------------------

st.header("Developer")

st.write("**Project:** Market Trend Analyzer")

st.write("**Purpose:** Data Analytics Internship Project")

st.write("**Framework:** Streamlit")

st.write("**Programming Language:** Python")

st.divider()

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.caption(
    "Market Trend Analyzer | Version 1.0"
)
