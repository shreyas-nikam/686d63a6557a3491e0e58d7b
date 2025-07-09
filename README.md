# EPS Dilution Impact Analyzer (QuLab)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-ff69b4.svg)](https://streamlit.io/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)](./LICENSE.md)

## Project Title and Description

**QuLab: Earnings Per Share (EPS) Calculator & Dilution Impact Analyzer**

This project is a Streamlit-based interactive lab application designed to educate financial analysts, investors, and students on the calculation and impact of Basic and Diluted Earnings Per Share (EPS). It provides a dynamic environment to understand how various potentially dilutive securities—such as convertible preferred stock, convertible debt, and stock options—can affect a company's EPS. Users can adjust financial inputs in real-time and observe the changes in EPS calculations and visualizations.

The application also includes supplementary pages to review fundamental income statement structures and key financial ratios, making it a comprehensive educational tool for corporate finance and accounting principles.

## Features

*   **Interactive EPS Calculation:** Dynamically calculate Basic and Diluted EPS based on user-defined financial inputs.
*   **Comprehensive Dilution Analysis:** Incorporates the impact of:
    *   **Convertible Preferred Stock:** Using the If-Converted Method.
    *   **Convertible Debt:** Using the If-Converted Method, considering after-tax interest savings.
    *   **Stock Options:** Using the Treasury Stock Method, considering average market price vs. exercise price.
*   **Anti-Dilution Testing:** Automatically applies anti-dilution rules, ensuring securities are only considered dilutive if they reduce EPS.
*   **Real-time Visualization:** Compares Basic vs. Diluted EPS using an interactive Plotly bar chart.
*   **Formula Explanations:** Detailed mathematical formulas for Basic and Diluted EPS components (including LaTeX rendering).
*   **Key Insights:** Summarizes the educational takeaways regarding dilution and anti-dilution.
*   **Synthetic Data Generation:** Pre-populates inputs with synthetic data for quick experimentation.
*   **Educational Modules:**
    *   Overview of **Income Statement Structure**.
    *   Explanation of **Key Income Statement Ratios** with formulas.
*   **Intuitive User Interface:** Built with Streamlit for an engaging and easy-to-use experience.

## Getting Started

Follow these instructions to set up and run the Streamlit application on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/quolab-eps-analyzer.git
    cd quolab-eps-analyzer
    ```

    *(Note: Replace `https://github.com/your-username/quolab-eps-analyzer.git` with the actual repository URL if this project is hosted.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file should contain:
    ```
    streamlit
    pandas
    numpy
    plotly
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**
    A new tab will automatically open in your web browser, typically at `http://localhost:8501`.

3.  **Navigate and Interact:**
    *   Use the **sidebar dropdown** to switch between the "EPS Calculator & Dilution Impact" page and the educational "Page 2" and "Page 3".
    *   On the "EPS Calculator" page, adjust the financial inputs in the **sidebar**. Observe how the Basic and Diluted EPS values and the comparative chart update in real-time.
    *   Explore the formula explanations and key insights provided on the main page.

## Project Structure

The project is organized into logical directories to maintain clarity and modularity.

```
quolab-eps-analyzer/
├── application_pages/
│   ├── page1.py          # Core EPS Calculator and Dilution Impact logic & UI
│   ├── page2.py          # Income Statement Structure overview page
│   └── page3.py          # Key Income Statement Ratios overview page
├── app.py                # Main Streamlit application entry point and navigation
├── requirements.txt      # List of Python dependencies
└── README.md             # This README file
```

*   `app.py`: The central file that initializes the Streamlit application, sets up the page configuration, displays the sidebar navigation, and routes to the appropriate content pages based on user selection.
*   `application_pages/`: A directory containing individual Python files, each representing a distinct page or module within the Streamlit application. This structure promotes reusability and maintainability.
    *   `page1.py`: Contains all the logic and UI elements for the EPS Calculator, including data generation, calculation functions, interactive inputs, and visualizations.
    *   `page2.py`: Provides educational content on the structure of an income statement.
    *   `page3.py`: Provides educational content on key income statement ratios.

## Technology Stack

*   **Python**: The primary programming language.
*   **Streamlit**: The framework used for building interactive web applications with Python.
*   **Pandas**: Used for data manipulation, particularly for handling synthetic data.
*   **NumPy**: Essential for numerical operations and generating synthetic data.
*   **Plotly**: Utilized for creating interactive and informative data visualizations (bar charts).

## Contributing

This is a lab project, primarily for educational purposes. However, if you have suggestions for improvements or bug fixes, feel free to:

1.  **Fork** the repository.
2.  **Create a new branch** (`git checkout -b feature/your-feature-name` or `bugfix/issue-description`).
3.  **Make your changes** and commit them (`git commit -m 'feat: Add new feature'` or `fix: Resolve bug`).
4.  **Push** your branch (`git push origin feature/your-feature-name`).
5.  **Open a Pull Request** to the `main` branch of the original repository, describing your changes.

## License

© 2025 QuantUniversity. All Rights Reserved.

This application is developed as part of a QuantUniversity lab project and is intended solely for educational use and demonstration purposes. Any reproduction, distribution, or commercial use of this demonstration, in whole or in part, requires prior written consent from QuantUniversity.

**Disclaimer:** This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors. Users are encouraged to verify and validate all information and code.

## Contact

For inquiries or further information about QuantUniversity and its educational programs, please visit:

*   **Website:** [QuantUniversity](https://www.quantuniversity.com/)
*   **Email:** [info@quantuniversity.com](mailto:info@quantuniversity.com)