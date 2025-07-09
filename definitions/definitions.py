import pandas as pd
import numpy as np

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

def calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding):
    """Calculates Basic Earnings Per Share (EPS)."""
    if wa_shares_outstanding <= 0:
        return 0.0
    available_income = net_income - preferred_dividends
    if available_income <= 0:
        return 0.0
    return available_income / wa_shares_outstanding

def calculate_diluted_eps_preferred(net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio):
    """Calculates Diluted EPS with Convertible Preferred Stock (If-Converted Method)."""
    new_shares = cps_count * cps_conv_ratio
    diluted_net_income = net_income + preferred_dividends_total # Add back preferred dividends
    diluted_shares = wa_shares_outstanding + new_shares

    if diluted_shares == 0:
        return float('inf')

    diluted_eps = diluted_net_income / diluted_shares
    return diluted_eps

def calculate_diluted_eps_debt(net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate):
    """Calculates Diluted EPS considering Convertible Debt (If-Converted Method)."""

    interest_expense = cd_face_value * cd_coupon_rate
    after_tax_interest_savings = interest_expense * (1 - tax_rate)
    
    new_shares = (cd_face_value / 1000) * cd_conv_ratio_per_1000
    diluted_net_income = net_income + after_tax_interest_savings
    diluted_shares_outstanding = wa_shares_outstanding + new_shares
    
    if cd_face_value == 0:
        diluted_eps = (net_income - preferred_dividends_total) / wa_shares_outstanding if wa_shares_outstanding else net_income
    else:
        diluted_eps = (diluted_net_income - preferred_dividends_total) / diluted_shares_outstanding if diluted_shares_outstanding else diluted_net_income

    return diluted_eps

def calculate_diluted_eps_options(net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price):
                """Calculates Diluted EPS considering Stock Options using the Treasury Stock Method."""
                if wa_shares_outstanding == 0:
                    return 0.0
                
                if avg_market_price <= so_exercise_price:
                    eps = (net_income - preferred_dividends_total) / wa_shares_outstanding
                    return eps
                
                proceeds = so_count * so_exercise_price
                repurchased_shares = proceeds / avg_market_price
                incremental_shares = so_count - repurchased_shares
                
                diluted_eps = (net_income - preferred_dividends_total) / (wa_shares_outstanding + incremental_shares)
                basic_eps = (net_income - preferred_dividends_total) / wa_shares_outstanding
                
                if diluted_eps < basic_eps:
                    return diluted_eps
                else:
                    return float('inf')

def orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp):
    """Calculates Basic and Diluted EPS."""

    basic_eps = (ni - pd) / was

    diluted_eps = basic_eps

    # Convertible Preferred Stock
    if cps_c > 0:
        diluted_eps_cps = ni / (was + cps_c * cps_cr)
        if diluted_eps_cps < diluted_eps:
            diluted_eps = diluted_eps_cps

    # Convertible Debt
    if cd_fv > 0:
        interest_expense = cd_fv * cd_cr
        after_tax_interest_savings = interest_expense * (1 - tr)
        diluted_eps_cd = (ni + after_tax_interest_savings - pd) / (was + (cd_fv / 1000) * cd_cr1000)
        if diluted_eps_cd < diluted_eps:
            diluted_eps = diluted_eps_cd

    # Stock Options
    if so_c > 0 and amp > so_ep:
        proceeds_from_exercise = so_c * so_ep
        shares_repurchased = proceeds_from_exercise / amp
        incremental_shares = so_c - shares_repurchased
        diluted_eps_so = (ni - pd) / (was + incremental_shares)
        if diluted_eps_so < diluted_eps:
            diluted_eps = diluted_eps_so

    return basic_eps, diluted_eps

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def update_eps_display(net_income, preferred_dividends, wa_shares_outstanding, tax_rate, cps_count, cps_conv_ratio, cps_div_per_share, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, so_count, so_exercise_price, avg_market_price):
    """Calculates and displays Basic and Diluted EPS with visualizations."""

    # Basic EPS Calculation
    net_income_available = net_income - preferred_dividends
    if wa_shares_outstanding == 0:
        basic_eps = 0.0
    else:
        basic_eps = net_income_available / wa_shares_outstanding

    # Diluted EPS Calculation Adjustments
    add_shares_cps = cps_count * cps_conv_ratio
    add_income_cps = cps_count * cps_div_per_share
    interest_expense = cd_face_value * cd_coupon_rate
    tax_shield = interest_expense * tax_rate
    add_shares_cd = cd_face_value / 1000 * cd_conv_ratio_per_1000
    
    if avg_market_price > 0:
        incremental_shares_so = max(0, (1 - (so_exercise_price / avg_market_price))) * so_count
    else:
        incremental_shares_so = 0

    # Diluted EPS Calculation
    diluted_net_income_available = net_income - preferred_dividends + interest_expense - tax_shield + add_income_cps
    diluted_wa_shares_outstanding = wa_shares_outstanding + add_shares_cps + add_shares_cd + incremental_shares_so
    
    if diluted_wa_shares_outstanding == 0:
        diluted_eps = 0.0
    else:
        diluted_eps = diluted_net_income_available / diluted_wa_shares_outstanding

    print(f"Basic EPS: ${basic_eps:.2f}")
    print(f"Diluted EPS: ${diluted_eps:.2f}")