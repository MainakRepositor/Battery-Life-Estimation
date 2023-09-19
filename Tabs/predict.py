"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regressor</b> for Battery Life Estimation.
            </p>
        """, unsafe_allow_html=True)
    k = 0.11
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A1 = st.slider("Top Speed (KmH)", float(df["TopSpeed_KmH"].min()), float(df["TopSpeed_KmH"].max()))
    A2 = st.slider("Range (Km)", float(df["Range_Km"].min()), float(df["Range_Km"].max()))
    A3 = st.slider("Efficiency (WhKm)", float(df["Efficiency_WhKm"].min()), float(df["Efficiency_WhKm"].max()))
    A4 = st.slider("FastCharge (KmH)", float(df["FastCharge_KmH"].min()), float(df["FastCharge_KmH"].max()))
    A5 = st.slider("Rapid Charge", float(df["RapidCharge"].min()), float(df["RapidCharge"].max()))
    A6 = st.slider("Power Train", float(df["PowerTrain"].min()), float(df["PowerTrain"].max()))
    A7 = st.slider("Plug Type", float(df["PlugType"].min()), float(df["PlugType"].max()))
    A8 = st.slider("Formation Energy", float(df["Formation_Energy"].min()), float(df["Formation_Energy"].max()))
    A9 = st.slider("Above Hull", float(df["Above_Hull"].min()), float(df["Above_Hull"].max()))
    A10 = st.slider("Band Gap", float(df["Band_Gap"].min()), float(df["Band_Gap"].max()))
    A11 = st.slider("Temp", float(df["Temp"].min()), float(df["Temp"].max()))
    A12 = st.slider("Density", float(df["Density"].min()), float(df["Density"].max()))
    A13 = st.slider("Volume", float(df["Volume"].min()), float(df["Volume"].max()))
    A14 = st.slider("Has Band structure", float(df["HasBandstructure"].min()), float(df["HasBandstructure"].max()))
    A15 = st.slider("Crystal System", float(df["Crystal_System"].min()), float(df["Crystal_System"].max()))
    A16 = st.slider("Discharge Time", float(df["Discharge_Time"].min()), float(df["Discharge_Time"].max()))
    A17 = st.slider("Decrement", float(df["Decrement"].min()), float(df["Decrement"].max()))
    A18 = st.slider("Max Voltage Discharging", float(df["Max_Voltage_Discharging"].min()), float(df["Max_Voltage_Discharging"].max()))
    A19 = st.slider("Min Voltage Charging", float(df["Min_Voltage_Charging"].min()), float(df["Min_Voltage_Charging"].max()))
    A20 = st.slider("Time constant current", float(df["Time_constant_current"].min()), float(df["Time_constant_current"].max()))
    A21 = st.slider("Charging time (in nano sec)", float(df["Charging_time"].min()), float(df["Charging_time"].max()))
   
    

    # Create a list to store all the features
    features = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Predicted Sucessfully")
        # Print the output according to the prediction
        st.success(str(round(prediction[0],2)) + " Days")
        
        # Print teh score of the model 
        st.write("The model used is trusted by engineers and has an accuracy of ", round((score*100),2),"%")
