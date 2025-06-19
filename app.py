import streamlit as st
import joblib  # or use pickle if needed
import numpy as np

# Load the trained model
reg = joblib.load('house_price_model.pkl')

# App title
st.title("🏠 House Price Prediction App")

# Input fields (example features — replace with your actual ones)
area = st.number_input("Enter the area in square feet", min_value=100)


# Predict button
if st.button("Predict Price"):
    # Make prediction
    input_data = np.array([[area, bedrooms, bathrooms]])  # Update with your model’s input format
    prediction = reg.predict(input_data)[0]



