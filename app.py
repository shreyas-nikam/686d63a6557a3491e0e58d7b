
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, you will learn about **Earnings Per Share (EPS) and the impact of dilution**. This application provides an interactive tool to calculate and visualize Basic and Diluted EPS, considering various potentially dilutive securities like convertible preferred stock, convertible debt, and stock options. Explore the financial implications by adjusting real-time inputs.
""")
page = st.sidebar.selectbox(label="Navigation", options=["EPS Calculator & Dilution Impact", "Page 2", "Page 3"])
if page == "EPS Calculator & Dilution Impact":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3":
    from application_pages.page3 import run_page3
    run_page3()
st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
            "Any reproduction of this demonstration "
            "requires prior written consent from QuantUniversity. "
            "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
