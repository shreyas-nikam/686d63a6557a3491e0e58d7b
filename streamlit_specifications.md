
# Streamlit Application Requirements Specification: EPS Calculator & Dilution Impact

## 1. Application Overview

### Purpose and Objectives
This Streamlit application provides an interactive platform for calculating and comparing **Basic Earnings Per Share (EPS)** and **Diluted EPS**. Its primary objective is to enable users to dynamically input key financial data and observe the immediate impact of various potentially dilutive securities on EPS calculations. This tool aims to demystify complex financial concepts by visually demonstrating the principles of the 'if-converted method' for convertible preferred stock and convertible debt, and the 'treasury stock method' for stock options and warrants.

### Target Audience and Use Cases
The primary target audience includes:
*   **Students and Learners:** To reinforce understanding of EPS calculations and the effects of complex capital structures as presented in financial statement analysis curricula.
*   **Financial Analysts and Investors:** To perform quick scenario analysis on a company's EPS under different hypothetical dilution scenarios.
*   **Corporate Finance Professionals:** To assess the potential dilutive impact of various outstanding securities on earnings per share.

### Key Value Propositions
*   **Interactive Learning:** Provides a hands-on approach to understanding EPS dilution.
*   **Instant Feedback:** Visualizes changes in EPS in real-time as input parameters are adjusted.
*   **Scenario Modeling:** Allows users to easily test "what-if" scenarios for different dilutive securities.
*   **Clarity and Simplicity:** Breaks down complex accounting methods into understandable components and formulas.
*   **Decision Support:** Helps identify and assess the implications of dilutive versus antidilutive effects on per-share earnings.

## 2. User Interface Requirements

### Layout and Navigation Structure
The application will feature a clear, intuitive single-page layout.
*   **Sidebar (`st.sidebar`):** Dedicated to all user input controls, allowing the main content area to remain focused on results and visualizations.
*   **Main Content Area:** Will display calculated EPS values, a summary of current inputs, and all interactive visualizations.
*   **Sections:** The main content will logically divide into:
    *   "Current EPS Snapshot" displaying numerical results.
    *   "EPS Comparison" for aggregated visualization.
    *   "Scenario Analysis" for dynamic relationship plots.

### Input Widgets and Controls
All input controls will be placed in the sidebar to ensure a clean user experience. Inline help text or tooltips will be provided for each control (`st.info` or `st.tooltip`).

#### A. Core Financial Data Inputs
*   **Net Income:** Numeric input (`st.number_input`) for the company's total earnings.
*   **Preferred Dividends:** Numeric input for dividends paid to preferred shareholders.
*   **Weighted Average Shares Outstanding (WASO):** Numeric input for common shares outstanding.
*   **Tax Rate:** Slider input (`st.slider`) for the corporate tax rate, ranging from $0.0$ to $1.0$.

#### B. Potentially Dilutive Securities Inputs
A series of checkboxes will allow users to enable/disable specific types of dilutive securities. When a checkbox is selected, relevant input fields for that security type will appear.
*   **Convertible Preferred Stock:**
    *   Checkbox: `st.checkbox("Include Convertible Preferred Stock")`
    *   If checked:
        *   **Convertible Preferred Stock Count:** Numeric input for the number of convertible preferred shares.
        *   **Convertible Preferred Conversion Ratio:** Numeric input for shares of common stock per preferred share.
        *   **Convertible Preferred Dividend Per Share:** Numeric input for the annual dividend paid per preferred share (this input, combined with `Convertible Preferred Stock Count`, determines total preferred dividends re-added in the numerator).
*   **Convertible Debt:**
    *   Checkbox: `st.checkbox("Include Convertible Debt")`
    *   If checked:
        *   **Convertible Debt Face Value:** Numeric input for the total face value of convertible debt.
        *   **Convertible Debt Coupon Rate:** Slider input for the annual coupon rate.
        *   **Convertible Debt Conversion Ratio (Shares per $1000):** Numeric input for common shares per $1,000$ face value of debt.
*   **Stock Options:**
    *   Checkbox: `st.checkbox("Include Stock Options")`
    *   If checked:
        *   **Stock Option Count:** Numeric input for the number of outstanding stock options.
        *   **Stock Option Exercise Price:** Numeric input for the price at which options can be exercised.
        *   **Average Market Price:** Numeric input for the average market price of the common stock during the period. This input is crucial for the treasury stock method.

