import streamlit as st
import pickle
import pandas as pd

# Load the model from the file
pickle_file = "housing_model.pkl"
with open(pickle_file, 'rb') as file:
    model = pickle.load(file)

# Define function for making predictions
def make_prediction(input_data):
    data = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(data)
    return prediction[0]

# Streamlit app
st.title('Housing Price Prediction')

# User inputs
mainroad = st.selectbox('Mainroad', ['yes', 'no'])
guestroom = st.selectbox('Guestroom', ['yes', 'no'])
basement = st.selectbox('Basement', ['yes', 'no'])
hotwaterheating = st.selectbox('Hotwaterheating', ['yes', 'no'])
airconditioning = st.selectbox('Airconditioning', ['yes', 'no'])
parking = st.number_input('Parking', min_value=0, max_value=5, step=1)
prefarea = st.selectbox('Prefarea', ['yes', 'no'])
furnishingstatus = st.selectbox('Furnishingstatus', ['furnished', 'semi-furnished', 'unfurnished'])
# New inputs for additional columns
bathrooms = st.number_input('Bathrooms', min_value=0, max_value=10, step=1)
stories = st.number_input('Stories', min_value=0, max_value=5, step=1)
area = st.number_input('Area', min_value=0)
bedrooms = st.number_input('Bedrooms', min_value=0, max_value=10, step=1)

input_data = {
    'mainroad': mainroad,
    'guestroom': guestroom,
    'basement': basement,
    'hotwaterheating': hotwaterheating,
    'airconditioning': airconditioning,
    'parking': parking,
    'prefarea': prefarea,
    'furnishingstatus': furnishingstatus,
    'bathrooms': bathrooms,
    'stories': stories,
    'area': area,
    'bedrooms': bedrooms,
}

# Make prediction when button is clicked
if st.button('Predict'):
    prediction = make_prediction(input_data)
    st.write(f'Predicted Price: ₹{prediction}')


