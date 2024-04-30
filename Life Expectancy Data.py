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

# Laden der Daten
data = pd.read_csv("Life Expectancy Data.csv")

# Eingabefelder für jedes Feature erstellen
input_data = {}
for column in data.columns:
    if data[column].dtype == 'object':
        input_data[column] = st.selectbox(f'Wähle {column}', data[column].unique())
    else:
        input_data[column] = st.number_input(f'Gib {column} ein', value=data[column].mean())

# Button zur Vorhersage
if st.button('Lebenserwartung vorhersagen'):
    prediction = predict_life_expectancy(input_data)
    st.write(f'Vorhergesagte Lebenserwartung: {prediction:.2f} Jahre')

# Denke daran, die Eingabefelder entsprechend den Features anzupassen, die dein Modell erfordert
