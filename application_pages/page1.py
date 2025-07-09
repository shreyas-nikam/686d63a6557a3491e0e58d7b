
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
        'Convertible Preferred Dividend Per Share': np.random.uniform(0.1, 1), # Not used in orchestrate but present in prompt
        'Convertible Debt Face Value': np.random.randint(0, 1000000),
        'Convertible Debt Coupon Rate': np.random.uniform(0.05, 0.1),
        'Convertible Debt Conversion Ratio (Shares per $1000)': np.random.randint(20, 50),
        'Stock Option Count': np.random.randint(0, 50000),
        'Stock Option Exercise Price': np.random.uniform(5, 20),
        'Average Market Price': np.random.uniform(10, 30)
    }
    synthetic_data = pd.Series(data)
    return synthetic_data

def calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding):
    """Calculates Basic Earnings Per Share (EPS)."""
    if wa_shares_outstanding <= 0:
        return 0.0
    available_income = net_income - preferred_dividends
    if available_income <= 0: # If earnings available to common shareholders are negative or zero
        return 0.0
    return available_income / wa_shares_outstanding

def orchestrate_eps_calculation(ni, pd_val, was, tr, cps_c, cps_cr, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp):
    """Calculates Basic and Diluted EPS, integrating all dilutive securities and anti-dilution tests.
    ni: Net Income
    pd_val: Preferred Dividends
    was: Weighted Average Shares Outstanding
    tr: Tax Rate
    cps_c: Convertible Preferred Stock Count
    cps_cr: Convertible Preferred Conversion Ratio
    cd_fv: Convertible Debt Face Value
    cd_cr: Convertible Debt Coupon Rate
    cd_cr1000: Convertible Debt Conversion Ratio (Shares per $1000)
    so_c: Stock Option Count
    so_ep: Stock Option Exercise Price
    amp: Average Market Price
    """

    basic_eps = (ni - pd_val) / was if was > 0 else 0.0

    diluted_eps_current = basic_eps # Initialize with basic_eps for antidilution check

    # --- 1. Convertible Preferred Stock (If-Converted Method) ---
    # Add back preferred dividends, add shares from conversion
    if cps_c > 0 and cps_cr > 0:
        potential_new_shares_cps = cps_c * cps_cr
        if (was + potential_new_shares_cps) > 0:
            diluted_income_cps = ni # Add back preferred dividends as per if-converted method for preferred stock
            diluted_shares_cps = was + potential_new_shares_cps
            diluted_eps_cps_candidate = diluted_income_cps / diluted_shares_cps
            
            # Anti-dilution test: If this conversion would lower EPS, it's dilutive.
            # If the candidate EPS is less than the current diluted_eps_current, it means it's dilutive.
            if diluted_eps_cps_candidate < diluted_eps_current:
                diluted_eps_current = diluted_eps_cps_candidate


    # --- 2. Convertible Debt (If-Converted Method) ---
    # Add back after-tax interest savings, add shares from conversion
    if cd_fv > 0 and cd_cr > 0 and cd_cr1000 > 0:
        interest_expense = cd_fv * cd_cr
        after_tax_interest_savings = interest_expense * (1 - tr)
        potential_new_shares_cd = (cd_fv / 1000) * cd_cr1000
        
        if (was + potential_new_shares_cd) > 0:
            # For convertible debt, the earnings available for common shareholders need to be considered.
            # The prompt's formula: (Net Income + After-Tax Interest Savings - Preferred Dividends)
            diluted_income_cd = ni + after_tax_interest_savings - pd_val
            diluted_shares_cd = was + potential_new_shares_cd
            diluted_eps_cd_candidate = diluted_income_cd / diluted_shares_cd
            
            # Anti-dilution test
            if diluted_eps_cd_candidate < diluted_eps_current:
                diluted_eps_current = diluted_eps_cd_candidate

    # --- 3. Stock Options (Treasury Stock Method) ---
    # Only if Average Market Price > Exercise Price (dilutive)
    if so_c > 0 and amp > so_ep and was > 0:
        proceeds_from_exercise = so_c * so_ep
        shares_repurchased = proceeds_from_exercise / amp
        incremental_shares = so_c - shares_repurchased
        
        if (was + incremental_shares) > 0:
            # Earnings available for common shareholders (Net Income - Preferred Dividends)
            diluted_income_so = ni - pd_val
            diluted_shares_so = was + incremental_shares
            diluted_eps_so_candidate = diluted_income_so / diluted_shares_so
            
            # Anti-dilution test
            if diluted_eps_so_candidate < diluted_eps_current:
                diluted_eps_current = diluted_eps_so_candidate

    # Final check: Diluted EPS should never be greater than Basic EPS
    # This handles cases where all potential dilutive securities are anti-dilutive.
    if diluted_eps_current > basic_eps:
        diluted_eps_current = basic_eps

    return basic_eps, diluted_eps_current


