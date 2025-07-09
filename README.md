This comprehensive README.md provides a detailed overview of the Streamlit application for calculating Basic and Diluted Earnings Per Share.

---

# QuLab: Basic & Diluted EPS Calculator

## 🚀 Project Overview

**QuLab: Basic & Diluted EPS Calculator** is an interactive Streamlit application designed as an educational lab project to help users understand the crucial financial metrics of Basic Earnings Per Share (EPS) and Diluted Earnings Per Share (EPS). The application allows users to input various financial parameters and instantly observe the calculation of these metrics, along with a visual representation of their impact.

Understanding EPS is fundamental for financial analysis, as it signifies the portion of a company's profit allocated to each outstanding share of common stock. Diluted EPS, in particular, offers a more conservative perspective by considering the potential dilution from convertible securities like stock options, convertible preferred stock, and convertible debt.

This application simplifies complex financial concepts, making them accessible for learning and exploration.

## ✨ Features

*   **Interactive Input Fields**: Easily adjust key financial metrics such as Net Income, Preferred Dividends, Weighted Average Shares Outstanding, and Tax Rate.
*   **Comprehensive Dilutive Securities Handling**: Input parameters for:
    *   **Convertible Preferred Stock**: Account for its potential conversion using the **If-Converted Method**.
    *   **Convertible Debt**: Calculate the dilutive impact considering interest savings and conversion, also using the **If-Converted Method**.
    *   **Stock Options**: Apply the **Treasury Stock Method** to determine the dilutive effect of outstanding options.
*   **Real-time EPS Calculation**: See Basic and Diluted EPS values update instantly as inputs are changed.
*   **Anti-Dilution Test**: Automatically incorporates the anti-dilution principle, ensuring that securities are only included if they decrease EPS (or increase loss per share), and Diluted EPS never exceeds Basic EPS.
*   **Formula Display**: Clear presentation of the mathematical formulas used for Basic and Diluted EPS calculations.
*   **Visual Comparison**: A bar chart visually compares Basic EPS and Diluted EPS, highlighting the potential dilution.
*   **Synthetic Data Generation**: Default input values are populated with synthetic data for quick experimentation.
*   **Educational Context**: Provides explanations of core concepts and methodologies (If-Converted Method, Treasury Stock Method).

## 🏁 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need Python 3.8+ installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/quolab-eps-calculator.git
    cd quolab-eps-calculator
    ```

    *(Note: Replace `https://github.com/your-username/quolab-eps-calculator.git` with the actual repository URL if this project is hosted.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    First, generate the `requirements.txt` file (if not already present):
    ```bash
    pip freeze > requirements.txt
    ```
    Then, install:
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` is not provided, manually install the dependencies: `pip install streamlit pandas numpy plotly`)*

## 🚀 Usage

Once the dependencies are installed, you can run the Streamlit application:

```bash
streamlit run app.py
```

This command will open the application in your default web browser (usually at `http://localhost:8501`).

### How to Use:

1.  **Adjust Inputs**: Use the sidebar on the left to modify the financial parameters:
    *   **Net Income**, **Preferred Dividends**, **Weighted Average Shares Outstanding**, and **Tax Rate** under "Input Parameters".
    *   Parameters for **Convertible Preferred Stock**, **Convertible Debt**, and **Stock Options** in their respective sections.
2.  **Observe Results**:
    *   Basic EPS and Diluted EPS metrics are displayed prominently in the main section.
    *   The "Basic vs. Diluted EPS Comparison" chart will dynamically update to reflect your changes.
    *   Review the "EPS Formulas" and "Key Insights" sections for a deeper understanding.

## 📁 Project Structure

The project is organized into a modular structure for clarity and maintainability:

```
quolab-eps-calculator/
├── app.py                      # Main Streamlit application entry point.
├── application_pages/          # Directory for different application modules/pages.
│   └── eps_calculator.py       # Contains the core logic for EPS calculation and its UI components.
├── .streamlit/                 # (Optional) Streamlit configuration files.
│   └── config.toml
├── requirements.txt            # List of Python dependencies.
└── README.md                   # Project documentation.
```

## 🛠️ Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For creating the interactive web application interface.
*   **Pandas**: Used for data handling (though primarily `pd.Series` for synthetic data).
*   **NumPy**: For numerical operations, especially in synthetic data generation.
*   **Plotly**: For generating interactive and visually appealing charts.

## 🤝 Contributing

This project is primarily an educational lab exercise. Contributions are not actively sought at this time. However, if you find any bugs or have suggestions for improvements, please feel free to open an issue in the repository.

## ⚖️ License

This application is developed for educational use and illustration purposes only.

© 2025 QuantUniversity. All Rights Reserved.

Any reproduction of this demonstration requires prior written consent from QuantUniversity. This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.

## 📞 Contact

For questions or inquiries related to this lab project or QuantUniversity's educational platforms, please visit:

*   **QuantUniversity Website**: [www.quantuniversity.com](https://www.quantuniversity.com/)