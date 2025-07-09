
# Streamlit Application Requirements Specification: EPS Calculator & Dilution Impact

This document outlines the requirements for developing a Streamlit application based on the provided Jupyter Notebook content and user requirements. It will serve as a blueprint, detailing interactive components, data handling, visualization, and the integration of existing Python code.

## 1. Application Overview

The **EPS Calculator & Dilution Impact** Streamlit application aims to provide an interactive tool for financial analysts, investors, and students to understand and calculate Basic and Diluted Earnings Per Share (EPS). The application will simulate real-world financial scenarios, allowing users to manipulate key financial inputs and observe the real-time impact on EPS and its components through dynamic visualizations.

**Objectives:**
*   To enable users to input core financial data and parameters related to potentially dilutive securities.
*   To accurately calculate and display Basic and Diluted EPS using standard financial methodologies, including anti-dilution tests.
*   To visually represent the difference between Basic and Diluted EPS and the contribution of various dilutive securities.
*   To facilitate "what-if" scenario analysis by allowing dynamic adjustment of inputs.
*   To provide clear explanations of the underlying financial concepts and formulas.

## 2. User Interface Requirements

The application will feature a clear, intuitive, and interactive user interface designed for ease of use and immediate feedback.

### Layout and Navigation Structure
*   **Main Page Layout:** A single-page application structure.
*   **Sidebar for Inputs:** All user input widgets will be organized within a Streamlit sidebar (`st.sidebar`) for clear separation from results and visualizations.
*   **Main Content Area:** The primary results (calculated EPS values), formula explanations, and visualizations will occupy the main content area.

### Input Widgets and Controls
The application will provide interactive input fields for the following financial parameters. Default values will be populated using the `generate_synthetic_data` function from the notebook to provide a lightweight sample scenario. Each input will include an inline help tooltip (`help` parameter in Streamlit widgets) as per user requirements.

1.  **Core Financials:**
    *   **Net Income:** `st.number_input` (e.g., min_value=0, step=1000)
        *   *Help Text:* "The company's total earnings after all expenses, interest, and taxes."
    *   **Preferred Dividends:** `st.number_input` (e.g., min_value=0, step=100)
        *   *Help Text:* "Dividends paid to preferred shareholders, subtracted for Basic EPS and re-added for convertible preferred diluted EPS."
    *   **Weighted Average Shares Outstanding:** `st.number_input` (e.g., min_value=1, step=100)
        *   *Help Text:* "The number of common shares outstanding over the reporting period, weighted by the portion of the period they were outstanding."
    *   **Tax Rate:** `st.slider` (e.g., min_value=0.0, max_value=0.5, step=0.01, format="%.2f")
        *   *Help Text:* "The company's effective tax rate, used for after-tax interest savings on convertible debt."

2.  **Convertible Preferred Stock:**
    *   **Convertible Preferred Stock Count:** `st.number_input` (e.g., min_value=0, step=10)
        *   *Help Text:* "Number of outstanding convertible preferred shares."
    *   **Convertible Preferred Conversion Ratio:** `st.number_input` (e.g., min_value=0.0, step=0.1)
        *   *Help Text:* "Number of common shares obtainable upon conversion of one preferred share."

3.  **Convertible Debt:**
    *   **Convertible Debt Face Value:** `st.number_input` (e.g., min_value=0, step=1000)
        *   *Help Text:* "Total face value of outstanding convertible debt."
    *   **Convertible Debt Coupon Rate:** `st.slider` (e.g., min_value=0.0, max_value=0.2, step=0.001, format="%.3f")
        *   *Help Text:* "Annual interest rate (coupon) on the convertible debt."
    *   **Convertible Debt Conversion Ratio (Shares per \$1000):** `st.number_input` (e.g., min_value=0, step=1)
        *   *Help Text:* "Number of common shares obtainable for every \$1000 face value of convertible debt upon conversion."

4.  **Stock Options:**
    *   **Stock Option Count:** `st.number_input` (e.g., min_value=0, step=10)
        *   *Help Text:* "Number of outstanding stock options."
    *   **Stock Option Exercise Price:** `st.number_input` (e.g., min_value=0.0, step=0.1)
        *   *Help Text:* "The price at which common shares can be acquired upon exercising stock options."
    *   **Average Market Price:** `st.number_input` (e.g., min_value=0.0, step=0.1)
        *   *Help Text:* "Average market price of the common stock during the period, used in the Treasury Stock Method."