### Output Display
*   **Calculated EPS Values:** Clear display of "Basic EPS" and "Diluted EPS" (orchestrated to include all selected dilutive securities and antidilution test) with two decimal places, e.g., `Basic EPS: $X.XX`, `Diluted EPS: $Y.YY`.
*   **Antidilution Warning:** A clear message (e.g., `st.warning`) will be displayed if a security is determined to be antidilutive and thus excluded from the diluted EPS calculation (i.e., if `Diluted EPS > Basic EPS`, then `Diluted EPS` is set to `Basic EPS`).
*   **Summary of Inputs:** A read-only section summarizing the currently active inputs used for the calculations.

### Interactive Elements
*   **Dynamic Updates:** All calculated values and visualizations will update in real-time as user inputs in the sidebar are changed.
*   **Input Validation:** Basic validation (e.g., non-negative shares, non-zero denominator where applicable) will be implemented with informative error messages (`st.error`).

## 3. Visualization Requirements

### Chart Types and Libraries
*   **Aggregated Comparison Plot:** A bar chart will compare Basic EPS and the calculated Diluted EPS.
*   **Relationship Plot:** A line or scatter plot showing how Diluted EPS changes as a *single selected continuous input variable* (e.g., `Average Market Price` for options, `Convertible Preferred Conversion Ratio` for preferred stock) is varied across a defined range, while other inputs remain constant.
*   **Visualization Library:** Plotly (`plotly.graph_objects`) will be used for all visualizations to leverage its interactive features.

### Interactive Visualization Features
*   **Hover-tooltips:** Plotly's native hover-tooltips will provide detailed data points and calculation breakdowns upon hovering over chart elements.
*   **Zoom and Pan:** Standard Plotly controls for zooming and panning will be enabled.
*   **Real-time Updates:** Visualizations must update dynamically and responsively whenever an input parameter is changed.
*   **Customizable Display:**
    *   The application will adopt a color-blind-friendly palette.
    *   Font sizes for text and labels in plots will be set to be easily readable (≥ 12pt).

### Annotation and Tooltip Specifications
*   **Clear Titles:** All plots will have automatically generated, descriptive titles (e.g., "Basic vs. Diluted EPS Comparison", "Impact of Average Market Price on Diluted EPS").
*   **Labeled Axes:** Axes will be clearly labeled with units where appropriate (e.g., "EPS ($)", "Average Market Price ($)").
*   **Legends:** Legends will be provided for multiple data series (e.g., "Basic EPS", "Diluted EPS").
*   **Static Fallback:** A button will be provided to allow users to save the generated visualizations as high-resolution PNG images.

### Scenario Analysis Visualization
*   A dropdown will allow the user to select one key continuous variable from the dilutive securities (e.g., `Average Market Price`, `Convertible Preferred Conversion Ratio`, `Convertible Debt Coupon Rate`).
*   Upon selection, a dedicated `st.slider` will appear to define the range for this selected variable for the relationship plot.
*   The relationship plot will then dynamically display how Diluted EPS (considering all active dilutive securities, but sweeping the selected one) changes across the specified range of the chosen variable.

### Mathematical Formulas for Display
The following formulas will be displayed within the application using LaTeX notation for clarity and precision:

**Basic EPS Formula:**
$$ \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}} $$

**Diluted EPS with Convertible Preferred Stock (If-Converted Method):**
$$ \text{Diluted EPS (Preferred)} = \frac{\text{Net Income} + \text{Preferred Dividends (re-added)}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

**Diluted EPS with Convertible Debt (If-Converted Method):**
$$ \text{Diluted EPS (Debt)} = \frac{\text{Net Income} + \text{After-Tax Interest Savings} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Shares from Conversion}} $$

**Diluted EPS with Stock Options (Treasury Stock Method):**
$$ \text{Diluted EPS (Options)} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding} + \text{Incremental Shares}} $$
where:
$$ \text{Incremental Shares} = \text{Shares from Option Exercise} - \text{Shares Repurchased} $$
$$ \text{Shares Repurchased} = \frac{\text{Proceeds from Option Exercise}}{\text{Average Market Price}} $$
$$ \text{Proceeds from Option Exercise} = \text{Number of Options} \times \text{Exercise Price} $$

**Required Libraries:**
The application will use the following open-source Python libraries from PyPI:
*   `pandas`
*   `numpy`
*   `plotly`
*   `streamlit`

