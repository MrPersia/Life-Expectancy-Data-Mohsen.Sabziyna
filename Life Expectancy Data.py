import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Laden der Daten
@st.cache
def load_data():
    data = pd.read_csv("Life Expectancy Data.csv")
    return data

data = load_data()

# Features und Zielvariable
X = data.drop(['Life expectancy '], axis=1)
y = data['Life expectancy ']

# Modell initialisieren und trainieren
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X, y)

# Funktion zur Vorhersage der Lebenserwartung
def predict_life_expectancy(input_data):
    # Konvertierung der Eingabedaten in ein DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Vorhersage machen
    prediction = rf_regressor.predict(input_df)
    return prediction[0]

# Streamlit-Interface einrichten
st.title('Lebenserwartungs-Vorhersagemodell')
st.write('Bitte geben Sie die erforderlichen Informationen ein, um die Lebenserwartung vorherzusagen')

# Eingabefelder für jedes Feature erstellen
input_data = {}
for column in X.columns:
    if X[column].dtype == 'object':
        input_data[column] = st.selectbox(f'Wähle {column}', X[column].unique())
    else:
        input_data[column] = st.number_input(f'Gib {column} ein', value=X[column].mean())

# Button zur Vorhersage
if st.button('Lebenserwartung vorhersagen'):
    prediction = predict_life_expectancy(input_data)
    st.write(f'Vorhergesagte Lebenserwartung: {prediction:.2f} Jahre')
