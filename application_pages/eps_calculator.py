
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_synthetic_data():
    """Generates synthetic financial data for EPS calculations."""
    data = {
        'Net Income': np.random.randint(1000000, 10000000),
        'Preferred Dividends': np.random.randint(0, 100000),
        'Weighted Average Shares Outstanding': np.random.randint(100000, 1000000),
        'Tax Rate': np.random.uniform(0.2, 0.4),
        'Convertible Preferred Stock Count': np.random.randint(0, 10000),
        'Convertible Preferred Conversion Ratio': np.random.uniform(0.5, 2),
        'Convertible Preferred Dividend Per Share': np.random.uniform(0.1, 1),
        'Convertible Debt Face Value': np.random.randint(0, 1000000),
        'Convertible Debt Coupon Rate': np.random.uniform(0.05, 0.1),
        'Convertible Debt Conversion Ratio (Shares per $1000)': np.random.randint(20, 50),
        'Stock Option Count': np.random.randint(0, 50000),
        'Stock Option Exercise Price': np.random.uniform(5, 20),
        'Average Market Price': np.random.uniform(10, 30)
    }
    return data

def orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp):
    """Calculates Basic and Diluted EPS."""

    if was <= 0: # Handle zero or negative shares outstanding for basic EPS
        basic_eps = 0.0
    else:
        basic_eps = (ni - pd) / was

    diluted_eps = basic_eps # Initialize diluted_eps with basic_eps for antidilution check

    # Convertible Preferred Stock
    if cps_c > 0 and (was + cps_c * cps_cr) > 0: # Ensure non-zero denominator
        # Add back preferred dividends to net income
        diluted_eps_cps = (ni + pd) / (was + cps_c * cps_cr)
        # Apply antidilution test: only if it's dilutive, update diluted_eps
        if diluted_eps_cps < diluted_eps:
            diluted_eps = diluted_eps_cps

    # Convertible Debt
    if cd_fv > 0:
        interest_expense = cd_fv * cd_cr
        after_tax_interest_savings = interest_expense * (1 - tr)
        if (was + (cd_fv / 1000) * cd_cr1000) > 0: # Ensure non-zero denominator
            diluted_eps_cd = (ni + after_tax_interest_savings - pd) / (was + (cd_fv / 1000) * cd_cr1000)
            # Apply antidilution test
            if diluted_eps_cd < diluted_eps:
                diluted_eps = diluted_eps_cd

    # Stock Options
    if so_c > 0 and amp > so_ep: # Options are dilutive only if market price > exercise price
        proceeds_from_exercise = so_c * so_ep
        shares_repurchased = proceeds_from_exercise / amp
        incremental_shares = so_c - shares_repurchased
        if (was + incremental_shares) > 0: # Ensure non-zero denominator
            diluted_eps_so = (ni - pd) / (was + incremental_shares)
            # Apply antidilution test
            if diluted_eps_so < diluted_eps:
                diluted_eps = diluted_eps_so
    elif so_c > 0 and amp <= so_ep: # Options are antidilutive or at the money, do not include
        pass # diluted_eps remains basic_eps or from other dilutive securities


    # Final check: Diluted EPS should never be greater than Basic EPS
    if diluted_eps > basic_eps:
        diluted_eps = basic_eps

    return basic_eps, diluted_eps

def display_eps_and_plot(basic_eps, diluted_eps):
    """Displays calculated EPS values and a Plotly bar chart."""
    st.markdown(f"**Calculated Basic EPS: `${basic_eps:.2f}`**")
    st.markdown(f"**Calculated Diluted EPS: `${diluted_eps:.2f}`**")

    # Plotly Visualization
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Basic EPS", "Diluted EPS"))
    fig.add_trace(go.Bar(y=[basic_eps], name="Basic EPS", marker_color='blue'), row=1, col=1)
    fig.add_trace(go.Bar(y=[diluted_eps], name="Diluted EPS", marker_color='red'), row=1, col=2)
    
    # Apply color-blind-friendly palette and font size (Streamlit defaults often handle this well,
    # but explicit colors are good for clarity)
    fig.update_layout(
        height=400,
        width=800,
        title_text="Basic vs Diluted EPS Comparison",
        font=dict(size=14), # Font size >= 12 pt
        showlegend=True,
        xaxis_title_text="EPS Type",
        yaxis_title_text="EPS Value ($)"
    )
    fig.update_yaxes(rangemode="tozero") # Ensure y-axis starts at zero

    st.plotly_chart(fig, use_container_width=True)

def run_eps_calculator():
    st.header("EPS Calculator")

    # Generate synthetic data for initial values
    synthetic_data = generate_synthetic_data()

    # Input widgets
    ni = st.sidebar.number_input("Net Income", value=synthetic_data['Net Income'], help="The company's total earnings after all expenses, interest, and taxes.")
    pd = st.sidebar.number_input("Preferred Dividends", value=synthetic_data['Preferred Dividends'], help="Dividends paid to preferred shareholders are subtracted because EPS only pertains to common shareholders.")
    was = st.sidebar.number_input("Weighted Average Shares Outstanding", value=synthetic_data['Weighted Average Shares Outstanding'], help="The number of shares outstanding over a reporting period, weighted by the portion of the period they were outstanding.")
    tr = st.sidebar.slider("Tax Rate", min_value=0.2, max_value=0.4, value=synthetic_data['Tax Rate'], step=0.01, help="Corporate tax rate.")
    cps_c = st.sidebar.number_input("Convertible Preferred Stock Count", value=synthetic_data['Convertible Preferred Stock Count'], help="Number of convertible preferred shares outstanding.")
    cps_cr = st.sidebar.number_input("Convertible Preferred Conversion Ratio", value=synthetic_data['Convertible Preferred Conversion Ratio'], step=0.1, help="Number of common shares each preferred share converts into.")
    cps_dps = st.sidebar.number_input("Convertible Preferred Dividend Per Share", value=synthetic_data['Convertible Preferred Dividend Per Share'], step=0.01, help="Dividend paid per convertible preferred share.")
    cd_fv = st.sidebar.number_input("Convertible Debt Face Value", value=synthetic_data['Convertible Debt Face Value'], help="Total face value of convertible debt outstanding.")
    cd_cr = st.sidebar.slider("Convertible Debt Coupon Rate", min_value=0.05, max_value=0.1, value=synthetic_data['Convertible Debt Coupon Rate'], step=0.001, help="Interest rate paid on convertible debt.")
    cd_cr1000 = st.sidebar.number_input("Convertible Debt Conversion Ratio (Shares per $1000)", value=synthetic_data['Convertible Debt Conversion Ratio (Shares per $1000)'], help="Number of common shares each $1000 of debt converts into.")
    so_c = st.sidebar.number_input("Stock Option Count", value=synthetic_data['Stock Option Count'], help="Number of outstanding stock options.")
    so_ep = st.sidebar.number_input("Stock Option Exercise Price", value=synthetic_data['Stock Option Exercise Price'], step=0.1, help="Price at which stock options can be exercised.")
    amp = st.sidebar.number_input("Average Market Price", value=synthetic_data['Average Market Price'], step=0.1, help="Average market price of the company's stock.")

    # EPS Calculation
    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)

    # Display results and plot
    display_eps_and_plot(basic_eps, diluted_eps)

