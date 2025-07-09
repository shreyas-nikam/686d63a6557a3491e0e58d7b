This comprehensive `README.md` file is designed for the Streamlit application lab project, "QuLab: Earnings Per Share (EPS) Dilution Analyzer."

---

# QuLab: Earnings Per Share (EPS) Dilution Analyzer

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

**QuLab: Earnings Per Share (EPS) Dilution Analyzer** is an interactive Streamlit web application designed as a lab project to explore and visualize the concept of Earnings Per Share (EPS) and how various financial instruments can dilute it. Understanding EPS is fundamental for investors and financial analysts to assess a company's profitability on a per-share basis.

This application provides a hands-on environment to manipulate key financial inputs and observe the real-time impact on Basic EPS and Diluted EPS, along with dynamic visualizations. It covers the core principles and calculations involved in determining EPS under different scenarios of potential dilution.

## Features

This application offers the following key functionalities:

*   **Interactive Input Parameters**: Adjust critical financial metrics such as Net Income, Preferred Dividends, Weighted Average Shares Outstanding, and Tax Rate using user-friendly sliders and number inputs.
*   **Dilutive Securities Analysis**: Simulate the impact of various dilutive instruments:
    *   **Convertible Preferred Stock**: Explore how conversion of preferred shares into common shares affects EPS.
    *   **Convertible Debt**: Analyze the dilutive effect of convertible bonds, considering after-tax interest savings.
    *   **Stock Options**: Understand the impact of employee stock options using the Treasury Stock Method.
*   **Real-time EPS Calculation**: Instantly view updated Basic EPS and Diluted EPS values as input parameters are changed.
*   **Dynamic Visualizations**: A clear bar chart comparison of Basic EPS vs. Diluted EPS, designed with color-blind friendly palettes for enhanced accessibility.
*   **Anti-Dilution Logic**: Integrates anti-dilution tests to ensure that only securities that genuinely decrease EPS are included in the Diluted EPS calculation, adhering to financial reporting standards.
*   **Educational Content**: Provides in-app formulae, key insights, and references for a deeper understanding of EPS concepts and calculations.
*   **Modular Code Structure**: Separates application logic from the main Streamlit UI for better organization and maintainability.

## Getting Started

Follow these instructions to set up and run the QuLab EPS Dilution Analyzer on your local machine.

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/QuLab-EPS-Analyzer.git
    cd QuLab-EPS-Analyzer
    ```
    *(Note: Replace `https://github.com/your-username/QuLab-EPS-Analyzer.git` with the actual repository URL if available, otherwise assume local files.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**
    Create a `requirements.txt` file in the root directory of the project with the following content:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    numpy>=1.20.0
    plotly>=5.0.0
    ```
    Then install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the prerequisites are installed, you can run the Streamlit application:

1.  **Navigate to the project directory (if not already there):**
    ```bash
    cd QuLab-EPS-Analyzer
    ```

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

3.  **Access the Application:**
    Your web browser will automatically open a new tab displaying the QuLab application, usually at `http://localhost:8501`.

### Basic Usage Instructions:

*   **Adjust Inputs**: Use the sliders and number input fields in the left sidebar to change financial parameters such as Net Income, Preferred Dividends, Weighted Average Shares Outstanding, Tax Rate, and details for Convertible Preferred Stock, Convertible Debt, and Stock Options.
*   **Observe Changes**: As you modify the inputs, the "Basic EPS" and "Diluted EPS" metrics will update in real-time in the main content area, along with the accompanying bar chart visualization.
*   **Explore Dilution**: Experiment with different values for the dilutive securities to understand their individual and combined impact on the company's EPS. Pay attention to how anti-dilution rules apply (e.g., stock options are only dilutive if the average market price is above the exercise price).

## Project Structure

The project is organized into the following main files:

```
QuLab-EPS-Analyzer/
├── app.py                  # Main Streamlit application entry point.
├── application.py          # Contains core logic, EPS calculation functions, and UI components.
└── requirements.txt        # Lists all Python dependencies required for the project.
```

*   `app.py`: Sets up the Streamlit page configuration, displays the main title, introduction, and calls the `run_application` function from `application.py` to render the interactive components.
*   `application.py`: Encapsulates the financial data generation, the `orchestrate_eps_calculation` function (which performs the actual EPS calculations including anti-dilution tests), and the `update_eps_display` function responsible for rendering the metrics and Plotly charts. It also defines the sidebar inputs and key insights/references.

## Technology Stack

*   **Python**: The core programming language used for the entire application.
*   **Streamlit**: The open-source app framework used for building the interactive web user interface.
*   **Pandas**: Utilized for basic data handling, specifically `pd.Series` for managing synthetic financial data.
*   **NumPy**: Used for numerical operations, particularly for generating synthetic data (`np.random`).
*   **Plotly**: Employed for creating interactive and customizable data visualizations (bar charts) to compare EPS values.

## Contributing

This project is primarily a lab demonstration. However, if you would like to contribute:

1.  **Fork** the repository.
2.  **Clone** your forked repository to your local machine.
3.  **Create a new branch** for your features or bug fixes: `git checkout -b feature/your-feature-name` or `bugfix/fix-description`.
4.  **Make your changes**.
5.  **Commit your changes** with a clear and concise message: `git commit -m "feat: Add new feature"`.
6.  **Push your branch** to your forked repository: `git push origin feature/your-feature-name`.
7.  **Open a Pull Request** to the main repository's `main` branch.

## License

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. Any reproduction or distribution of this demonstration requires prior written consent from QuantUniversity. This lab was generated using the QuCreate platform, which relies on AI models for generating code, and may contain inaccuracies or errors.

## Contact

For questions or inquiries regarding this project or QuantUniversity's educational platforms, please visit [QuantUniversity's Website](https://www.quantuniversity.com/).