
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def run_eps_calculation():
    st.header("EPS Calculation")

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

    # Calculations
    basic_eps = (net_income - preferred_dividends) / waso if waso > 0 else 0

    diluted_eps = basic_eps  # Initialize diluted_eps with basic_eps

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
        else:
            st.info("Stock options are anti-dilutive because the average market price is not greater than the exercise price.")


    # Antidilution Check
    if diluted_eps > basic_eps:
        diluted_eps = basic_eps
        st.warning("Diluted EPS is greater than Basic EPS.  Diluted EPS is set to Basic EPS.")

    # Display Results
    st.subheader("Calculated EPS Values")
    st.metric("Basic EPS", value=f"{basic_eps:.2f}")
    st.metric("Diluted EPS", value=f"{diluted_eps:.2f}")

    # Visualization
    labels = ['Basic EPS', 'Diluted EPS']
    values = [basic_eps, diluted_eps]

    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    fig.update_layout(title='Basic vs. Diluted EPS', yaxis_title='EPS ($)')
    st.plotly_chart(fig)

    # Summary of Inputs
    st.subheader("Summary of Inputs")
    input_data = {
        "Net Income": net_income,
        "Preferred Dividends": preferred_dividends,
        "Weighted Average Shares Outstanding": waso,
        "Tax Rate": tax_rate,
        "Include Convertible Preferred Stock": include_convertible_preferred,
        "Include Convertible Debt": include_convertible_debt,
        "Include Stock Options": include_stock_options
    }

    if include_convertible_preferred:
        input_data.update({
            "Convertible Preferred Stock Count": convertible_preferred_count,
            "Convertible Preferred Conversion Ratio": convertible_preferred_conversion_ratio,
            "Convertible Preferred Dividend Per Share": convertible_preferred_dividend_per_share
        })

    if include_convertible_debt:
        input_data.update({
            "Convertible Debt Face Value": convertible_debt_face_value,
            "Convertible Debt Coupon Rate": convertible_debt_coupon_rate,
            "Convertible Debt Conversion Ratio (Shares per $1000)": convertible_debt_conversion_ratio
        })

    if include_stock_options:
        input_data.update({
            "Stock Option Count": stock_option_count,
            "Stock Option Exercise Price": stock_option_exercise_price,
            "Average Market Price": average_market_price
        })

    input_df = pd.DataFrame.from_dict(input_data, orient='index', columns=['Value'])
    st.dataframe(input_df)
