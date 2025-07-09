
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the concept of Earnings Per Share (EPS) and the impact of potential dilution from various sources such as convertible securities and stock options.
We will use interactive visualizations and real-time calculations to understand how these factors can affect a company's EPS.

EPS is a key financial metric used to evaluate a company's profitability. Basic EPS considers only outstanding common shares, while Diluted EPS accounts for the potential dilution that could occur if convertible securities or stock options are exercised.

Understanding the difference between Basic and Diluted EPS is crucial for investors and analysts to accurately assess a company's earnings potential.
""")

page = st.sidebar.selectbox(label="Navigation", options=["EPS Calculator"])
if page == "EPS Calculator":
    from application_pages.page1 import run_page1
    run_page1()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
            "Any reproduction of this demonstration "
            "requires prior written consent from QuantUniversity. "
            "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