def run_page1():
    st.title("EPS Calculator & Dilution Impact")
    st.markdown("""
    This application provides an interactive tool for financial analysts, investors, and students to understand and calculate Basic and Diluted Earnings Per Share (EPS). Manipulate the inputs in the sidebar to observe the real-time impact on EPS and its components through dynamic visualizations.
    """)

    synthetic_data = generate_synthetic_data()

    st.sidebar.header("Financial Inputs")

    st.sidebar.subheader("Core Financials")
    net_income = st.sidebar.number_input(
        "Net Income ($)",
        min_value=0,
        step=1000,
        value=int(synthetic_data['Net Income']),
        help="The company's total earnings after all expenses, interest, and taxes."
    )
    preferred_dividends = st.sidebar.number_input(
        "Preferred Dividends ($)",
        min_value=0,
        step=100,
        value=int(synthetic_data['Preferred Dividends']),
        help="Dividends paid to preferred shareholders, subtracted for Basic EPS and re-added for convertible preferred diluted EPS."
    )
    wa_shares_outstanding = st.sidebar.number_input(
        "Weighted Average Shares Outstanding",
        min_value=1,
        step=100,
        value=int(synthetic_data['Weighted Average Shares Outstanding']),
        help="The number of common shares outstanding over the reporting period, weighted by the portion of the period they were outstanding."
    )
    tax_rate = st.sidebar.slider(
        "Tax Rate",
        min_value=0.0,
        max_value=0.5,
        step=0.01,
        format="%.2f",
        value=float(synthetic_data['Tax Rate']),
        help="The company's effective tax rate, used for after-tax interest savings on convertible debt."
    )

    st.sidebar.subheader("Convertible Preferred Stock")
    cps_count = st.sidebar.number_input(
        "Convertible Preferred Stock Count",
        min_value=0,
        step=10,
        value=int(synthetic_data['Convertible Preferred Stock Count']),
        help="Number of outstanding convertible preferred shares."
    )
    cps_conversion_ratio = st.sidebar.number_input(
        "Convertible Preferred Conversion Ratio",
        min_value=0.0,
        step=0.1,
        value=float(synthetic_data['Convertible Preferred Conversion Ratio']),
        help="Number of common shares obtainable upon conversion of one preferred share."
    )

    st.sidebar.subheader("Convertible Debt")
    cd_face_value = st.sidebar.number_input(
        "Convertible Debt Face Value ($)",
        min_value=0,
        step=1000,
        value=int(synthetic_data['Convertible Debt Face Value']),
        help="Total face value of outstanding convertible debt."
    )
    cd_coupon_rate = st.sidebar.slider(
        "Convertible Debt Coupon Rate",
        min_value=0.0,
        max_value=0.2,
        step=0.001,
        format="%.3f",
        value=float(synthetic_data['Convertible Debt Coupon Rate']),
        help="Annual interest rate (coupon) on the convertible debt."
    )
    cd_conversion_ratio_per_1000 = st.sidebar.number_input(
        "Convertible Debt Conversion Ratio (Shares per $1000)",
        min_value=0,
        step=1,
        value=int(synthetic_data['Convertible Debt Conversion Ratio (Shares per $1000)']),
        help="Number of common shares obtainable for every $1000 face value of convertible debt upon conversion."
    )

    st.sidebar.subheader("Stock Options")
    so_count = st.sidebar.number_input(
        "Stock Option Count",
        min_value=0,
        step=10,
        value=int(synthetic_data['Stock Option Count']),
        help="Number of outstanding stock options."
    )
    so_exercise_price = st.sidebar.number_input(
        "Stock Option Exercise Price ($)",
        min_value=0.0,
        step=0.1,
        value=float(synthetic_data['Stock Option Exercise Price']),
        help="The price at which common shares can be acquired upon exercising stock options."
    )
    average_market_price = st.sidebar.number_input(
        "Average Market Price ($)",
        min_value=0.0,
        step=0.1,
        value=float(synthetic_data['Average Market Price']),
        help="Average market price of the common stock during the period, used in the Treasury Stock Method."
    )

    # Perform calculations
    basic_eps, diluted_eps = orchestrate_eps_calculation(
        net_income,
        preferred_dividends,
        wa_shares_outstanding,
        tax_rate,
        cps_count,
        cps_conversion_ratio,
        cd_face_value,
        cd_coupon_rate,
        cd_conversion_ratio_per_1000,
        so_count,
        so_exercise_price,
        average_market_price
    )

    st.subheader("Calculated EPS Values")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Basic EPS", value=f"\${basic_eps:.2f}")
    with col2:
        st.metric(label="Diluted EPS", value=f"\${diluted_eps:.2f}")

    st.subheader("Comparative Analysis")
    fig = make_subplots(rows=1, cols=1) # Single subplot as per visualization requirement

    fig.add_trace(go.Bar(
        x=['Basic EPS', 'Diluted EPS'],
        y=[basic_eps, diluted_eps],
        marker_color=['#648FFF', '#DC267F'] # Color-blind friendly palette (Blue and Red)
    ))
    fig.update_layout(
        title_text="Basic vs. Diluted EPS Comparison",
        font=dict(size=14), # Minimum font size 12pt
        yaxis_title="EPS ($)",
        height=400,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Formulas Explained")
    st.markdown(r"""
    **Basic EPS Formula:**
    $$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$

    **Diluted EPS Formula (General Principle):**
    Diluted EPS considers the potential dilution from securities that could be converted into common stock. The anti-dilution test is crucial: if a potential conversion would *increase* EPS (make it less dilutive), it is ignored.

    **1. Convertible Preferred Stock (If-Converted Method):**
    If dilutive, preferred dividends are added back to net income, and common shares from conversion are added to shares outstanding.
    $$ \text{Diluted EPS}_{\text{Preferred}} = \frac{\text{Net Income} + \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + (\text{Preferred Stock Count} \times \text{Conversion Ratio})} $$

    **2. Convertible Debt (If-Converted Method):**
    If dilutive, after-tax interest savings are added back to net income, and common shares from conversion are added to shares outstanding.
    $$ \text{After-Tax Interest Savings} = (\text{Face Value} \times \text{Coupon Rate}) \times (1 - \text{Tax Rate}) $$
    $$ \text{Shares from Conversion} = (\frac{\text{Face Value}}{1000}) \times \text{Conversion Ratio per \$1000} $$
    $$ \text{Diluted EPS}_{\text{Debt}} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

    **3. Stock Options (Treasury Stock Method):**
    If dilutive (average market price > exercise price), the proceeds from exercising options are assumed to be used to repurchase shares at the average market price. Only the net incremental shares are added to shares outstanding.
    $$ \text{Proceeds from Exercise} = \text{Option Count} \times \text{Exercise Price} $$
    $$ \text{Shares Repurchased} = \frac{\text{Proceeds from Exercise}}{\text{Average Market Price}} $$
    $$ \text{Incremental Shares} = \text{Option Count} - \text{Shares Repurchased} $$
    $$ \text{Diluted EPS}_{\text{Options}} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}} $$
    """)

    st.subheader("Key Insights")
    st.markdown("""
    *   **Dilution Impact:** Observe how the inclusion of potentially dilutive securities (convertible preferred stock, convertible debt, stock options) reduces EPS, providing a more conservative view of earnings per share.
    *   **Anti-Dilution Test:** Securities are only considered dilutive if their conversion would decrease EPS. If they increase EPS, they are excluded from the diluted EPS calculation.
    *   **What-If Analysis:** Adjust various inputs like Net Income, Tax Rate, or Average Market Price to understand their sensitivity and impact on Basic and Diluted EPS.
    """)

    st.subheader("References")
    st.markdown("""
    *   Financial Accounting Standards Board (FASB) ASC 260, Earnings Per Share.
    *   Investopedia: [Basic EPS](https://www.investopedia.com/terms/b/basic-eps.asp), [Diluted EPS](https://www.investopedia.com/terms/d/dilutedeps.asp), [Treasury Stock Method](https://www.investopedia.com/terms/t/treasurystockmethod.asp), [If-Converted Method](https://www.investopedia.com/terms/i/ifconvertedmethod.asp).
    """)
