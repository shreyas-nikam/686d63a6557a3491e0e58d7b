
import streamlit as st

st.set_page_config(page_title="EPS Calculator & Dilution Impact", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("EPS Calculator & Dilution Impact")
st.divider()
st.markdown("""
In this lab, we explore the impact of potential dilution on a company's Earnings Per Share (EPS).
We will examine how different types of convertible securities, such as convertible preferred stock, convertible debt, and stock options,
can affect the EPS calculation. The application provides an interactive platform to dynamically input financial data
and visualize the immediate impact of these securities on both Basic and Diluted EPS.

**Key Concepts:**

*   **Basic EPS:** Represents the earnings available to each share of common stock outstanding.
    $$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$
*   **Diluted EPS:** Reflects the potential dilution of EPS that could occur if dilutive securities were converted into common stock.

**Dilutive Securities:**

*   **Convertible Preferred Stock:** Preferred stock that can be converted into common stock.
    The **if-converted method** assumes that the preferred stock is converted at the beginning of the period.
    $$ \text{Diluted EPS (Preferred)} = \frac{\text{Net Income} + \text{Preferred Dividends (re-added)}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$
*   **Convertible Debt:** Debt that can be converted into common stock.
    The **if-converted method** assumes that the debt is converted at the beginning of the period.
    $$ \text{Diluted EPS (Debt)} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$
*   **Stock Options:** Options that allow the holder to purchase common stock at a specified price.
    The **treasury stock method** assumes that the option holders exercise their options and the company uses the proceeds
    to repurchase shares of its own stock at the average market price.
    $$ \text{Diluted EPS (Options)} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}} $$
    where:
    $$ \text{Incremental Shares} = \text{Shares from Option Exercise} - \text{Shares Repurchased} $$
    $$ \text{Shares Repurchased} = \frac{\text{Proceeds from Option Exercise}}{\text{Average Market Price}} $$
    $$ \text{Proceeds from Option Exercise} = \text{Number of Options} \times \text{Exercise Price} $$

**How to Use This Application:**

1.  Enter the core financial data, including Net Income, Preferred Dividends, Weighted Average Shares Outstanding, and Tax Rate.
2.  Select the types of dilutive securities to include in the calculation.
3.  Enter the relevant data for each selected dilutive security, such as conversion ratios, coupon rates, and exercise prices.
4.  Observe the calculated Basic EPS and Diluted EPS values.
5.  Analyze the impact of each dilutive security on the Diluted EPS.
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
