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

# Custom CSS for styling
st.set_page_config(page_title='Housing Price Prediction', page_icon='🏠', layout='wide')
st.markdown("""
    <style>
    .main {
        background-color: #31383B;
    }
    .sidebar .sidebar-content {
        background-color: #4b6cb7;
        color: white;
    }
    .stButton>button {
        background-color: #BBE70F;
        color: white;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #000000;
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app

st.title('🏠 Housing Price Prediction')
st.markdown("""
    <div style='text-align: center; color: #FFFFFF; font-size: 24px;'>
        Welcome to the Housing Price Prediction website!
    </div>
""", unsafe_allow_html=True)

# Use columns for a better layout
col1, col2 = st.columns(2)

with col1:
    mainroad = st.selectbox('House situated near the Mainroad', ['yes', 'no'])
    guestroom = st.selectbox('House containing a Guestroom', ['yes', 'no'])
    basement = st.selectbox('House containing a Basement', ['yes', 'no'])
    hotwaterheating = st.selectbox('Hotwaterheating provisions', ['yes', 'no'])
    airconditioning = st.selectbox('Airconditioning provisions', ['yes', 'no'])
    parking = st.number_input('no. of Parking spots', min_value=0, max_value=5, step=1)

with col2:
    prefarea = st.selectbox('Is the house in your preferred area? ', ['yes', 'no'])
    furnishingstatus = st.selectbox('Furnishing status of the house', ['furnished', 'semi-furnished', 'unfurnished'])
    bathrooms = st.number_input('no of Bathrooms', min_value=0, max_value=10, step=1)
    stories = st.number_input('no of Stories', min_value=0, max_value=5, step=1)
    area = st.number_input('Area in sqft', min_value=0)
    bedrooms = st.number_input('no of Bedrooms', min_value=0, max_value=10, step=1)

input_data = {
    'House situated near the Mainroad': mainroad,
    'House containing a Guestroom': guestroom,
    'House containing a Basement': basement,
    'Hot water heating provisions': hotwaterheating,
    'Airconditioning provisions': airconditioning,
    'no. of Parking spots': parking,
    'Is the house in your preferred area?': prefarea,
    'Furnishing status of the house': furnishingstatus,
    'no of Bathrooms': bathrooms,
    'no of Stories': stories,
    'Area in sqft': area,
    'no of Bedrooms': bedrooms,
}

# Make prediction when button is clicked
if st.button('Predict'):
    prediction = make_prediction(input_data)
    st.success(f'🏡 Predicted Price: ₹{prediction}')

# Add a sidebar
st.sidebar.title("About")
st.sidebar.info("This app uses a machine learning model to predict the price of a house based on various features provided by the user. It was built using Streamlit. --This app aims to simplify prediction of House prices, with various set questions to narrow down your personalized choice")
st.sidebar.info
# Add a footer
st.markdown("""
    <div class="footer">
        <p>Developed by Abhinav. © 2024</p>
    </div>
    """, unsafe_allow_html=True)




 
