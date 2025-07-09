
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the concepts of **Basic Earnings Per Share (EPS)** and **Diluted Earnings Per Share (EPS)**.
Understanding EPS is crucial for financial analysis as it indicates the portion of a company's profit allocated to each outstanding share of common stock. Diluted EPS, in particular, provides a more conservative view by considering the potential dilution from convertible securities, such as stock options, convertible preferred stock, and convertible debt.

This interactive application allows you to:
- Input key financial metrics and parameters related to potentially dilutive securities.
- See real-time calculations of Basic and Diluted EPS.
- Visualize the impact of potential dilution on a company's earnings per share.
- Understand the formulas and methodologies, including the anti-dilution test.

**Basic EPS** represents the earnings available to common shareholders divided by the weighted average number of common shares outstanding.

$$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$

**Diluted EPS** adjusts Basic EPS for the impact of all dilutive potential common shares outstanding during the period. This includes shares that would be issued upon the conversion of convertible bonds, convertible preferred stock, and the exercise of stock options or warrants.

The application uses the following methods for calculating the dilutive impact:
- **If-Converted Method** for Convertible Preferred Stock and Convertible Debt: Assumes these securities are converted into common stock at the beginning of the period (or date of issuance, if later), and adjusts net income for any related interest or preferred dividend savings.
- **Treasury Stock Method** for Stock Options: Assumes the exercise of options and the use of the proceeds to repurchase common stock at the average market price. Only the net increase in shares is considered dilutive.

An important concept is **anti-dilution**: a security is anti-dilutive if its conversion or exercise would increase earnings per share or decrease loss per share. Anti-dilutive securities are excluded from the calculation of Diluted EPS. Diluted EPS should never be higher than Basic EPS.
""")
# Your code starts here
from application_pages.eps_calculator import run_eps_calculator
run_eps_calculator()
# Your code ends
st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
            "Any reproduction of this demonstration "
            "requires prior written consent from QuantUniversity. "
            "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
