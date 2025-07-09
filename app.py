
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the concept of Earnings Per Share (EPS) and its diluted counterpart. EPS is a critical financial metric that indicates a company's profitability on a per-share basis, providing valuable insights for investors and stakeholders.

**Key Concepts Covered:**
*   **Basic EPS**: The fundamental measure of earnings available to each share of common stock.
*   **Diluted EPS**: A more conservative measure that considers the potential dilution from convertible securities, stock options, and warrants.
*   **Anti-Dilution**: The principle of excluding securities that would increase EPS if included in the diluted EPS calculation.

**Formulae:**

*   **Basic EPS**:
    $$\text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}}$$

*   **Diluted EPS (General)**:
    $$\text{Diluted EPS} = \frac{\text{Adjusted Net Income}}{\text{Adjusted Weighted Average Shares Outstanding}}$$

The application allows interactive input of financial data relevant to EPS calculation, accurate calculation of Basic and Diluted EPS based on user-defined parameters and visually compare Basic and Diluted EPS, providing clear insights into the dilution effect.
""")
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["EPS Calculator"])
if page == "EPS Calculator":
    from application_pages.eps_calculator import run_eps_calculator
    run_eps_calculator()
# Your code ends
st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
            "Any reproduction of this demonstration "
            "requires prior written consent from QuantUniversity. "
            "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
