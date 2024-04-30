import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained Random Forest model
with open('random_forest_model.pkl', 'rb') as file:
    rf_regressor = pickle.load(file)

def predict_life_expectancy(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # If you have categorical variables, encode them using LabelEncoder or OneHotEncoder
    # Example:
    # encoder = LabelEncoder()
    # input_df['CategoricalFeature'] = encoder.fit_transform(input_df['CategoricalFeature'])

    # Make prediction
    prediction = rf_regressor.predict(input_df)
    return prediction[0]

# Set up Streamlit interface
st.title('Life Expectancy Prediction Model')
st.write('Please enter the required fields to predict the life expectancy')

# Create inputs for each feature
# Here you need to add inputs for each feature your model uses. Example:
age = st.number_input('Age', min_value=0, max_value=120, value=30)
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=22.0)
# Add more inputs as per your dataset

# Button to make prediction
if st.button('Predict Life Expectancy'):
    input_data = {'Age': age, 'BMI': bmi}  # Add all your features here
    prediction = predict_life_expectancy(input_data)
    st.write(f'Predicted Life Expectancy: {prediction:.2f} years')

# Remember to adjust inputs according to the features your model requires
