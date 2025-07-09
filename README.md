
# EPS Calculator - Streamlit Application

This Streamlit application provides an interactive tool for understanding and calculating Earnings Per Share (EPS), including the impact of potentially dilutive securities.

## Overview

The application allows users to input key financial data, such as net income, preferred dividends, and weighted average shares outstanding, and then explore the effects of convertible preferred stock, convertible debt, and stock options on the diluted EPS.

## Features

-   Interactive input of financial data.
-   Calculation of Basic EPS and Diluted EPS.
-   Scenario analysis to visualize the impact of changing key variables on Diluted EPS.
-   Clear and concise display of results and visualizations using Plotly.

## Getting Started

To run this application, you need to have Python and Docker installed.

### Running with Docker

1.  Clone the repository.
2.  Build the Docker image:

    ```bash
    docker build -t eps-calculator .
    ```

3.  Run the Docker container:

    ```bash
    docker run -p 8501:8501 eps-calculator
    ```

4.  Open your web browser and go to `http://localhost:8501`.

### Running Locally

1.  Clone the repository.
2.  Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

5.  Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Libraries

-   Streamlit
-   Pandas
-   Plotly
-   NumPy
