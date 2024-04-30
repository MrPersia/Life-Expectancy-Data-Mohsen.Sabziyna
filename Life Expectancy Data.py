import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import IterativeImputer

# Daten laden und vorverarbeiten
@st.cache
def load_data():
    data = pd.read_csv("Life Expectancy Data.csv")

    # Numerische Spalten imputieren
    numerical_columns = data.select_dtypes(include=['number']).columns
    imputer = IterativeImputer()
    data_imputed = data.copy() 
    data_imputed[numerical_columns] = imputer.fit_transform(data[numerical_columns])

    return data_imputed

data = load_data()

# Feature- und Zielvariablen definieren
X = data.drop(['Life expectancy '], axis=1)
y = data['Life expectancy ']

# Kategorische Variablen kodieren
label_encoder = LabelEncoder()
for column in X.select_dtypes(include=['object']).columns:
    X[column] = label_encoder.fit_transform(X[column])

# Skalierung der Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modell laden
@st.cache(allow_output_mutation=True)
def load_model():
    model = RandomForestRegressor(random_state=42)
    model.fit(X_scaled, y)
    return model

model = load_model()

# Streamlit App
st.title("Lebenserwartung Vorhersage")

# Eingabeformular für Features
inputs = {}
for feature in X.columns:
    inputs[feature] = st.number_input(f"{feature}", value=X[feature].mean())

# Vorhersage machen
input_data = pd.DataFrame([inputs])
input_data_scaled = scaler.transform(input_data)
prediction = model.predict(input_data_scaled)

# Ergebnis anzeigen
st.subheader("Vorhergesagte Lebenserwartung:")
st.write(prediction[0])
