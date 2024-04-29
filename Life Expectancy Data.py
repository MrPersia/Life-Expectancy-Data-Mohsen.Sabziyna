import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize

# Daten einlesen
@st.cache
def load_data():
    return pd.read_csv("Life Expectancy Data.csv")

life_expectancy = load_data()

# Spalten umbenennen
life_expectancy.rename(columns={
    " BMI ": "BMI",
    "Life expectancy ": "Life_expectancy",
    "Adult Mortality": "Adult_mortality",
    "infant deaths": "Infant_deaths",
    "percentage expenditure": "Percentage_expenditure",
    "Hepatitis B": "HepatitisB",
    "Measles ": "Measles",
    "under-five deaths ": "Under_five_deaths",
    "Total expenditure": "Total_expenditure",
    "Diphtheria ": "Diphtheria",
    " thinness  1-19 years": "Thinness_1-19_years",
    " thinness 5-9 years": "Thinness_5-9_years",
    " HIV/AIDS": "HIV/AIDS",
    "Income composition of resources": "Income_composition_of_resources"
}, inplace=True)

# Berechnung der Lebenserwartung
def calculate_life_expectancy(features):
    # Berechnung der Lebenserwartung basierend auf ausgewählten Features
    # Hier kannst du deine Lebenserwartungsberechnung einfügen
    life_expectancy = np.random.randint(50, 90)
    return life_expectancy

# Streamlit-Anwendung
st.title('Lebenserwartungsberechnung')

# Benutzer-Inputs
st.sidebar.header('Eigenschaften auswählen')
features = {}
features['Adult Mortality'] = st.sidebar.slider('Adult Mortality', min_value=0, max_value=1000, value=500)
features['Infant Deaths'] = st.sidebar.slider('Infant Deaths', min_value=0, max_value=1000, value=50)
# Weitere Features hinzufügen...

# Berechnung der Lebenserwartung
if st.sidebar.button('Lebenserwartung berechnen'):
    life_exp = calculate_life_expectancy(features)
    st.success(f'Die geschätzte Lebenserwartung beträgt {life_exp} Jahre.')

# Daten anzeigen
st.subheader('Datenübersicht')
st.write(life_expectancy)
