
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def calculate_basic_eps(net_income, preferred_dividends, waso):
    if waso == 0:
        st.error("Weighted Average Shares Outstanding cannot be zero.")
        return None
    return (net_income - preferred_dividends) / waso

def calculate_diluted_eps(net_income, preferred_dividends, waso, tax_rate, convertible_preferred_data, convertible_debt_data, stock_options_data):
    diluted_waso = waso
    diluted_net_income = net_income - preferred_dividends

    # Handle Convertible Preferred Stock (If-Converted Method)
    if convertible_preferred_data['include'] and convertible_preferred_data['conversion_ratio'] > 0:
        additional_shares_pref = convertible_preferred_data['count'] * convertible_preferred_data['conversion_ratio']
        # Only include if dilutive
        eps_test_pref = (diluted_net_income + convertible_preferred_data['dividend_per_share'] * convertible_preferred_data['count']) / (diluted_waso + additional_shares_pref)
        if eps_test_pref < (diluted_net_income / diluted_waso): # Simple check for dilutive effect on this security alone
            diluted_waso += additional_shares_pref
            diluted_net_income += convertible_preferred_data['dividend_per_share'] * convertible_preferred_data['count']
        else:
            st.info(f"Convertible Preferred Stock is antidilutive and excluded.")

    # Handle Convertible Debt (If-Converted Method)
    if convertible_debt_data['include'] and convertible_debt_data['conversion_ratio'] > 0:
        after_tax_interest_savings = convertible_debt_data['face_value'] * convertible_debt_data['coupon_rate'] * (1 - tax_rate)
        additional_shares_debt = (convertible_debt_data['face_value'] / 1000) * convertible_debt_data['conversion_ratio']
        # Only include if dilutive
        eps_test_debt = (diluted_net_income + after_tax_interest_savings) / (diluted_waso + additional_shares_debt)
        if eps_test_debt < (diluted_net_income / diluted_waso): # Simple check for dilutive effect on this security alone
            diluted_net_income += after_tax_interest_savings
            diluted_waso += additional_shares_debt
        else:
            st.info(f"Convertible Debt is antidilutive and excluded.")


    # Handle Stock Options (Treasury Stock Method)
    if stock_options_data['include'] and stock_options_data['average_market_price'] > 0 and stock_options_data['exercise_price'] > 0:
        if stock_options_data['average_market_price'] < stock_options_data['exercise_price']:
            st.info("Stock Options are antidilutive (exercise price > average market price) and excluded.")
        else:
            proceeds_from_exercise = stock_options_data['count'] * stock_options_data['exercise_price']
            shares_repurchased = proceeds_from_exercise / stock_options_data['average_market_price']
            incremental_shares_options = stock_options_data['count'] - shares_repurchased
            # Options are dilutive if incremental shares > 0. If average market price <= exercise price, incremental shares will be 0 or negative.
            if incremental_shares_options > 0:
                diluted_waso += incremental_shares_options
            else:
                st.info(f"Stock Options are antidilutive (no incremental shares) and excluded.")


    if diluted_waso <= 0:
        st.error("Diluted Weighted Average Shares Outstanding cannot be zero or negative.")
        return None

    return diluted_net_income / diluted_waso

