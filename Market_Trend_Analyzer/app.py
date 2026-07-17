"""
=========================================================
Market Trend Analyzer
Main Application
=========================================================
"""

import streamlit as st
from pathlib import Path

# ------------------------------------------------------
# Page Configuration
# ------------------------------------------------------

st.set_page_config(
    page_title="Market Trend Analyzer",
    page_icon="Market_Trend_Analyzer/assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------
# Load Custom CSS
# ------------------------------------------------------

css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------------------------------------------
# Sidebar
# ------------------------------------------------------

st.sidebar.image("Market_Trend_Analyzer/assets/logo.png", width=180)

st.sidebar.markdown(
    "<h2 style='text-align:center;'>Market Trend Analyzer</h2>",
    unsafe_allow_html=True
)
"""Navigate using the pages listed below.

• Home

• Sales Analysis

• Product Analysis

• Regional Analysis

• Sales Prediction

• Business Insights

• About
"""
)

st.sidebar.markdown("---")

st.sidebar.caption("Version 1.0")

# ------------------------------------------------------
# Main Header
# ------------------------------------------------------

st.markdown(
"""
<div class="dashboard-title">
Market Trend Analyzer
</div>

<div class="dashboard-subtitle">
Business Intelligence Dashboard using Streamlit and Machine Learning
</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ------------------------------------------------------
# Welcome Section
# ------------------------------------------------------

left, right = st.columns([2,1])

with left:

    st.markdown("## Welcome")

    st.write(
    """
    This dashboard provides interactive business analytics
    and sales forecasting using the Superstore dataset.

    The dashboard helps analyze:

    - Sales Performance
    - Product Performance
    - Regional Performance
    - Business Insights
    - Sales Prediction
    """
    )

with right:

    st.metric(
        label="Dashboard",
        value="Ready"
    )

# ------------------------------------------------------
# Dashboard Features
# ------------------------------------------------------

st.markdown("## Dashboard Modules")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
    """
    ### Sales Analysis

    Analyze sales trends over time,
    monthly growth,
    discounts,
    and revenue.
    """
    )

with c2:

    st.markdown(
    """
    ### Product Analysis

    Identify top-performing products,
    categories,
    and customer demand.
    """
    )

with c3:

    st.markdown(
    """
    ### Business Insights

    Discover KPIs,
    recommendations,
    and overall market performance.
    """
    )

st.markdown("---")

# ------------------------------------------------------
# Footer
# ------------------------------------------------------

st.markdown(
"""
<div class="footer">

Market Trend Analyzer | Data Analytics Internship Project

</div>
""",
unsafe_allow_html=True
)
