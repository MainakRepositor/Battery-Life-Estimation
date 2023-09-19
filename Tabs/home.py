"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Battery Life Estimation System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
           A battery life detection system employing AI utilizes machine learning algorithms to monitor and predict the remaining battery capacity of devices. It continuously collects data on power usage patterns, environmental conditions, and charge-discharge cycles, and employs predictive models to estimate battery health. By analyzing historical and real-time data, the system can provide accurate forecasts of remaining battery life, enabling users to plan device usage efficiently and avoid unexpected shutdowns. This AI-driven solution enhances user experience, optimizes power management, and extends the lifespan of batteries, contributing to sustainability and improved reliability across various applications, from smartphones to electric vehicles.
        </p>
    """, unsafe_allow_html=True)
