
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def run_eps_calculator():
    st.header("Earnings Per Share (EPS) Calculator")

    # --- Sidebar Inputs ---
    st.sidebar.header("Financial Data")
    net_income = st.sidebar.number_input("Net Income", value=1000000.0)
    preferred_dividends = st.sidebar.number_input("Preferred Dividends", value=100000.0)
    waso = st.sidebar.number_input("Weighted Average Shares Outstanding (WASO)", value=1000000.0)
    tax_rate = st.sidebar.slider("Tax Rate", min_value=0.0, max_value=1.0, value=0.25)

    st.sidebar.header("Potentially Dilutive Securities")

    # Convertible Preferred Stock
    include_preferred = st.sidebar.checkbox("Include Convertible Preferred Stock")
    if include_preferred:
        preferred_shares = st.sidebar.number_input("Convertible Preferred Stock Count", value=100000.0)
        preferred_conversion_ratio = st.sidebar.number_input("Convertible Preferred Conversion Ratio (Shares per Preferred Share)", value=1.0)
        preferred_dividend_per_share = st.sidebar.number_input("Convertible Preferred Dividend Per Share", value=1.0)
        total_preferred_dividends = preferred_shares * preferred_dividend_per_share

    # Convertible Debt
    include_debt = st.sidebar.checkbox("Include Convertible Debt")
    if include_debt:
        debt_face_value = st.sidebar.number_input("Convertible Debt Face Value", value=500000.0)
        debt_coupon_rate = st.sidebar.slider("Convertible Debt Coupon Rate", min_value=0.0, max_value=0.20, value=0.05)
        debt_conversion_ratio = st.sidebar.number_input("Convertible Debt Conversion Ratio (Shares per $1000)", value=20.0)
        interest_expense = debt_face_value * debt_coupon_rate
        after_tax_interest_savings = interest_expense * (1 - tax_rate)

    # Stock Options
    include_options = st.sidebar.checkbox("Include Stock Options")
    if include_options:
        option_count = st.sidebar.number_input("Stock Option Count", value=50000.0)
        option_exercise_price = st.sidebar.number_input("Stock Option Exercise Price", value=10.0)
        average_market_price = st.sidebar.number_input("Average Market Price", value=15.0)

    # --- Calculations ---
    basic_eps = (net_income - preferred_dividends) / waso

    diluted_eps = basic_eps  # Initialize with basic EPS

    # Convertible Preferred Stock Calculation
    if include_preferred:
        diluted_eps_preferred = (net_income + total_preferred_dividends) / (waso + (preferred_shares * preferred_conversion_ratio))
        if diluted_eps_preferred < diluted_eps:
            diluted_eps = diluted_eps_preferred

    # Convertible Debt Calculation
    if include_debt:
        diluted_eps_debt = (net_income + after_tax_interest_savings - preferred_dividends) / (waso + (debt_face_value / 1000 * debt_conversion_ratio))
        if diluted_eps_debt < diluted_eps:
            diluted_eps = diluted_eps_debt
    
    # Stock Options Calculation (Treasury Stock Method)
    if include_options:
        if average_market_price > option_exercise_price:
            proceeds = option_count * option_exercise_price
            shares_repurchased = proceeds / average_market_price
            incremental_shares = option_count - shares_repurchased
            diluted_eps_options = (net_income - preferred_dividends) / (waso + incremental_shares)
            if diluted_eps_options < diluted_eps:
                diluted_eps = diluted_eps_options

    # --- Output Display ---
    st.header("Current EPS Snapshot")
    st.write(f"Basic EPS: ${basic_eps:.2f}")
    st.write(f"Diluted EPS: ${diluted_eps:.2f}")

    if diluted_eps > basic_eps:
        st.warning("Diluted EPS is greater than Basic EPS. This indicates an anti-dilutive effect. Diluted EPS is set to Basic EPS.")
        diluted_eps = basic_eps

    # --- Summary of Inputs ---
    st.subheader("Summary of Inputs")
    input_data = {
        "Net Income": net_income,
        "Preferred Dividends": preferred_dividends,
        "WASO": waso,
        "Tax Rate": tax_rate,
    }

    if include_preferred:
        input_data["Preferred Shares"] = preferred_shares
        input_data["Conversion Ratio (Preferred)"] = preferred_conversion_ratio
        input_data["Dividend Per Share"] = preferred_dividend_per_share

    if include_debt:
        input_data["Debt Face Value"] = debt_face_value
        input_data["Debt Coupon Rate"] = debt_coupon_rate
        input_data["Conversion Ratio (Debt)"] = debt_conversion_ratio

    if include_options:
        input_data["Option Count"] = option_count
        input_data["Exercise Price"] = option_exercise_price
        input_data["Market Price"] = average_market_price

    input_df = pd.DataFrame(input_data, index=['Value']).T
    st.dataframe(input_df)

    # --- Visualizations ---
    st.header("EPS Comparison")
    fig = go.Figure(data=[
        go.Bar(name="Basic EPS", x=["EPS"], y=[basic_eps]),
        go.Bar(name="Diluted EPS", x=["EPS"], y=[diluted_eps]),
    ])
    st.plotly_chart(fig, use_container_width=True)

    # --- Scenario Analysis ---
    st.header("Scenario Analysis")
    scenario_variable = st.selectbox("Select a variable for scenario analysis:",
                                      options=["Average Market Price", "Convertible Preferred Conversion Ratio", "Convertible Debt Coupon Rate"])

    if scenario_variable == "Average Market Price" and include_options:
        min_price = st.slider("Minimum Average Market Price", min_value=1.0, max_value=average_market_price, value=average_market_price * 0.5)
        max_price = st.slider("Maximum Average Market Price", min_value=average_market_price, max_value=average_market_price * 2, value=average_market_price * 1.5)
        price_range = np.linspace(min_price, max_price, 50)
        diluted_eps_values = []
        for price in price_range:
            # Recalculate Diluted EPS with varying market price
            temp_diluted_eps = (net_income - preferred_dividends) / waso  # Initialize with basic EPS

            if include_preferred:
                temp_diluted_eps_preferred = (net_income + total_preferred_dividends) / (waso + (preferred_shares * preferred_conversion_ratio))
                if temp_diluted_eps_preferred < temp_diluted_eps:
                    temp_diluted_eps = temp_diluted_eps_preferred

            if include_debt:
                temp_diluted_eps_debt = (net_income + after_tax_interest_savings - preferred_dividends) / (waso + (debt_face_value / 1000 * debt_conversion_ratio))
                if temp_diluted_eps_debt < temp_diluted_eps:
                    temp_diluted_eps = temp_diluted_eps_debt

            if average_market_price > option_exercise_price:
                proceeds = option_count * option_exercise_price
                shares_repurchased = proceeds / price
                incremental_shares = option_count - shares_repurchased
                temp_diluted_eps_options = (net_income - preferred_dividends) / (waso + incremental_shares)
                if temp_diluted_eps_options < temp_diluted_eps:
                    temp_diluted_eps = temp_diluted_eps_options
            diluted_eps_values.append(temp_diluted_eps)

        fig_scenario = go.Figure(data=[go.Scatter(x=price_range, y=diluted_eps_values, mode='lines')])
        fig_scenario.update_layout(title="Impact of Average Market Price on Diluted EPS",
                                  xaxis_title="Average Market Price",
                                  yaxis_title="Diluted EPS")
        st.plotly_chart(fig_scenario, use_container_width=True)

    elif scenario_variable == "Convertible Preferred Conversion Ratio" and include_preferred:
        min_ratio = st.slider("Minimum Conversion Ratio", min_value=0.1, max_value=preferred_conversion_ratio, value=preferred_conversion_ratio * 0.5)
        max_ratio = st.slider("Maximum Conversion Ratio", min_value=preferred_conversion_ratio, max_value=preferred_conversion_ratio * 2, value=preferred_conversion_ratio * 1.5)
        ratio_range = np.linspace(min_ratio, max_ratio, 50)
        diluted_eps_values = []

        for ratio in ratio_range:
             # Recalculate Diluted EPS with varying conversion ratio
            temp_diluted_eps = (net_income - preferred_dividends) / waso  # Initialize with basic EPS

            temp_diluted_eps_preferred = (net_income + total_preferred_dividends) / (waso + (preferred_shares * ratio))
            if temp_diluted_eps_preferred < temp_diluted_eps:
                temp_diluted_eps = temp_diluted_eps_preferred

            if include_debt:
                temp_diluted_eps_debt = (net_income + after_tax_interest_savings - preferred_dividends) / (waso + (debt_face_value / 1000 * debt_conversion_ratio))
                if temp_diluted_eps_debt < temp_diluted_eps:
                    temp_diluted_eps = temp_diluted_eps_debt

            if include_options:
                if average_market_price > option_exercise_price:
                    proceeds = option_count * option_exercise_price
                    shares_repurchased = proceeds / average_market_price
                    incremental_shares = option_count - shares_repurchased
                    temp_diluted_eps_options = (net_income - preferred_dividends) / (waso + incremental_shares)
                    if temp_diluted_eps_options < temp_diluted_eps:
                        temp_diluted_eps = temp_diluted_eps_options

            diluted_eps_values.append(temp_diluted_eps)

        fig_scenario = go.Figure(data=[go.Scatter(x=ratio_range, y=diluted_eps_values, mode='lines')])
        fig_scenario.update_layout(title="Impact of Preferred Conversion Ratio on Diluted EPS",
                                  xaxis_title="Conversion Ratio",
                                  yaxis_title="Diluted EPS")
        st.plotly_chart(fig_scenario, use_container_width=True)

    elif scenario_variable == "Convertible Debt Coupon Rate" and include_debt:
        min_rate = st.slider("Minimum Coupon Rate", min_value=0.0, max_value=debt_coupon_rate, value=debt_coupon_rate * 0.5)
        max_rate = st.slider("Maximum Coupon Rate", min_value=debt_coupon_rate, max_value=0.20, value=debt_coupon_rate * 1.5)
        rate_range = np.linspace(min_rate, max_rate, 50)
        diluted_eps_values = []

        for rate in rate_range:
            # Recalculate Diluted EPS with varying coupon rate
            temp_diluted_eps = (net_income - preferred_dividends) / waso  # Initialize with basic EPS

            if include_preferred:
                temp_diluted_eps_preferred = (net_income + total_preferred_dividends) / (waso + (preferred_shares * preferred_conversion_ratio))
                if temp_diluted_eps_preferred < temp_diluted_eps:
                    temp_diluted_eps = temp_diluted_eps_preferred

            interest_expense = debt_face_value * rate
            after_tax_interest_savings = interest_expense * (1 - tax_rate)

            temp_diluted_eps_debt = (net_income + after_tax_interest_savings - preferred_dividends) / (waso + (debt_face_value / 1000 * debt_conversion_ratio))
            if temp_diluted_eps_debt < temp_diluted_eps:
                temp_diluted_eps = temp_diluted_eps_debt

            if include_options:
                if average_market_price > option_exercise_price:
                    proceeds = option_count * option_exercise_price
                    shares_repurchased = proceeds / average_market_price
                    incremental_shares = option_count - shares_repurchased
                    temp_diluted_eps_options = (net_income - preferred_dividends) / (waso + incremental_shares)
                    if temp_diluted_eps_options < temp_diluted_eps:
                        temp_diluted_eps = temp_diluted_eps_options
            diluted_eps_values.append(temp_diluted_eps)

        fig_scenario = go.Figure(data=[go.Scatter(x=rate_range, y=diluted_eps_values, mode='lines')])
        fig_scenario.update_layout(title="Impact of Debt Coupon Rate on Diluted EPS",
                                  xaxis_title="Coupon Rate",
                                  yaxis_title="Diluted EPS")
        st.plotly_chart(fig_scenario, use_container_width=True)
