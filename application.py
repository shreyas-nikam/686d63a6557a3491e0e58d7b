
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_synthetic_data(num_records):
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
    synthetic_data = pd.Series(data)
    return synthetic_data

def orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp):
    """Calculates Basic and Diluted EPS."""

    basic_eps = (ni - pd) / was if was > 0 else 0.0 # Handle division by zero

    diluted_eps = basic_eps # Initialize diluted_eps with basic_eps for antidilution check

    # Convertible Preferred Stock
    if cps_c > 0 and (was + cps_c * cps_cr) > 0:
        diluted_eps_cps = (ni + pd) / (was + cps_c * cps_cr)
        if diluted_eps_cps < diluted_eps: # Apply antidilution test
            diluted_eps = diluted_eps_cps

    # Convertible Debt
    if cd_fv > 0:
        interest_expense = cd_fv * cd_cr
        after_tax_interest_savings = interest_expense * (1 - tr)
        denominator_cd = was + (cd_fv / 1000) * cd_cr1000
        if denominator_cd > 0:
            diluted_eps_cd = (ni + after_tax_interest_savings - pd) / denominator_cd
            if diluted_eps_cd < diluted_eps: # Apply antidilution test
                diluted_eps = diluted_eps_cd

    # Stock Options
    if so_c > 0 and amp > so_ep: # Options are dilutive only if market price > exercise price
        proceeds_from_exercise = so_c * so_ep
        shares_repurchased = proceeds_from_exercise / amp if amp > 0 else 0
        incremental_shares = so_c - shares_repurchased
        denominator_so = was + incremental_shares
        if denominator_so > 0:
            diluted_eps_so = (ni - pd) / denominator_so
            if diluted_eps_so < diluted_eps: # Apply antidilution test
                diluted_eps = diluted_eps_so
    # If options are antidilutive (amp <= so_ep), they are not included,
    # so diluted_eps remains as calculated from other dilutive securities or basic_eps.

    # Final check: Diluted EPS should never be greater than Basic EPS
    if diluted_eps > basic_eps:
        diluted_eps = basic_eps

    return basic_eps, diluted_eps

def update_eps_display(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp):
    """Calculates and displays EPS with visualizations."""
    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)

    st.metric(label="Basic EPS", value=f"{basic_eps:.2f}")
    st.metric(label="Diluted EPS", value=f"{diluted_eps:.2f}")

    fig = make_subplots(rows=1, cols=2, subplot_titles=("Basic EPS", "Diluted EPS"))
    # Using color-blind friendly colors as per requirement
    fig.add_trace(go.Bar(y=[basic_eps], name="Basic EPS", marker_color='#648FFF'), row=1, col=1) # Blue
    fig.add_trace(go.Bar(y=[diluted_eps], name="Diluted EPS", marker_color='#DC267F'), row=1, col=2) # Red

    # Ensure clear titles, labeled axes, and legends, font size >= 12 pt
    fig.update_layout(
        height=400,
        width=800,
        title_text="Basic vs. Diluted EPS Comparison",
        font=dict(size=12), # Minimum font size 12pt
        showlegend=True,
        bargap=0.2
    )
    fig.update_yaxes(title_text="EPS ($)", row=1, col=1)
    fig.update_yaxes(title_text="EPS ($)", row=1, col=2)
    fig.update_xaxes(showticklabels=False) # Hide x-axis labels if not meaningful

    st.plotly_chart(fig, use_container_width=True)


def run_application():
    """Main function to run the Streamlit application."""
    synthetic_data = generate_synthetic_data(1)

    # Sidebar inputs
    with st.sidebar:
        st.header("Financial Inputs")
        net_income = st.number_input("Net Income", min_value=0, step=1000, value=synthetic_data['Net Income'], help="The company's total earnings after all expenses, interest, and taxes.")
        preferred_dividends = st.number_input("Preferred Dividends", min_value=0, step=100, value=synthetic_data['Preferred Dividends'], help="Dividends paid to preferred shareholders, subtracted for Basic EPS and re-added for convertible preferred diluted EPS.")
        wa_shares_outstanding = st.number_input("Weighted Average Shares Outstanding", min_value=1, step=100, value=synthetic_data['Weighted Average Shares Outstanding'], help="The number of common shares outstanding over the reporting period, weighted by the portion of the period they were outstanding.")
        tax_rate = st.slider("Tax Rate", min_value=0.0, max_value=0.5, step=0.01, format="%.2f", value=synthetic_data['Tax Rate'], help="The company's effective tax rate, used for after-tax interest savings on convertible debt.")

        st.subheader("Convertible Preferred Stock")
        cps_count = st.number_input("Convertible Preferred Stock Count", min_value=0, step=10, value=int(synthetic_data['Convertible Preferred Stock Count']), help="Number of outstanding convertible preferred shares.")
        cps_conv_ratio = st.number_input("Convertible Preferred Conversion Ratio", min_value=0.0, step=0.1, value=synthetic_data['Convertible Preferred Conversion Ratio'], help="Number of common shares obtainable upon conversion of one preferred share.")
        cps_dps = synthetic_data['Convertible Preferred Dividend Per Share']

        st.subheader("Convertible Debt")
        cd_face_value = st.number_input("Convertible Debt Face Value", min_value=0, step=1000, value=int(synthetic_data['Convertible Debt Face Value']), help="Total face value of outstanding convertible debt.")
        cd_coupon_rate = st.slider("Convertible Debt Coupon Rate", min_value=0.0, max_value=0.2, step=0.001, format="%.3f", value=synthetic_data['Convertible Debt Coupon Rate'], help="Annual interest rate (coupon) on the convertible debt.")
        cd_cr1000 = st.number_input("Convertible Debt Conversion Ratio (Shares per $1000)", min_value=0, step=1, value=int(synthetic_data['Convertible Debt Conversion Ratio (Shares per $1000)']), help="Number of common shares obtainable for every $1000 face value of convertible debt upon conversion.")

        st.subheader("Stock Options")
        so_c = st.number_input("Stock Option Count", min_value=0, step=10, value=int(synthetic_data['Stock Option Count']), help="Number of outstanding stock options.")
        so_ep = st.number_input("Stock Option Exercise Price", min_value=0.0, step=0.1, value=synthetic_data['Stock Option Exercise Price'], help="The price at which common shares can be acquired upon exercising stock options.")
        avg_market_price = st.number_input("Average Market Price", min_value=0.0, step=0.1, value=synthetic_data['Average Market Price'], help="Average market price of the common stock during the period, used in the Treasury Stock Method.")

    # Main content area
    update_eps_display(net_income, preferred_dividends, wa_shares_outstanding, tax_rate,
                        cps_count, cps_conv_ratio, cps_dps, cd_face_value, cd_coupon_rate, cd_cr1000,
                        so_c, so_ep, avg_market_price)

    st.markdown("""
    ### Key Insights
    - Diluted EPS is generally lower than Basic EPS due to the potential dilution from convertible securities and stock options.
    - The extent of dilution depends on the terms of the dilutive securities (e.g., conversion ratios, exercise prices) and the company's financial performance.
    - Anti-dilution tests ensure that only dilutive securities that decrease EPS are included in the Diluted EPS calculation.

    ### References
    - [Investopedia: Earnings Per Share (EPS)](https://www.investopedia.com/terms/e/eps.asp)
    - [Corporate Finance Institute: Diluted EPS](https://corporatefinanceinstitute.com/resources/knowledge/finance/diluted-earnings-per-share-depsp/)
    """)
