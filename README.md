Here's a comprehensive `README.md` file for your Streamlit application lab project.

---

# QuLab: Interactive EPS Calculator

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

This repository hosts a Streamlit application developed as part of a QuantUniversity Lab project. The application serves as an interactive tool to explore and calculate Earnings Per Share (EPS), demonstrating the impact of potential dilution from various financial instruments like convertible securities and stock options.

## 📚 Project Overview

Earnings Per Share (EPS) is a fundamental financial metric that indicates the portion of a company's profit allocated to each outstanding share of common stock. This application allows users to understand the distinction between Basic EPS and Diluted EPS by providing a hands-on simulation.

*   **Basic EPS** considers only the common shares currently outstanding.
*   **Diluted EPS** accounts for the potential dilution that could occur if all outstanding convertible securities (like convertible preferred stock, convertible debt) and stock options were exercised or converted into common shares. Understanding Diluted EPS is crucial for investors and analysts to accurately assess a company's earnings potential under a "worst-case" dilution scenario.

## ✨ Features

*   **Interactive Input Parameters**: Adjust key financial metrics (Net Income, Shares Outstanding, Tax Rate, etc.) and details of dilutive securities (convertible preferred stock, convertible debt, stock options) via a user-friendly sidebar.
*   **Dynamic EPS Calculation**: Real-time calculation of Basic and Diluted EPS based on your inputs.
*   **Comprehensive Dilution Analysis**: Incorporates the effects of:
    *   **Convertible Preferred Stock**: Using the "if-converted" method.
    *   **Convertible Debt**: Using the "if-converted" method, accounting for after-tax interest savings.
    *   **Stock Options**: Using the Treasury Stock Method, considering average market price vs. exercise price.
*   **Antidilution Test**: Automatically applies antidilution rules to ensure diluted EPS is never greater than basic EPS, correctly excluding antidilutive securities.
*   **Formula Visualization**: Displays the underlying mathematical formulas for Basic and Diluted EPS calculations using LaTeX.
*   **Visual Comparison**: A Plotly bar chart provides a clear visual comparison between Basic and Diluted EPS.
*   **Synthetic Data Generation**: Automatically populates initial input fields with synthetic data for quick testing and exploration.

## 🚀 Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

*   Python 3.7+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://www.github.com/your-username/qu-lab-eps-calculator.git # Replace with your actual repo URL
    cd qu-lab-eps-calculator
    ```

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

    ```bash
    pip install -r requirements.txt
    ```
    (Create a `requirements.txt` file with the following content if it doesn't exist):
    ```
    streamlit>=1.30.0
    pandas>=2.0.0
    numpy>=1.26.0
    plotly>=5.0.0
    ```

## 🏃‍♀️ Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  This command will open the application in your default web browser (usually at `http://localhost:8501`).

3.  **Interact with the application:**
    *   Use the sidebar on the left to adjust various financial parameters and details of convertible securities and stock options.
    *   Observe the real-time changes in Basic EPS and Diluted EPS metrics.
    *   Review the displayed formulas for a deeper understanding of the calculations.
    *   Analyze the bar chart to visually compare the two EPS values.

## 📁 Project Structure

```
qu-lab-eps-calculator/
├── app.py
├── application_pages/
│   └── page1.py
├── requirements.txt
└── README.md
```

*   `app.py`: The main entry point of the Streamlit application. It sets up the page configuration, displays the main introduction, and handles page navigation.
*   `application_pages/page1.py`: Contains the core logic for the "EPS Calculator" page, including data generation, EPS calculation functions (`orchestrate_eps_calculation`), and the Streamlit UI elements for user inputs and output display.
*   `requirements.txt`: Lists all the Python dependencies required to run the application.
*   `README.md`: This file, providing an overview of the project.

## 🛠 Technology Stack

*   **Streamlit**: For building the interactive web application interface.
*   **Pandas**: For data manipulation (used in synthetic data generation).
*   **NumPy**: For numerical operations, especially in synthetic data generation and calculations.
*   **Plotly**: For creating interactive data visualizations (bar charts).

## 🤝 Contributing

This project is primarily a lab demonstration. While formal contributions are not expected, if you have suggestions for improvements or find issues, please feel free to open an issue in the repository.

## 📜 License

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.

**Disclaimer**: This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.

## ✉️ Contact

For questions or inquiries regarding this project or QuantUniversity's programs, please visit:

*   **QuantUniversity Website**: [www.quantuniversity.com](https://www.quantuniversity.com/)

---