### Visualization Components
*   **EPS Metrics Display:** `st.metric` will be used to prominently display the calculated Basic EPS and Diluted EPS values.
*   **Comparative Bar Chart:** A Plotly bar chart (`st.plotly_chart`) will visualize the Basic EPS versus the Diluted EPS, allowing for a quick visual comparison of the dilution impact.
    *   **Chart Style:** Adopt a color-blind-friendly palette. Ensure clear titles, labeled axes, and legends. Font size for chart text will be set to $\geq 12 \text{ pt}$.
*   **Future Enhancements (Optional):** Consider adding visualizations that break down the impact of each dilutive security on total diluted shares outstanding or income adjustments, if deemed necessary for deeper insights.

### Interactive Elements and Feedback Mechanisms
*   **Real-time Updates:** As users adjust any input parameter, the EPS calculations and the visualizations will update instantaneously.
*   **Input Validation:** Implement basic validation (e.g., `min_value` for number inputs) to prevent unrealistic inputs where applicable.
*   **Help Text/Tooltips:** Each input control will have descriptive inline help text to guide users.

## 3. Additional Requirements

*   **Real-time Updates and Responsiveness:** Streamlit's architecture naturally supports real-time updates as input widgets are changed, ensuring a responsive user experience.
*   **Annotation and Tooltip Specifications:** As specified in Section 2.2, all input widgets will include informative tooltips or inline help text to explain their purpose and financial relevance.
*   **Performance:** The application should adhere to the "execute end-to-end on a mid-spec laptop (8 GB RAM) in fewer than 5 minutes" constraint. Given the nature of the calculations (simple arithmetic, no large datasets or complex models), this should be easily met.
*   **Open-Source Libraries:** Only open-source Python libraries (`pandas`, `numpy`, `plotly`, `streamlit`) will be used, as per the constraint.
*   **Color Palette and Font Size:** Plotly visualizations will be configured to use a color-blind-friendly palette and a font size of $\geq 12 \text{ pt}$ for optimal readability.

## 4. Notebook Content and Code Requirements

This section details how the provided Jupyter Notebook content and code will be integrated into the Streamlit application.

### Extracted Code and Streamlit Integration Strategy

All Python functions defined in the Jupyter Notebook will be directly incorporated into the Streamlit application's Python script.

1.  **Dependency Installation:**
    *   `!pip install pandas numpy plotly`
    *   *Streamlit Integration:* While these are `pip` commands for a notebook, in a Streamlit application, these libraries should be listed in a `requirements.txt` file for deployment. The script will import them directly.

2.  **`generate_synthetic_data(num_records)` function:**
    *   *Purpose:* Provides realistic synthetic financial data.
    *   *Streamlit Integration:* This function will be called once at the start of the Streamlit application to generate default values for all input widgets. This fulfills the "optional lightweight sample" requirement.
    *   *Relevant Code:*
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

3.  **`calculate_basic_eps(...)` function:**
    *   *Purpose:* Calculates Basic EPS.
    *   *Streamlit Integration:* This function will be called internally by `orchestrate_eps_calculation`. The formula will be displayed using `st.latex` or `st.markdown`.
    *   *Relevant Code:*
        ```python
        def calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding):
            """Calculates Basic Earnings Per Share (EPS)."""
            if wa_shares_outstanding <= 0:
                return 0.0
            available_income = net_income - preferred_dividends
            if available_income <= 0:
                return 0.0
            return available_income / wa_shares_outstanding
        ```
    *   *Mathematical Formula Display:*
        $$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$

