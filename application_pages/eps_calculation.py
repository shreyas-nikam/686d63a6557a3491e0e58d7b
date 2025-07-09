
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def run_eps_calculation():
    st.header("EPS Calculation")

    # Input Widgets
    net_income = st.number_input("Net Income", value=1000000.0, step=10000.0)
    preferred_dividends = st.number_input("Preferred Dividends", value=0.0, step=1000.0)
    waso = st.number_input("Weighted Average Shares Outstanding", value=1000000.0, step=10000.0)
    tax_rate = st.slider("Tax Rate", min_value=0.0, max_value=1.0, value=0.25, step=0.01)

    #Calculations
    basic_eps = (net_income - preferred_dividends) / waso if waso >0 else 0

    # Display Results
    st.subheader("Calculated EPS Values")
    st.metric("Basic EPS", value=f"{basic_eps:.2f}")

    # Visualization
    fig = go.Figure(data=[go.Bar(x=["Basic EPS"], y=[basic_eps])])
    fig.update_layout(title="Basic EPS", yaxis_title="EPS ($)")
    st.plotly_chart(fig)

