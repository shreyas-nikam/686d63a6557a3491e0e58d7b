# QuLab: Earnings Per Share (EPS) Calculator

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

**QuLab: Earnings Per Share (EPS) Calculator** is an interactive Streamlit application designed as a comprehensive lab project to explore and calculate Earnings Per Share (EPS) and its diluted counterpart. This tool provides a hands-on approach for students, financial analysts, and investors to understand the nuances of EPS calculation, including the impact of various dilutive securities.

The application focuses on two critical financial metrics:
*   **Basic EPS**: A fundamental measure representing the portion of a company's profit allocated to each outstanding share of common stock.
*   **Diluted EPS**: A more conservative measure that accounts for all potential sources of dilution, such as convertible securities (preferred stock, debt) and stock options, to give a "worst-case" scenario for earnings per share.

The lab also highlights the concept of **Anti-Dilution**, ensuring that only securities that would decrease EPS are included in the diluted calculation.

## Features

*   **Interactive Input**: Users can easily input various financial data points (Net Income, Preferred Dividends, Shares Outstanding, Tax Rate, Convertible Securities details, Stock Option details) via a user-friendly sidebar interface.
*   **Dynamic Calculations**: Real-time calculation of both Basic and Diluted EPS based on user-provided inputs.
*   **Comprehensive Dilution Analysis**: Incorporates logic for potential dilution from:
    *   Convertible Preferred Stock
    *   Convertible Debt
    *   Stock Options (using the Treasury Stock Method)
*   **Anti-Dilution Testing**: Automatically applies anti-dilution principles, excluding securities that would increase EPS if converted or exercised.
*   **Visual Comparison**: A clear Plotly bar chart visually compares Basic and Diluted EPS, providing immediate insights into the dilution effect.
*   **Synthetic Data Generation**: Automatically populates input fields with synthetic data upon launch, allowing for quick demonstrations and exploration without manual data entry.
*   **Educational Context**: Provides on-screen explanations of key concepts and formulas.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.7+ installed.
The application relies on the following Python libraries:

*   `streamlit`
*   `pandas`
*   `numpy`
*   `plotly`

### Installation

1.  **Clone the Repository (if applicable):**
    If this project is hosted on a Git repository, clone it to your local machine:
    ```bash
    git clone https://github.com/your-username/qucrete-eps-calculator.git
    cd qucrete-eps-calculator
    ```
    *(If not a Git repo, create the project directory and place the files inside it.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    Create a `requirements.txt` file in your project root with the following content:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    numpy>=1.20.0
    plotly>=5.0.0
    ```
    Then, install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit Application:**
    Navigate to the project's root directory (where `app.py` is located) in your terminal and run:
    ```bash
    streamlit run app.py
    ```
    This command will open the application in your default web browser (usually at `http://localhost:8501`).

2.  **Using the EPS Calculator:**
    *   The application will load with pre-filled synthetic data in the sidebar.
    *   Adjust the financial inputs in the **sidebar** to see how Basic and Diluted EPS change in real-time.
    *   The main content area displays the calculated Basic and Diluted EPS values and a comparative bar chart.
    *   Experiment with different values for Net Income, Preferred Dividends, Shares Outstanding, Convertible Securities, and Stock Options to observe their impact on dilution.
    *   Pay attention to how the **Average Market Price** affects the dilutive nature of Stock Options (options are only dilutive if `Average Market Price > Exercise Price`).
    *   Observe the anti-dilution principle in action: if including a security would increase EPS, it is excluded from the diluted calculation (resulting in Diluted EPS equaling Basic EPS or remaining higher than it was before considering that specific security).

## Project Structure

```
.
├── app.py
└── application_pages/
    └── eps_calculator.py
└── requirements.txt
└── README.md
```

*   `app.py`: The main entry point for the Streamlit application. It sets up the page configuration, displays the main title and introductory text, and handles navigation to different application pages.
*   `application_pages/`: A directory containing modules for different sections or functionalities of the application.
*   `application_pages/eps_calculator.py`: Contains the core logic for the EPS Calculator. This includes functions for generating synthetic data, performing the Basic and Diluted EPS calculations (including anti-dilution tests), and rendering the results and Plotly visualization.
*   `requirements.txt`: Lists all Python dependencies required to run the application.
*   `README.md`: This file, providing project information and instructions.

## Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web user interface.
*   **NumPy**: Used for numerical operations and generating synthetic data.
*   **Plotly**: For creating interactive and insightful data visualizations (bar charts).
*   **Pandas**: While not explicitly used for DataFrames in this specific logic, it's a common dependency in financial applications and often used implicitly with other libraries or for future enhancements.

## Contributing

This lab project was generated using the QuCreate platform by QuantUniversity, leveraging AI models for code generation. While direct contributions to this specific lab instance are not typically accepted, we encourage you to:

*   Fork the repository (if publicly available) to experiment and extend its functionalities.
*   Report any issues or suggest improvements by contacting QuantUniversity directly.

## License

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. Any reproduction or distribution of this demonstration, in whole or in part, requires prior written consent from QuantUniversity. This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.

## Contact

For more information about QuantUniversity and the QuCreate platform, please visit our website:

*   **Website**: [QuantUniversity](https://www.quantuniversity.com/)
*   **QuCreate**: (Specific link if available, otherwise direct to main site)
