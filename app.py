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
st.set_page_config(page_title='Housing Price Prediction', page_icon='🏠', layout='wide')
st.title('🏠 Housing Price Prediction')
st.markdown("Welcome to the Housing Price Prediction app. Please provide the following details to get the estimated price of the house.")

# Use columns for a better layout
col1, col2 = st.columns(2)

with col1:
    mainroad = st.selectbox('Mainroad', ['yes', 'no'])
    guestroom = st.selectbox('Guestroom', ['yes', 'no'])
    basement = st.selectbox('Basement', ['yes', 'no'])
    hotwaterheating = st.selectbox('Hotwaterheating', ['yes', 'no'])
    airconditioning = st.selectbox('Airconditioning', ['yes', 'no'])
    parking = st.number_input('Parking', min_value=0, max_value=5, step=1)

with col2:
    prefarea = st.selectbox('Prefarea', ['yes', 'no'])
    furnishingstatus = st.selectbox('Furnishingstatus', ['furnished', 'semi-furnished', 'unfurnished'])
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
    st.success(f'🏡 Predicted Price: ₹{prediction}')

# Add a sidebar
st.sidebar.title("About")
st.sidebar.info("This app uses a machine learning model to predict the price of a house based on various features provided by the user. It was built using Streamlit.")

# Add a footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed by Your Name. © 2024</p>
    </div>
    """, unsafe_allow_html=True)



