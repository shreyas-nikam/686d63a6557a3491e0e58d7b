
import streamlit as st

st.set_page_config(page_title="EPS Calculator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("EPS Calculator")
st.divider()
st.markdown("""
In this lab, we explore the intricacies of Earnings Per Share (EPS) calculations, focusing on the impact of potential dilution from convertible securities and stock options.
This interactive tool allows you to dynamically adjust financial inputs and immediately visualize their effects on both Basic and Diluted EPS.
We will cover the 'if-converted method' for convertible preferred stock and convertible debt, and the 'treasury stock method' for stock options and warrants.

**Key Concepts:**

*   **Basic EPS:** Earnings available to common shareholders divided by the weighted average number of common shares outstanding.
*   **Diluted EPS:** A more conservative measure that considers the potential dilution from securities that could increase the number of common shares outstanding.
*   **Antidilution:** Occurs when including a security in the diluted EPS calculation would *increase* EPS. In such cases, the security is excluded from the calculation.

**Formulas:**

**Basic EPS Formula:**
$$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$

**Diluted EPS with Convertible Preferred Stock (If-Converted Method):**
$$ \text{Diluted EPS (Preferred)} = \frac{\text{Net Income} + \text{Preferred Dividends (re-added)}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

**Diluted EPS with Convertible Debt (If-Converted Method):**
$$ \text{Diluted EPS (Debt)} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

**Diluted EPS with Stock Options (Treasury Stock Method):**
$$ \text{Diluted EPS (Options)} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}} $$
where:
$$ \text{Incremental Shares} = \text{Shares from Option Exercise} - \text{Shares Repurchased} $$
$$ \text{Shares Repurchased} = \frac{\text{Proceeds from Option Exercise}}{\text{Average Market Price}} $$
$$ \text{Proceeds from Option Exercise} = \text{Number of Options} \times \text{Exercise Price} $$
""")

page = st.sidebar.selectbox(label="Navigation", options=["EPS Calculator"])

if page == "EPS Calculator":
    from application_pages.eps_calculator import run_eps_calculator
    run_eps_calculator()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
