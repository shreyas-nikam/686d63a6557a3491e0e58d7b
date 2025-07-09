# EPS Calculator: A Streamlit Application for Understanding Earnings Per Share and Dilution

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## 📊 Project Description

This Streamlit application serves as an interactive educational tool designed to help users understand the concepts of Basic Earnings Per Share (EPS) and Diluted EPS. It provides a platform to explore how various financial instruments, such as convertible preferred stock, convertible debt, and stock options, can impact a company's EPS through potential dilution.

The application allows users to input core financial data and then dynamically add different dilutive securities. It calculates and visualizes both Basic and Diluted EPS, demonstrating the effects of potential conversions and exercises. Furthermore, it includes a scenario analysis feature to illustrate how Diluted EPS changes across a range of values for a selected input variable.

**Key Concepts Explored:**

*   **Basic EPS:** Earnings per share calculated based on common shares outstanding.
    $$
    \text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding}}
    $$
*   **Diluted EPS:** A more conservative measure that accounts for the potential conversion of all dilutive securities into common shares.
*   **If-Converted Method:** Applied to convertible preferred stock and convertible debt, assuming conversion at the beginning of the period.
*   **Treasury Stock Method:** Used for stock options and warrants, assuming proceeds from exercise are used to repurchase shares.
*   **Antidilution:** Understanding when securities are excluded from Diluted EPS calculation because their inclusion would increase EPS.

## ✨ Features

*   **Basic EPS Calculation:** Instantly calculates Basic Earnings Per Share based on net income, preferred dividends, and weighted average shares outstanding.
*   **Comprehensive Diluted EPS Calculation:**
    *   Includes logic for **Convertible Preferred Stock** using the If-Converted Method.
    *   Accounts for **Convertible Debt** using the If-Converted Method.
    *   Integrates **Stock Options** using the Treasury Stock Method.
*   **Interactive Input Forms:** User-friendly sliders, number inputs, and checkboxes to adjust financial parameters and include/exclude dilutive securities.
*   **Antidilution Check:** Automatically identifies and excludes antidilutive securities, ensuring accurate Diluted EPS calculation as per accounting standards.
*   **Dynamic Visualizations:** Utilizes Plotly to generate clear and interactive bar charts comparing Basic vs. Diluted EPS, and line graphs for scenario analysis.
*   **Scenario Analysis:** Explore the sensitivity of Diluted EPS to changes in key variables like:
    *   Average Market Price (for stock options)
    *   Convertible Preferred Conversion Ratio
    *   Convertible Debt Coupon Rate
*   **Input Summary:** Displays a tabular summary of all entered financial data and dilutive security parameters for easy review.
*   **Modular Codebase:** Organized into separate files for better maintainability and readability.

## 🚀 Getting Started

Follow these instructions to set up and run the EPS Calculator application on your local machine.

### Prerequisites

*   Python 3.7+

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/eps-calculator-streamlit.git
    cd eps-calculator-streamlit
    ```
    *(Note: Replace `https://github.com/yourusername/eps-calculator-streamlit.git` with the actual repository URL if this project is hosted.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**

    Create a `requirements.txt` file in the root directory of your project with the following content:

    ```
    streamlit
    numpy
    pandas
    plotly
    ```

    Then, install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

## 🎮 Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**
    Your web browser should automatically open to the application's local URL (usually `http://localhost:8501`). If not, copy and paste the URL displayed in your terminal into your browser.

3.  **Navigate and Interact:**
    *   Use the sidebar to switch between "EPS Calculation" and "Scenario Analysis" pages.
    *   On the "EPS Calculation" page, enter core financial data and use the checkboxes to include/exclude different dilutive securities. Adjust their respective parameters to see the impact on Basic and Diluted EPS.
    *   On the "Scenario Analysis" page, select a variable and its range to observe how Diluted EPS changes across various scenarios.

## 📁 Project Structure

The project is organized into a clear and modular structure:

```
eps-calculator-streamlit/
├── app.py
├── application_pages/
│   ├── __init__.py
│   ├── eps_calculation.py
│   └── scenario_analysis.py
└── requirements.txt
```

*   `app.py`: The main Streamlit entry point. It sets up the page configuration, displays the introductory text, and handles navigation between different application pages.
*   `application_pages/`: A directory containing modular components for different sections of the application.
    *   `eps_calculation.py`: Contains the Streamlit code for the core EPS calculation page, including input widgets, calculations, and visualizations for Basic and Diluted EPS.
    *   `scenario_analysis.py`: Contains the Streamlit code for the scenario analysis page, allowing users to test the sensitivity of Diluted EPS to changes in specific variables. It also houses the `calculate_diluted_eps` helper function.
*   `requirements.txt`: Lists all Python dependencies required to run the application.

## 🛠️ Technology Stack

*   **Python:** The core programming language.
*   **Streamlit:** The primary framework used for building the interactive web application.
*   **NumPy:** Used for numerical operations, particularly in scenario analysis for generating ranges.
*   **Pandas:** Used for data manipulation, particularly for displaying input summaries.
*   **Plotly:** Utilized for generating interactive and visually appealing charts (bar charts and line plots).

## 🤝 Contributing

This project is primarily for educational purposes and internal lab use, generated by the QuCreate platform. Therefore, we are not actively seeking external contributions at this time. However, if you find any issues, have suggestions, or general feedback, please feel free to open an issue on the repository.

## 📝 License

This application is copyrighted by **QuantUniversity** and all rights are reserved. It is provided for educational and illustrative purposes only. Any reproduction or distribution of this demonstration requires prior written consent from QuantUniversity.

Please note that this lab was generated using the **QuCreate platform**, which relies on AI models for code generation, and may contain inaccuracies or errors.

© 2025 QuantUniversity. All Rights Reserved.

## ✉️ Contact

For inquiries, feedback, or further information about QuantUniversity and their educational platforms, please visit:

[QuantUniversity Website](https://www.quantuniversity.com/)