def run_eps_calculator():
    st.header("EPS Calculator & Dilution Impact")

    with st.sidebar:
        st.subheader("Core Financial Data Inputs")
        net_income = st.number_input("Net Income ($)", value=1_000_000.0, step=10_000.0, min_value=0.0)
        preferred_dividends = st.number_input("Preferred Dividends ($)", value=0.0, step=1_000.0, min_value=0.0)
        waso = st.number_input("Weighted Average Shares Outstanding", value=100_000.0, step=1_000.0, min_value=1.0)
        tax_rate = st.slider("Tax Rate", min_value=0.0, max_value=1.0, value=0.25, step=0.01)
        st.info("Ensure the tax rate is entered as a decimal (e.g., 0.25 for 25%).")

        st.subheader("Potentially Dilutive Securities Inputs")

        # Convertible Preferred Stock
        include_preferred = st.checkbox("Include Convertible Preferred Stock")
        convertible_preferred_data = {'include': include_preferred}
        if include_preferred:
            convertible_preferred_data['count'] = st.number_input("Convertible Preferred Stock Count", value=1000, min_value=0)
            convertible_preferred_data['conversion_ratio'] = st.number_input("Convertible Preferred Conversion Ratio (Shares per preferred share)", value=10.0, min_value=0.0)
            convertible_preferred_data['dividend_per_share'] = st.number_input("Convertible Preferred Dividend Per Share ($)", value=5.0, min_value=0.0)
            st.info("Uses the 'If-Converted Method'. Shares are added to denominator, dividends re-added to numerator.")
        else:
            convertible_preferred_data.update({'count': 0, 'conversion_ratio': 0.0, 'dividend_per_share': 0.0})

        # Convertible Debt
        include_debt = st.checkbox("Include Convertible Debt")
        convertible_debt_data = {'include': include_debt}
        if include_debt:
            convertible_debt_data['face_value'] = st.number_input("Convertible Debt Face Value ($)", value=1_000_000.0, min_value=0.0)
            convertible_debt_data['coupon_rate'] = st.number_input("Convertible Debt Coupon Rate (Decimal)", value=0.05, format="%.2f", min_value=0.0, max_value=1.0)
            convertible_debt_data['conversion_ratio'] = st.number_input("Convertible Debt Conversion Ratio (Shares per $1000 face value)", value=20.0, min_value=0.0)
            st.info("Uses the 'If-Converted Method'. Shares are added to denominator, after-tax interest savings re-added to numerator.")
        else:
            convertible_debt_data.update({'face_value': 0.0, 'coupon_rate': 0.0, 'conversion_ratio': 0.0})

        # Stock Options
        include_options = st.checkbox("Include Stock Options")
        stock_options_data = {'include': include_options}
        if include_options:
            stock_options_data['count'] = st.number_input("Stock Option Count", value=10_000, min_value=0)
            stock_options_data['exercise_price'] = st.number_input("Stock Option Exercise Price ($)", value=30.0, min_value=0.0)
            stock_options_data['average_market_price'] = st.number_input("Average Market Price ($)", value=40.0, min_value=0.0)
            st.info("Uses the 'Treasury Stock Method'. Incremental shares are added to denominator.")
        else:
            stock_options_data.update({'count': 0, 'exercise_price': 0.0, 'average_market_price': 0.0})

    # Calculations
    basic_eps = calculate_basic_eps(net_income, preferred_dividends, waso)
    diluted_eps_calculated = calculate_diluted_eps(net_income, preferred_dividends, waso, tax_rate, convertible_preferred_data, convertible_debt_data, stock_options_data)

    # Antidilution Test
    diluted_eps_final = diluted_eps_calculated
    antidilution_warning = False
    if basic_eps is not None and diluted_eps_calculated is not None:
        if diluted_eps_calculated > basic_eps:
            diluted_eps_final = basic_eps
            antidilution_warning = True

    st.subheader("Current EPS Snapshot")
    col1, col2 = st.columns(2)
    with col1:
        if basic_eps is not None:
            st.metric("Basic EPS", value=f"${basic_eps:.2f}")
        else:
            st.metric("Basic EPS", value="N/A")
    with col2:
        if diluted_eps_final is not None:
            st.metric("Diluted EPS", value=f"${diluted_eps_final:.2f}")
            if antidilution_warning:
                st.warning("Diluted EPS > Basic EPS. Diluted EPS set to Basic EPS (Antidilution Rule).")
        else:
            st.metric("Diluted EPS", value="N/A")


    st.subheader("EPS Comparison")
    if basic_eps is not None and diluted_eps_final is not None:
        eps_data = pd.DataFrame({
            'EPS Type': ['Basic EPS', 'Diluted EPS'],
            'Value': [basic_eps, diluted_eps_final]
        })
        fig_bar = go.Figure(data=[
            go.Bar(name='EPS', x=eps_data['EPS Type'], y=eps_data['Value'],
                   marker_color=['#1f77b4', '#ff7f0e']) # Blue for Basic, Orange for Diluted
        ])
        fig_bar.update_layout(title_text="Basic vs. Diluted EPS Comparison",
                              yaxis_title="EPS ($)",
                              bargap=0.4,
                              font=dict(size=12))
        st.plotly_chart(fig_bar, use_container_width=True)
        st.download_button(
            label="Download EPS Comparison Chart as PNG",
            data=fig_bar.to_image(format="png"),
            file_name="eps_comparison.png",
            mime="image/png"
        )

    st.subheader("Scenario Analysis: Impact on Diluted EPS")
    st.markdown("Select a key variable to observe its impact on Diluted EPS across a range, while other inputs remain constant.")

    scenario_variable_options = {
        "None": None,
        "Average Market Price (for Options)": "average_market_price",
        "Convertible Preferred Conversion Ratio": "preferred_conversion_ratio",
        "Convertible Debt Coupon Rate": "debt_coupon_rate"
    }

    selected_scenario_variable_key = st.selectbox("Select variable for scenario analysis:", list(scenario_variable_options.keys()))
    selected_scenario_variable = scenario_variable_options[selected_scenario_variable_key]

    if selected_scenario_variable:
        # Create a copy of current inputs to vary one
        scenario_net_income = net_income
        scenario_preferred_dividends = preferred_dividends
        scenario_waso = waso
        scenario_tax_rate = tax_rate
        scenario_convertible_preferred_data = convertible_preferred_data.copy()
        scenario_convertible_debt_data = convertible_debt_data.copy()
        scenario_stock_options_data = stock_options_data.copy()

        # Define range for the selected variable
        if selected_scenario_variable == "average_market_price":
            if not include_options:
                st.warning("Please enable 'Include Stock Options' to use this scenario analysis.")
            else:
                current_val = stock_options_data['average_market_price'] if stock_options_data['average_market_price'] > 0 else 1.0
                min_val = max(0.1, current_val * 0.5)
                max_val = current_val * 1.5
                range_vals = np.linspace(min_val, max_val, 50)
                st.markdown(f"Varying Average Market Price from ${min_val:.2f} to ${max_val:.2f}")

                diluted_eps_series = []
                for val in range_vals:
                    temp_stock_options_data = scenario_stock_options_data.copy()
                    temp_stock_options_data['average_market_price'] = val
                    eps = calculate_diluted_eps(scenario_net_income, scenario_preferred_dividends, scenario_waso, scenario_tax_rate,
                                                scenario_convertible_preferred_data, scenario_convertible_debt_data, temp_stock_options_data)
                    # Apply antidilution rule for scenario analysis as well
                    if eps is not None and basic_eps is not None and eps > basic_eps:
                        eps = basic_eps
                    diluted_eps_series.append(eps)

                fig_line = go.Figure(data=go.Scatter(x=range_vals, y=diluted_eps_series, mode='lines+markers', name='Diluted EPS'))
                fig_line.update_layout(title_text="Impact of Average Market Price on Diluted EPS",
                                       xaxis_title="Average Market Price ($)",
                                       yaxis_title="Diluted EPS ($)",
                                       font=dict(size=12))
                st.plotly_chart(fig_line, use_container_width=True)
                st.download_button(
                    label="Download Scenario Chart as PNG",
                    data=fig_line.to_image(format="png"),
                    file_name="scenario_market_price.png",
                    mime="image/png"
                )

        elif selected_scenario_variable == "preferred_conversion_ratio":
            if not include_preferred:
                st.warning("Please enable 'Include Convertible Preferred Stock' to use this scenario analysis.")
            else:
                current_val = convertible_preferred_data['conversion_ratio'] if convertible_preferred_data['conversion_ratio'] > 0 else 1.0
                min_val = max(0.1, current_val * 0.5)
                max_val = current_val * 1.5
                range_vals = np.linspace(min_val, max_val, 50)
                st.markdown(f"Varying Preferred Conversion Ratio from {min_val:.2f} to {max_val:.2f}")

                diluted_eps_series = []
                for val in range_vals:
                    temp_preferred_data = scenario_convertible_preferred_data.copy()
                    temp_preferred_data['conversion_ratio'] = val
                    eps = calculate_diluted_eps(scenario_net_income, scenario_preferred_dividends, scenario_waso, scenario_tax_rate,
                                                temp_preferred_data, scenario_convertible_debt_data, scenario_stock_options_data)
                    if eps is not None and basic_eps is not None and eps > basic_eps:
                        eps = basic_eps
                    diluted_eps_series.append(eps)

                fig_line = go.Figure(data=go.Scatter(x=range_vals, y=diluted_eps_series, mode='lines+markers', name='Diluted EPS'))
                fig_line.update_layout(title_text="Impact of Preferred Conversion Ratio on Diluted EPS",
                                       xaxis_title="Preferred Conversion Ratio",
                                       yaxis_title="Diluted EPS ($)",
                                       font=dict(size=12))
                st.plotly_chart(fig_line, use_container_width=True)
                st.download_button(
                    label="Download Scenario Chart as PNG",
                    data=fig_line.to_image(format="png"),
                    file_name="scenario_preferred_ratio.png",
                    mime="image/png"
                )

        elif selected_scenario_variable == "debt_coupon_rate":
            if not include_debt:
                st.warning("Please enable 'Include Convertible Debt' to use this scenario analysis.")
            else:
                current_val = convertible_debt_data['coupon_rate'] if convertible_debt_data['coupon_rate'] > 0 else 0.01
                min_val = max(0.0, current_val * 0.5)
                max_val = min(1.0, current_val * 1.5) # Coupon rate max 1.0 (100%)
                range_vals = np.linspace(min_val, max_val, 50)
                st.markdown(f"Varying Debt Coupon Rate from {min_val:.2f} to {max_val:.2f}")

                diluted_eps_series = []
                for val in range_vals:
                    temp_debt_data = scenario_convertible_debt_data.copy()
                    temp_debt_data['coupon_rate'] = val
                    eps = calculate_diluted_eps(scenario_net_income, scenario_preferred_dividends, scenario_waso, scenario_tax_rate,
                                                scenario_convertible_preferred_data, temp_debt_data, scenario_stock_options_data)
                    if eps is not None and basic_eps is not None and eps > basic_eps:
                        eps = basic_eps
                    diluted_eps_series.append(eps)

                fig_line = go.Figure(data=go.Scatter(x=range_vals, y=diluted_eps_series, mode='lines+markers', name='Diluted EPS'))
                fig_line.update_layout(title_text="Impact of Debt Coupon Rate on Diluted EPS",
                                       xaxis_title="Convertible Debt Coupon Rate",
                                       yaxis_title="Diluted EPS ($)",
                                       font=dict(size=12))
                st.plotly_chart(fig_line, use_container_width=True)
                st.download_button(
                    label="Download Scenario Chart as PNG",
                    data=fig_line.to_image(format="png"),
                    file_name="scenario_debt_coupon.png",
                    mime="image/png"
                )
        else:
            st.info("Select a variable above to see its impact on Diluted EPS.")


    st.subheader("Summary of Current Inputs")
    st.markdown("---")
    st.markdown(f"**Core Financials:**")
    st.markdown(f"- Net Income: ${net_income:,.2f}")
    st.markdown(f"- Preferred Dividends: ${preferred_dividends:,.2f}")
    st.markdown(f"- Weighted Average Shares Outstanding (WASO): {waso:,.0f}")
    st.markdown(f"- Tax Rate: {tax_rate:.2%}")
    st.markdown("---")

    if include_preferred:
        st.markdown(f"**Convertible Preferred Stock:**")
        st.markdown(f"- Count: {convertible_preferred_data['count']:,}")
        st.markdown(f"- Conversion Ratio: {convertible_preferred_data['conversion_ratio']:.2f} shares/preferred share")
        st.markdown(f"- Dividend Per Share: ${convertible_preferred_data['dividend_per_share']:.2f}")
        st.markdown("---")

    if include_debt:
        st.markdown(f"**Convertible Debt:**")
        st.markdown(f"- Face Value: ${convertible_debt_data['face_value']:,.2f}")
        st.markdown(f"- Coupon Rate: {convertible_debt_data['coupon_rate']:.2%}")
        st.markdown(f"- Conversion Ratio: {convertible_debt_data['conversion_ratio']:.2f} shares/$1000 face value")
        st.markdown("---")

    if include_options:
        st.markdown(f"**Stock Options:**")
        st.markdown(f"- Count: {stock_options_data['count']:,}")
        st.markdown(f"- Exercise Price: ${stock_options_data['exercise_price']:.2f}")
        st.markdown(f"- Average Market Price: ${stock_options_data['average_market_price']:.2f}")
        st.markdown("---")