4.  **`calculate_diluted_eps_preferred(...)` function:**
    *   *Purpose:* Calculates Diluted EPS considering Convertible Preferred Stock (If-Converted Method).
    *   *Streamlit Integration:* This logic is primarily encapsulated and managed within `orchestrate_eps_calculation` to ensure correct anti-dilution testing. The formula will be displayed using `st.latex` or `st.markdown`.
    *   *Relevant Code:* (Logic embedded in `orchestrate_eps_calculation`)
        ```python
        # Original:
        # def calculate_diluted_eps_preferred(net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio):
        #     new_shares = cps_count * cps_conv_ratio
        #     diluted_net_income = net_income + preferred_dividends_total
        #     diluted_shares = wa_shares_outstanding + new_shares
        #     if diluted_shares == 0:
        #         return float('inf')
        #     diluted_eps = diluted_net_income / diluted_shares
        #     return diluted_eps
        ```
    *   *Mathematical Formula Display:*
        $$ \text{Diluted EPS (Preferred)} = \frac{\text{Net Income} + \text{Preferred Dividends (re-added)}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

5.  **`calculate_diluted_eps_debt(...)` function:**
    *   *Purpose:* Calculates Diluted EPS considering Convertible Debt (If-Converted Method).
    *   *Streamlit Integration:* Similar to preferred stock, this logic is managed within `orchestrate_eps_calculation`. The formula will be displayed using `st.latex` or `st.markdown`.
    *   *Relevant Code:* (Logic embedded in `orchestrate_eps_calculation`)
        ```python
        # Original:
        # def calculate_diluted_eps_debt(net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate):
        #     interest_expense = cd_face_value * cd_coupon_rate
        #     after_tax_interest_savings = interest_expense * (1 - tax_rate)
        #     new_shares = (cd_face_value / 1000) * cd_conv_ratio_per_1000
        #     diluted_net_income = net_income + after_tax_interest_savings
        #     diluted_shares_outstanding = wa_shares_outstanding + new_shares
        #     # ... antidilution logic ...
        #     return diluted_eps
        ```
    *   *Mathematical Formula Display:*
        $$ \text{Diluted EPS (Debt)} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$
        where $\text{After-Tax Interest Savings} = \text{Interest Expense} \times (1 - \text{Tax Rate})$ and $\text{Interest Expense} = \text{Face Value} \times \text{Coupon Rate}$.

6.  **`calculate_diluted_eps_options(...)` function:**
    *   *Purpose:* Calculates Diluted EPS considering Stock Options (Treasury Stock Method).
    *   *Streamlit Integration:* Logic managed within `orchestrate_eps_calculation`. The formulas will be displayed using `st.latex` or `st.markdown`.
    *   *Relevant Code:* (Logic embedded in `orchestrate_eps_calculation`)
        ```python
        # Original:
        # def calculate_diluted_eps_options(net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price):
        #     if wa_shares_outstanding == 0: return 0.0
        #     if avg_market_price <= so_exercise_price:
        #         eps = (net_income - preferred_dividends_total) / wa_shares_outstanding
        #         return eps
        #     proceeds = so_count * so_exercise_price
        #     repurchased_shares = proceeds / avg_market_price
        #     incremental_shares = so_count - repurchased_shares
        #     diluted_eps = (net_income - preferred_dividends_total) / (wa_shares_outstanding + incremental_shares)
        #     # ... antidilution check ...
        #     return diluted_eps
        ```
    *   *Mathematical Formula Display:*
        $$ \text{Diluted EPS (Options)} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}} $$
        where $\text{Incremental Shares} = \text{Shares from Option Exercise} - \text{Shares Repurchased}$.
        $\text{Proceeds from Option Exercise} = \text{Number of Options} \times \text{Exercise Price}$.
        $\text{Shares Repurchased} = \frac{\text{Proceeds from Option Exercise}}{\text{Average Market Price}}$.

7.  **`orchestrate_eps_calculation(...)` function:**
    *   *Purpose:* Provides a comprehensive calculation of Basic and Diluted EPS, integrating all dilutive securities and crucial anti-dilution tests. This is the central calculation function.
    *   *Streamlit Integration:* This function will be called directly in the main content area of the Streamlit application, using the values retrieved from the user input widgets. Its returned `basic_eps` and `diluted_eps` values will be the primary results displayed.
    *   *Relevant Code:*
        ```python
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
        ```

8.  **`update_eps_display(...)` function:**
    *   *Purpose:* Calculates and displays EPS with visualizations. Its primary value for Streamlit is the Plotly visualization.
    *   *Streamlit Integration:* The calculation logic within this function will be replaced by a call to `orchestrate_eps_calculation` to ensure consistency with anti-dilution tests. The Plotly chart generation will be extracted and used with `st.plotly_chart` to display the comparison of basic and diluted EPS.
    *   *Relevant Code (Plotly Part):*
        ```python
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots

        # ... (after calling orchestrate_eps_calculation to get basic_eps and diluted_eps) ...

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
        ```

### Overall Streamlit Application Flow
1.  Import necessary libraries (`streamlit`, `pandas`, `numpy`, `plotly`).
2.  Define all Python functions (`generate_synthetic_data`, `calculate_basic_eps`, `calculate_diluted_eps_preferred`, `calculate_diluted_eps_debt`, `calculate_diluted_eps_options`, `orchestrate_eps_calculation`).
3.  Set the Streamlit page title and initial markdown description.
4.  Create a sidebar (`st.sidebar`) for all input parameters, populating them with default values from `generate_synthetic_data` and including help text.
5.  In the main content area:
    *   Call `orchestrate_eps_calculation` with the user-defined inputs to get the final Basic and Diluted EPS values.
    *   Display these values using `st.metric`.
    *   Present the mathematical formulas using `st.markdown` with LaTeX syntax.
    *   Generate and display the Plotly bar chart comparing Basic and Diluted EPS using `st.plotly_chart`.
6.  Add a "Key Insights" section and a "References" section using `st.markdown`.

This structured approach ensures that all user requirements and notebook content are systematically addressed in the Streamlit application development.
