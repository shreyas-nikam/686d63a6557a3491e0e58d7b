
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="EPS Calculator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("EPS Calculator")
st.divider()
st.markdown("""
### Understanding Earnings Per Share (EPS) and Dilution

This application helps you understand the concepts of Basic Earnings Per Share (EPS) and Diluted EPS. It allows you to explore how different financial instruments, such as convertible preferred stock, convertible debt, and stock options, can impact a company's EPS.

**Key Concepts:**

*   **Basic EPS:** Calculated by dividing net income available to common shareholders by the weighted average number of common shares outstanding.

    $$
    \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}}
    $$

*   **Diluted EPS:** A more conservative measure that considers the potential dilution of earnings if all convertible securities were exercised or converted into common stock.

*   **If-Converted Method:** Used for convertible preferred stock and convertible debt. It assumes that these securities were converted at the beginning of the period (or at the time of issuance, if later).

*   **Treasury Stock Method:** Used for stock options and warrants. It assumes that the proceeds from the exercise of these securities are used to repurchase shares of common stock at the average market price.

**How to Use This App:**

1.  Enter the core financial data, including net income, preferred dividends, weighted average shares outstanding, and tax rate.
2.  Use the checkboxes to include or exclude different types of dilutive securities (convertible preferred stock, convertible debt, and stock options).
3.  If you include a dilutive security, enter the relevant information, such as conversion ratios, coupon rates, and exercise prices.
4.  Observe how the Basic EPS and Diluted EPS change as you adjust the input parameters.
5.  Explore the scenario analysis to see how Diluted EPS changes as a function of a single selected continuous input variable.

**Important Considerations:**

*   A security is considered *antidilutive* if its inclusion in the diluted EPS calculation would result in a higher EPS. Antidilutive securities are excluded from the diluted EPS calculation.
*   This application is for educational purposes only and should not be used for making investment decisions.

""")

page = st.sidebar.selectbox(label="Navigation", options=["EPS Calculation", "Scenario Analysis"])

if page == "EPS Calculation":
    from application_pages.eps_calculation import run_eps_calculation
    run_eps_calculation()
elif page == "Scenario Analysis":
    from application_pages.scenario_analysis import run_scenario_analysis
    run_scenario_analysis()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
