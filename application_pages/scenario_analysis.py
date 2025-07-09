
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def run_scenario_analysis():
    st.header("Scenario Analysis")

    # Input Widgets
    net_income = st.number_input("Net Income", value=1000000.0, step=10000.0)
    preferred_dividends = st.number_input("Preferred Dividends", value=0.0, step=1000.0)
    waso = st.number_input("Weighted Average Shares Outstanding", value=1000000.0, step=10000.0)
    tax_rate = st.slider("Tax Rate", min_value=0.0, max_value=1.0, value=0.25, step=0.01)

    # Dilutive Securities Checkboxes
    include_convertible_preferred = st.checkbox("Include Convertible Preferred Stock")
    include_convertible_debt = st.checkbox("Include Convertible Debt")
    include_stock_options = st.checkbox("Include Stock Options")

    # Convertible Preferred Stock Inputs
    if include_convertible_preferred:
        convertible_preferred_count = st.number_input("Convertible Preferred Stock Count", value=10000.0, step=1000.0)
        convertible_preferred_conversion_ratio = st.number_input("Convertible Preferred Conversion Ratio", value=10.0, step=1.0)
        convertible_preferred_dividend_per_share = st.number_input("Convertible Preferred Dividend Per Share", value=1.0, step=0.1)

    # Convertible Debt Inputs
    if include_convertible_debt:
        convertible_debt_face_value = st.number_input("Convertible Debt Face Value", value=1000000.0, step=10000.0)
        convertible_debt_coupon_rate = st.slider("Convertible Debt Coupon Rate", min_value=0.0, max_value=0.2, value=0.05, step=0.01)
        convertible_debt_conversion_ratio = st.number_input("Convertible Debt Conversion Ratio (Shares per $1000)", value=50.0, step=1.0)

    # Stock Options Inputs
    if include_stock_options:
        stock_option_count = st.number_input("Stock Option Count", value=50000.0, step=1000.0)
        stock_option_exercise_price = st.number_input("Stock Option Exercise Price", value=20.0, step=1.0)
        average_market_price = st.number_input("Average Market Price", value=25.0, step=1.0)

    # Scenario Analysis Variable Selection
    scenario_variable = st.selectbox(
        "Select Variable for Scenario Analysis",
        options=[
            "Average Market Price (Stock Options)",
            "Convertible Preferred Conversion Ratio",
            "Convertible Debt Coupon Rate"
        ]
    )

    # Scenario Analysis Range Input
    if scenario_variable == "Average Market Price (Stock Options)":
        min_price = st.slider("Minimum Average Market Price", min_value=1.0, max_value=50.0, value=15.0, step=1.0)
        max_price = st.slider("Maximum Average Market Price", min_value=1.0, max_value=50.0, value=35.0, step=1.0)
        price_range = np.linspace(min_price, max_price, 50)  # Generate a range of prices

        diluted_eps_values = []
        for avg_price in price_range:
            diluted_eps = calculate_diluted_eps(net_income, preferred_dividends, waso, tax_rate,
                                                  include_convertible_preferred, convertible_preferred_count,
                                                  convertible_preferred_conversion_ratio, convertible_preferred_dividend_per_share,
                                                  include_convertible_debt, convertible_debt_face_value,
                                                  convertible_debt_coupon_rate, convertible_debt_conversion_ratio,
                                                  include_stock_options, stock_option_count, stock_option_exercise_price,
                                                  avg_price)
            diluted_eps_values.append(diluted_eps)

        # Create the plot
        fig = go.Figure(data=[go.Scatter(x=price_range, y=diluted_eps_values, mode='lines')])
        fig.update_layout(title='Impact of Average Market Price on Diluted EPS',
                          xaxis_title='Average Market Price ($)',
                          yaxis_title='Diluted EPS ($)')
        st.plotly_chart(fig)

    elif scenario_variable == "Convertible Preferred Conversion Ratio":
        min_ratio = st.slider("Minimum Conversion Ratio", min_value=1.0, max_value=20.0, value=5.0, step=1.0)
        max_ratio = st.slider("Maximum Conversion Ratio", min_value=1.0, max_value=20.0, value=15.0, step=1.0)
        ratio_range = np.linspace(min_ratio, max_ratio, 50)

        diluted_eps_values = []
        for conversion_ratio in ratio_range:
            diluted_eps = calculate_diluted_eps(net_income, preferred_dividends, waso, tax_rate,
                                                  include_convertible_preferred, convertible_preferred_count,
                                                  conversion_ratio, convertible_preferred_dividend_per_share,
                                                  include_convertible_debt, convertible_debt_face_value,
                                                  convertible_debt_coupon_rate, convertible_debt_conversion_ratio,
                                                  include_stock_options, stock_option_count, stock_option_exercise_price,
                                                  average_market_price)
            diluted_eps_values.append(diluted_eps)

        fig = go.Figure(data=[go.Scatter(x=ratio_range, y=diluted_eps_values, mode='lines')])
        fig.update_layout(title='Impact of Convertible Preferred Conversion Ratio on Diluted EPS',
                          xaxis_title='Conversion Ratio',
                          yaxis_title='Diluted EPS ($)')
        st.plotly_chart(fig)

    elif scenario_variable == "Convertible Debt Coupon Rate":
        min_rate = st.slider("Minimum Coupon Rate", min_value=0.0, max_value=0.2, value=0.01, step=0.01)
        max_rate = st.slider("Maximum Coupon Rate", min_value=0.0, max_value=0.2, value=0.1, step=0.01)
        rate_range = np.linspace(min_rate, max_rate, 50)

        diluted_eps_values = []
        for coupon_rate in rate_range:
            diluted_eps = calculate_diluted_eps(net_income, preferred_dividends, waso, tax_rate,
                                                  include_convertible_preferred, convertible_preferred_count,
                                                  convertible_preferred_conversion_ratio, convertible_preferred_dividend_per_share,
                                                  include_convertible_debt, convertible_debt_face_value,
                                                  coupon_rate, convertible_debt_conversion_ratio,
                                                  include_stock_options, stock_option_count, stock_option_exercise_price,
                                                  average_market_price)
            diluted_eps_values.append(diluted_eps)

        fig = go.Figure(data=[go.Scatter(x=rate_range, y=diluted_eps_values, mode='lines')])
        fig.update_layout(title='Impact of Convertible Debt Coupon Rate on Diluted EPS',
                          xaxis_title='Coupon Rate',
                          yaxis_title='Diluted EPS ($)')
        st.plotly_chart(fig)


