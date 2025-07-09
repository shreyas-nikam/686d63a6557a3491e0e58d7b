
# Streamlit EPS Calculator & Dilution Impact Application Specification

## 1. Application Overview

### Purpose and Objectives
This Streamlit application will provide an interactive tool for understanding and calculating Basic and Diluted Earnings Per Share (EPS), demonstrating the impact of potentially dilutive securities. It aims to demystify complex financial calculations by allowing users to manipulate key financial inputs and observe real-time changes in EPS values and their visual representation.

The primary objectives are:
*   To enable interactive input of financial data relevant to EPS calculation.
*   To accurately calculate Basic and Diluted EPS based on user-defined parameters, including comprehensive anti-dilution testing.
*   To visually compare Basic and Diluted EPS, providing clear insights into the dilution effect.
*   To serve as a learning tool for financial concepts related to EPS, convertible securities, and stock options.
*   To facilitate "what-if" scenario analysis for financial performance on a per-share basis.

### Scope & Constraints
*   The application will be developed using open-source Python libraries (e.g., Streamlit, Pandas, NumPy, Plotly).
*   It must be performant, running end-to-end on a mid-spec laptop (8 GB RAM) with updates in less than 5 seconds.
*   All calculations will adhere to standard financial methodologies for EPS, including the 'If-Converted Method' for convertible preferred stock and convertible debt, and the 'Treasury Stock Method' for stock options, incorporating anti-dilution principles.

## 2. User Interface Requirements

### Layout and Navigation Structure
The application will feature a clear, single-page layout with a sidebar for input controls and the main area for displaying results and visualizations.
*   **Sidebar**: Will contain all user input widgets for financial parameters.
*   **Main Content Area**: Will display the calculated Basic and Diluted EPS values, along with interactive charts. Explanations of methodologies will be provided below the results.

### Input Widgets and Controls
The following financial parameters will be configurable by the user via Streamlit widgets, providing initial synthetic values for ease of use:

*   **Financial Performance (Core)**
    *   `Net Income`: Numeric input (e.g., `st.number_input`, with initial random value from 1,000,000 to 10,000,000).
    *   `Preferred Dividends`: Numeric input (e.g., `st.number_input`, with initial random value from 0 to 100,000).
    *   `Weighted Average Shares Outstanding`: Numeric input (e.g., `st.number_input`, with initial random value from 100,000 to 1,000,000).
    *   `Tax Rate`: Slider or number input for percentage (e.g., `st.slider` from 0.2 to 0.4, step 0.01).

*   **Convertible Preferred Stock**
    *   `Convertible Preferred Stock Count`: Numeric input (e.g., `st.number_input`, with initial random value from 0 to 10,000).
    *   `Convertible Preferred Conversion Ratio`: Numeric input (e.g., `st.number_input`, with initial random value from 0.5 to 2.0, step 0.1).
    *   `Convertible Preferred Dividend Per Share`: Numeric input (e.g., `st.number_input`, with initial random value from 0.1 to 1.0, step 0.01).

*   **Convertible Debt**
    *   `Convertible Debt Face Value`: Numeric input (e.g., `st.number_input`, with initial random value from 0 to 1,000,000).
    *   `Convertible Debt Coupon Rate`: Slider or number input for percentage (e.g., `st.slider` from 0.05 to 0.1, step 0.001).
    *   `Convertible Debt Conversion Ratio (Shares per $1000)`: Numeric input (e.g., `st.number_input`, with initial random value from 20 to 50).

*   **Stock Options**
    *   `Stock Option Count`: Numeric input (e.g., `st.number_input`, with initial random value from 0 to 50,000).
    *   `Stock Option Exercise Price`: Numeric input (e.g., `st.number_input`, with initial random value from 5.0 to 20.0, step 0.1).
    *   `Average Market Price`: Numeric input (e.g., `st.number_input`, with initial random value from 10.0 to 30.0, step 0.1).

### Visualization Components
A `plotly` bar chart will be displayed, comparing the calculated Basic EPS and Diluted EPS.
*   **Chart Type**: Bar chart (`go.Bar`).
*   **Data**: Basic EPS and Diluted EPS values.
*   **Labels**: Clear titles and labeled axes (e.g., "Basic EPS" and "Diluted EPS" on the x-axis, "EPS Value ($)" on the y-axis).
*   **Style**: Color-blind-friendly palette and readable font sizes (≥ 12 pt).

