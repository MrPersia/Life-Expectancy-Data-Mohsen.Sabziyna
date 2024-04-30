import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Laden des trainierten Random Forest-Modells
@st.cache(allow_output_mutation=True)
def load_model():
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Funktion zur Vorhersage der Lebenserwartung
def predict_life_expectancy(input_data):
    # Konvertierung der Eingabedaten in ein DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Kategorische Variablen mit LabelEncoder kodieren, falls erforderlich
    # Beispiel:
    # encoder = LabelEncoder()
    # input_df['CategoricalFeature'] = encoder.fit_transform(input_df['CategoricalFeature'])

    # Vorhersage machen
    rf_regressor = load_model()
    prediction = rf_regressor.predict(input_df)
    return prediction[0]

# Streamlit-Interface einrichten
st.title('Lebenserwartungs-Vorhersagemodell')
st.write('Bitte geben Sie die erforderlichen Informationen ein, um die Lebenserwartung vorherzusagen')

# Eingabefelder für jedes Feature erstellen
# Füge hier Eingabefelder für jedes Feature hinzu, das dein Modell verwendet. Beispiel:
age = st.number_input('Alter', min_value=0, max_value=120, value=30)
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=22.0)
# Füge weitere Eingabefelder gemäß deinem Datensatz hinzu

# Button zur Vorhersage
if st.button('Lebenserwartung vorhersagen'):
    input_data = {'Age': age, 'BMI': bmi}  # Füge hier alle deine Features hinzu
    prediction = predict_life_expectancy(input_data)
    st.write(f'Vorhergesagte Lebenserwartung: {prediction:.2f} Jahre')

# Denke daran, die Eingabefelder entsprechend den Features anzupassen, die dein Modell erfordert

