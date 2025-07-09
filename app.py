
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the concept of Earnings Per Share (EPS) and how different financial instruments can dilute it. Understanding EPS is crucial for investors and analysts to assess a company's profitability on a per-share basis.

We will cover:
- **Basic EPS**: The earnings available to common shareholders divided by the weighted average shares outstanding.
- **Diluted EPS**: The earnings available to common shareholders divided by the weighted average shares outstanding, assuming all dilutive securities (e.g., convertible preferred stock, convertible debt, stock options) are converted into common stock.

The application allows you to manipulate key financial inputs and observe the real-time impact on EPS and its components through dynamic visualizations.

**Formulae:**

- **Basic EPS:**
  $$\text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}}$$
- **Diluted EPS (Preferred):**
  $$\text{Diluted EPS (Preferred)} = \frac{\text{Net Income} + \text{Preferred Dividends (re-added)}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}}$$
- **Diluted EPS (Debt):**
  $$\text{Diluted EPS (Debt)} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}}$$
  where $\text{After-Tax Interest Savings} = \text{Interest Expense} \times (1 - \text{Tax Rate})$ and $\text{Interest Expense} = \text{Face Value} \times \text{Coupon Rate}$.
- **Diluted EPS (Options):**
  $$\text{Diluted EPS (Options)} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}}$$
  where $\text{Incremental Shares} = \text{Shares from Option Exercise} - \text{Shares Repurchased}$.
  $\text{Proceeds from Option Exercise} = \text{Number of Options} \times \text{Exercise Price}$.
  $\text{Shares Repurchased} = \frac{\text{Proceeds from Option Exercise}}{\text{Average Market Price}}$.
""")
# Your code starts here
# No pages for now, will add the entire code in the main file.
from application import run_application
run_application()
# Your code ends
st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
            "Any reproduction of this demonstration "
            "requires prior written consent from QuantUniversity. "
            "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