### Interactive Elements and Feedback Mechanisms
*   **Real-time Updates**: Changes to any input widget will automatically trigger recalculations and update the displayed EPS values and the `plotly` chart.
*   **Tooltips/Help Text**: Each input control will include inline help text or tooltips (`help` parameter) describing the financial concept it represents and its role in the calculation.
*   **Result Display**: Basic and Diluted EPS values will be prominently displayed with appropriate formatting (e.g., currency format).

## 3. Additional Requirements

### Real-time Updates and Responsiveness
The application will leverage Streamlit's reactive model to ensure that any modification to an input parameter instantly updates the calculated EPS figures and the associated visualizations. This provides a dynamic and responsive user experience crucial for scenario analysis.

### Annotation and Tooltip Specifications
Detailed explanations will be provided for each input parameter, calculation step, and the EPS methodologies. These will be implemented using:
*   `help` argument in Streamlit input widgets for concise explanations.
*   `st.markdown` to display the mathematical formulas and narrative descriptions (from the Jupyter Notebook's markdown cells) for Basic EPS, Diluted EPS (Convertible Preferred Stock), Diluted EPS (Convertible Debt), and Diluted EPS (Stock Options), ensuring strict LaTeX formatting.

## 4. Notebook Content and Code Requirements

This section details the extraction and integration of relevant code and content from the Jupyter Notebook into the Streamlit application. The `orchestrate_eps_calculation` function will be the primary driver for calculations due to its comprehensive anti-dilution testing.

### 4.1. Utility Function: Data Generation
The `generate_synthetic_data` function will be used to provide initial, realistic default values for the Streamlit input widgets, allowing the application to run immediately without user input.

**Python Code:**
```python
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
```

### 4.2. Basic EPS Calculation

**Narrative Explanation (from Notebook):**
Basic Earnings Per Share (EPS) is a fundamental financial metric that indicates the portion of a company's profit allocated to each outstanding share of common stock.
*   **Net Income**: The company's total earnings after all expenses, interest, and taxes.
*   **Preferred Dividends**: Dividends paid to preferred shareholders are subtracted because EPS only pertains to common shareholders.
*   **Weighted Average Shares Outstanding (WASO)**: The number of shares outstanding over a reporting period, weighted by the portion of the period they were outstanding. This is used to account for changes in the number of shares outstanding during the period.

**Formula (from Notebook):**
$$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$

**Python Code (from Notebook, adapted for orchestration):**
The `calculate_basic_eps` function is conceptually part of the `orchestrate_eps_calculation`.

```python
# Part of orchestrate_eps_calculation:
# basic_eps = (ni - pd) / was
```

### 4.3. Diluted EPS Calculation: Convertible Preferred Stock (If-Converted Method)

**Narrative Explanation (from Notebook):**
Diluted EPS accounts for all potentially dilutive securities that could decrease EPS if converted into common stock. For **Convertible Preferred Stock**, the 'if-converted method' assumes that all convertible preferred shares are converted into common shares at the beginning of the period (or date of issuance, if later). This method has two main adjustments:
1.  **Numerator Adjustment**: Preferred dividends are added back to net income because these dividends would not be paid if the preferred stock were converted.
2.  **Denominator Adjustment**: The number of common shares outstanding increases by the number of shares that would be issued upon conversion of the preferred stock.

**Formula (from Notebook):**
$$ \text{Diluted EPS (Preferred)} = \frac{\text{Net Income} + \text{Preferred Dividends (re-added)}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

**Python Code (from Notebook, adapted for orchestration):**
The `calculate_diluted_eps_preferred` function is conceptually part of the `orchestrate_eps_calculation`.

```python
# Part of orchestrate_eps_calculation:
# if cps_c > 0:
#     diluted_eps_cps = (ni + pd) / (was + cps_c * cps_cr)
#     if diluted_eps_cps < diluted_eps: # Apply antidilution test
#         diluted_eps = diluted_eps_cps
```

### 4.4. Diluted EPS Calculation: Convertible Debt (If-Converted Method)

**Narrative Explanation (from Notebook):**
Similar to convertible preferred stock, convertible debt also uses the 'if-converted method' for Diluted EPS. This method assumes that convertible debt is converted into common stock at the beginning of the period. The adjustments are:
1.  **Numerator Adjustment**: The after-tax interest expense on the convertible debt is added back to net income. This is because if the debt were converted, the company would no longer have to pay interest on it, and this saving would increase net income. The after-tax effect is important as interest expense is tax-deductible.
2.  **Denominator Adjustment**: The number of common shares outstanding increases by the number of shares that would be issued upon conversion of the debt.

**Formula (from Notebook):**
$$ \text{Diluted EPS (Debt)} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

**Python Code (from Notebook, adapted for orchestration):**
The `calculate_diluted_eps_debt` function is conceptually part of the `orchestrate_eps_calculation`.

```python
# Part of orchestrate_eps_calculation:
# if cd_fv > 0:
#     interest_expense = cd_fv * cd_cr
#     after_tax_interest_savings = interest_expense * (1 - tr)
#     diluted_eps_cd = (ni + after_tax_interest_savings - pd) / (was + (cd_fv / 1000) * cd_cr1000)
#     if diluted_eps_cd < diluted_eps: # Apply antidilution test
#         diluted_eps = diluted_eps_cd
```

### 4.5. Diluted EPS Calculation: Stock Options (Treasury Stock Method)

**Narrative Explanation (from Notebook):**
The Treasury Stock Method is used to account for stock options and warrants in Diluted EPS calculations. This method assumes that the options or warrants are exercised, and the company uses the proceeds to repurchase its own shares in the open market at the average market price.
1.  **No Numerator Adjustment**: There's no direct impact on net income from exercising stock options.
2.  **Denominator Adjustment**: The number of shares outstanding increases by the number of shares issued upon exercising the options, less the number of shares repurchased with the proceeds from exercising the options.

**Formulas (from Notebook):**
$$ \text{Diluted EPS (Options)} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}} $$
where:
$$ \text{Incremental Shares} = \text{Shares from Option Exercise} - \text{Shares Repurchased} $$
and the number of shares repurchased is calculated as:
$$ \text{Shares Repurchased} = \frac{\text{Proceeds from Option Exercise}}{\text{Average Market Price}} $$
The proceeds from exercising the options are calculated as:
$$ \text{Proceeds from Option Exercise} = \text{Number of Options} \times \text{Exercise Price} $$

