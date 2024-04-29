import streamlit as st
import pandas as pd
import numpy as np

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

# Winsorization
cols_to_winsorize = [
    'Life_expectancy', 'Adult_mortality', 'Alcohol', 'HepatitisB', 'Polio',
    'Total_expenditure', 'Diphtheria', 'HIV/AIDS', 'Thinness_1-19_years',
    'Thinness_5-9_years', 'Income_composition_of_resources', 'Schooling'
]
for col in cols_to_winsorize:
    life_expectancy[f'winz_{col}'] = winsorize(life_expectancy[col], (0.05, 0))

# Streamlit-Anwendung
st.title('Lebenserwartungsberechnung')

# Benutzer-Inputs
st.sidebar.header('Eigenschaften auswählen')
adult_mortality = st.sidebar.slider('Adult Mortality', min_value=int(life_expectancy['Adult_mortality'].min()), 
                                    max_value=int(life_expectancy['Adult_mortality'].max()), value=int(life_expectancy['Adult_mortality'].mean()))
infant_deaths = st.sidebar.slider('Infant Deaths', min_value=int(life_expectancy['Infant_deaths'].min()), 
                                    max_value=int(life_expectancy['Infant_deaths'].max()), value=int(life_expectancy['Infant_deaths'].mean()))

# Lebenserwartung berechnen
def calculate_life_expectancy(adult_mortality, infant_deaths):
    # Hier kann die Lebenserwartungsberechnung basierend auf den Benutzereingaben erfolgen
    life_expectancy = 80 - adult_mortality / 100 - infant_deaths / 100
    return life_expectancy

# Berechnung der Lebenserwartung
if st.sidebar.button('Lebenserwartung berechnen'):
    life_exp = calculate_life_expectancy(adult_mortality, infant_deaths)
    st.success(f'Die geschätzte Lebenserwartung beträgt etwa {life_exp:.2f} Jahre.')

# Daten anzeigen
st.subheader('Datenübersicht')
st.write(life_expectancy)