def calculate_diluted_eps(net_income, preferred_dividends, waso, tax_rate,
                           include_convertible_preferred, convertible_preferred_count,
                           convertible_preferred_conversion_ratio, convertible_preferred_dividend_per_share,
                           include_convertible_debt, convertible_debt_face_value,
                           convertible_debt_coupon_rate, convertible_debt_conversion_ratio,
                           include_stock_options, stock_option_count, stock_option_exercise_price,
                           average_market_price):
    diluted_eps = (net_income - preferred_dividends) / waso if waso > 0 else 0

    # Convertible Preferred Stock Dilution
    if include_convertible_preferred:
        preferred_dividends_readded = convertible_preferred_count * convertible_preferred_dividend_per_share
        shares_from_preferred_conversion = convertible_preferred_count * convertible_preferred_conversion_ratio
        diluted_eps_preferred = (net_income + preferred_dividends_readded) / (waso + shares_from_preferred_conversion) if (waso + shares_from_preferred_conversion) > 0 else 0

        if diluted_eps_preferred < diluted_eps:
            diluted_eps = diluted_eps_preferred

    # Convertible Debt Dilution
    if include_convertible_debt:
        interest_savings = convertible_debt_face_value * convertible_debt_coupon_rate
        after_tax_interest_savings = interest_savings * (1 - tax_rate)
        shares_from_debt_conversion = (convertible_debt_face_value / 1000) * convertible_debt_conversion_ratio
        diluted_eps_debt = (net_income + after_tax_interest_savings - preferred_dividends) / (waso + shares_from_debt_conversion) if (waso + shares_from_debt_conversion) > 0 else 0
        if diluted_eps_debt < diluted_eps:
            diluted_eps = diluted_eps_debt

    # Stock Options Dilution
    if include_stock_options:
        if average_market_price > stock_option_exercise_price:
            proceeds_from_exercise = stock_option_count * stock_option_exercise_price
            shares_repurchased = proceeds_from_exercise / average_market_price
            incremental_shares = stock_option_count - shares_repurchased
            diluted_eps_options = (net_income - preferred_dividends) / (waso + incremental_shares) if (waso + incremental_shares) > 0 else 0
            if diluted_eps_options < diluted_eps:
                diluted_eps = diluted_eps_options

    return diluted_eps