**Python Code (from Notebook, adapted for orchestration):**
The `calculate_diluted_eps_options` function is conceptually part of the `orchestrate_eps_calculation`.

```python
# Part of orchestrate_eps_calculation:
# if so_c > 0 and amp > so_ep: # Options are dilutive only if market price > exercise price
#     proceeds_from_exercise = so_c * so_ep
#     shares_repurchased = proceeds_from_exercise / amp
#     incremental_shares = so_c - shares_repurchased
#     diluted_eps_so = (ni - pd) / (was + incremental_shares)
#     if diluted_eps_so < diluted_eps: # Apply antidilution test
#         diluted_eps = diluted_eps_so
# elif so_c > 0 and amp <= so_ep: # Options are antidilutive or at the money, do not include
#     pass
```

### 4.6. Orchestrating EPS Calculation (Comprehensive Dilution Analysis)

**Narrative Explanation (from Notebook, adapted for Streamlit context):**
The `orchestrate_eps_calculation` function provides a comprehensive calculation of both Basic and Diluted EPS. It integrates the logic for convertible preferred stock, convertible debt, and stock options, ensuring that the most dilutive scenario is presented for Diluted EPS. A critical aspect of diluted EPS is the anti-dilution test: if the effect of including a potentially dilutive security is to increase EPS (make it less dilutive), then that security is considered anti-dilutive and is excluded from the diluted EPS calculation. The diluted EPS should never be higher than basic EPS. This orchestration function encapsulates the business logic for assessing the full impact of a complex capital structure on a company's earnings per share.

**Python Code (from Notebook, core calculation logic):**
This function will be called directly by Streamlit based on user inputs.

```python
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
```

### 4.7. Dynamic EPS Display and Visualization

**Narrative Explanation (from Notebook, adapted for Streamlit context):**
This section integrates the calculated Basic and Diluted EPS values with interactive visualizations using `plotly`. Dynamic visualizations offer immense business value by enhancing understanding, facilitating scenario analysis, improving communication, and identifying antidilutive effects. The `plotly` chart will provide an immediate visual comparison of Basic and Diluted EPS as parameters are adjusted.

**Python Code (from Notebook, adapted for Streamlit):**
This code will be executed within the Streamlit application to render the visualization.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

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

```
