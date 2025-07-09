
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def calculate_basic_eps(net_income, preferred_dividends, waso):
    if waso == 0:
        st.error("Weighted Average Shares Outstanding cannot be zero.")
        return None
    return (net_income - preferred_dividends) / waso

def calculate_diluted_eps(net_income, preferred_dividends, waso, convertible_preferred_data, convertible_debt_data, stock_options_data):
    diluted_waso = waso
    diluted_net_income = net_income - preferred_dividends

    #Handle Convertible Preferred Stock
    if convertible_preferred_data['include']:
      additional_shares = convertible_preferred_data['count'] * convertible_preferred_data['conversion_ratio']
      diluted_waso += additional_shares
      diluted_net_income += convertible_preferred_data['dividend_per_share'] * convertible_preferred_data['count']


    #Handle Convertible Debt
    if convertible_debt_data['include']:
        after_tax_interest_savings = convertible_debt_data['face_value'] * convertible_debt_data['coupon_rate'] * (1 - 0.3) #assuming tax rate 30%
        diluted_net_income += after_tax_interest_savings
        additional_shares = convertible_debt_data['face_value'] / 1000 * convertible_debt_data['conversion_ratio']
        diluted_waso += additional_shares

    #Handle Stock Options
    if stock_options_data['include']:
        if stock_options_data['average_market_price'] == 0:
            st.error("Average Market Price cannot be zero when including Stock Options.")
            return None
        proceeds_from_exercise = stock_options_data['count'] * stock_options_data['exercise_price']
        shares_repurchased = proceeds_from_exercise / stock_options_data['average_market_price']
        incremental_shares = stock_options_data['count'] - shares_repurchased
        diluted_waso += incremental_shares

    if diluted_waso ==0:
        st.error("Diluted Weighted Average Shares Outstanding cannot be zero.")
        return None

    diluted_eps = diluted_net_income / diluted_waso
    return diluted_eps

def run_eps_calculator():
    st.header("EPS Calculator")

    # Input parameters
    net_income = st.number_input("Net Income", value=1000000.0, step=10000.0)
    preferred_dividends = st.number_input("Preferred Dividends", value=0.0, step=1000.0)
    waso = st.number_input("Weighted Average Shares Outstanding", value=100000.0, step=1000.0)


    convertible_preferred_data = {
        'include': st.checkbox("Include Convertible Preferred Stock"),
        'count': st.number_input("Convertible Preferred Stock Count", value=0, disabled=not convertible_preferred_data['include']),
        'conversion_ratio': st.number_input("Convertible Preferred Conversion Ratio", value=1.0, disabled=not convertible_preferred_data['include']),
        'dividend_per_share': st.number_input("Convertible Preferred Dividend Per Share", value=0.0, disabled=not convertible_preferred_data['include'])
    }

    convertible_debt_data = {
        'include': st.checkbox("Include Convertible Debt"),
        'face_value': st.number_input("Convertible Debt Face Value", value=0.0, disabled=not convertible_debt_data['include']),
        'coupon_rate': st.number_input("Convertible Debt Coupon Rate (Decimal)", value=0.0, disabled=not convertible_debt_data['include'], format="%.2f"),
        'conversion_ratio': st.number_input("Convertible Debt Conversion Ratio (Shares per $1000)", value=0.0, disabled=not convertible_debt_data['include'])
    }


    stock_options_data = {
        'include': st.checkbox("Include Stock Options"),
        'count': st.number_input("Stock Option Count", value=0, disabled=not stock_options_data['include']),
        'exercise_price': st.number_input("Stock Option Exercise Price", value=0.0, disabled=not stock_options_data['include']),
        'average_market_price': st.number_input("Average Market Price", value=0.0, disabled=not stock_options_data['include'])
    }


    # Calculations
    basic_eps = calculate_basic_eps(net_income, preferred_dividends, waso)
    diluted_eps = calculate_diluted_eps(net_income, preferred_dividends, waso, convertible_preferred_data, convertible_debt_data, stock_options_data)

    # Output
    st.subheader("Results")
    if basic_eps is not None:
        st.metric("Basic EPS", value=f"${basic_eps:.2f}")
    if diluted_eps is not None:
        st.metric("Diluted EPS", value=f"${diluted_eps:.2f}")

