
import streamlit as st
st.set_page_config(page_title="EPS Calculator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("EPS Calculator")
st.divider()
st.markdown("""
In this lab, we will explore the concept of Earnings Per Share (EPS) and its diluted counterpart. EPS is a crucial financial metric that indicates a company's profitability on a per-share basis. Understanding the impact of potential dilution from convertible securities and stock options is vital for investors and financial analysts.

**Basic EPS** represents the earnings available to common shareholders relative to the weighted average number of common shares outstanding during the reporting period.

**Diluted EPS** takes into account the potential dilution that could occur if dilutive securities, such as convertible preferred stock, convertible debt, and stock options, were exercised or converted into common stock. The goal of diluted EPS is to provide a more conservative view of earnings per share by reflecting the potential decrease in EPS if these dilutive securities were converted.

This application provides an interactive platform to calculate and compare Basic EPS and Diluted EPS. You can dynamically input key financial data and observe the immediate impact of various potentially dilutive securities on EPS calculations.

### Key Formulas:

**Basic EPS Formula:**
$\\text{Basic EPS} = \\frac{\\text{Net Income} - \\text{Preferred Dividends}}{\\text{Weighted Average Shares Outstanding}}$

**Diluted EPS with Convertible Preferred Stock (If-Converted Method):**
$\\text{Diluted EPS (Preferred)} = \\frac{\\text{Net Income} + \\text{Preferred Dividends (re-added)}}{\\text{Weighted Average Shares Outstanding} + \\text{Shares from Conversion}}$

**Diluted EPS with Convertible Debt (If-Converted Method):**
$\\text{Diluted EPS (Debt)} = \\frac{\\text{Net Income} + \\text{After-Tax Interest Savings} - \\text{Preferred Dividends}}{\\text{Weighted Average Shares Outstanding} + \\text{Shares from Conversion}}$

**Diluted EPS with Stock Options (Treasury Stock Method):**
$\\text{Diluted EPS (Options)} = \\frac{\\text{Net Income} - \\text{Preferred Dividends}}{\\text{Weighted Average Shares Outstanding} + \\text{Incremental Shares}}$

where:
$\\text{Incremental Shares} = \\text{Shares from Option Exercise} - \\text{Shares Repurchased}$
$\\text{Shares Repurchased} = \\frac{\\text{Proceeds from Option Exercise}}{\\text{Average Market Price}}$
$\\text{Proceeds from Option Exercise} = \\text{Number of Options} \\times \\text{Exercise Price}$
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
