import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def clean_luftkvalitet_data(df):
    
    df = pd.read_csv('/Users/vildevikane/Desktop/Milj-data-prosjekt/data/raw/luftkvalitet_test.csv')
    
    # Lager en kopi for å unngå å endre orginalen
    df_clean = df.copy()

    # Konverterer kolonnenavn til lowercase og fjerner mellomrom
    df_clean.columns = df_clean.columns.str.lower().str.strip()

    # Håndterer manglende verdier
    # Erstatter tomme strings og "null" med NaN
    df_clean = df_clean.replace(['', 'null', 'NA', 'N/A'], np.nan)

    # Renser AQI-kolonner
    if 'aqi' in df_clean.columns:

        # Fjerner ikke-numeriske verdier og tvinger feil til NaN
        df_clean['aqi'] = pd.to_numeric(df_clean['aqi'],errors = 'coerce')

        # Fjerner ugylige AQI-verdier (AQI <0 eller AQI > 500)
        df_clean.loc[~df_clean['aqi'].between(0, 500), 'aqi'] = np.nan

    # Renser bynavn
    if 'city' in df_clean.columns:
        # Konverterer til store bokstaver for bynavn og fjerner mellomrom 
        df_clean['city'] = df_clean['city'].str.strip().str.title()

    # Renser kategori kolonner
    if 'category' in df_clean.columns:

        # Standardiserer air quality kategorier
        category_mapping = {
            'excellent': 'Excellent air quality',
            'good': 'Good air quality',
            'moderate': 'Moderate air quality',
            'poor': 'Poor air quality',
            'very poor': 'Very poor air quality',
            'severe': 'Severe air quality',
        }

        df_clean['category'] = df_clean['category'].str.lower().map(category_mapping)

        # Rens main_pollutant column
        if 'main_pollutant' in df_clean.columns:

            # Standardiserer forurensingsnavene
            df_clean['main_pollutant'] = df_clean['main_pollutant'].str.lower()
        
        # Fjern rader hvor alle verdier mangler
        df_clean = df_clean.dropna(how = 'all')

        return df_clean
    
def validate_luftkvalitet_data(df):
    # Validerer renset luftkvalitetsdata og returnerer en endelig rapport
    validation_report = {
        'missing_values': df.isnull().sum().to_dict(),
        'unique_categories': df['category'].unique().tolist() if 'category' in df.columns else [],
        'unique_pollutants': df['main_pollutant '].unique().tolist() if 'main_pollutant' in df.columns else [],
        'aqi_stats': df['aqi'].describe().to_dict() if 'aqi' in df.columns else {},
        'row_count': len(df)
        }
    
    return validation_report 
    
def process_luftkvalitet_data(filepath):
    # Behandle luftkvalitetsdata fra CSV-fil

    # Lese CSV-filen
    df = pd.read_csv(filepath)

    # Rense dataen
    cleaned_df = clean_luftkvalitet_data(df)

    # Validerer den rensede dataen
    validation_report = validate_luftkvalitet_data(cleaned_df)

    return cleaned_df, validation_report
    
# Tester koden:
file_path = '/Users/vildevikane/Desktop/Milj-data-prosjekt/data/raw/luftkvalitet_test.csv'
cleaned_data, report = process_luftkvalitet_data(file_path)

# Se rapporten
print("Validation report:")
print(report)

# Se den rensede dataen
print("\nCleaned Data:")
print (cleaned_data.head())

# Denne koden gir 3 hovedfunksjoner:

# 1. clean_air_quality_data(): Denne funksjonen:
# - Standardiserer kolonnenavn
# - Håndterer manglende verdier
# - Renser og validerer AQI verdier
# - Standardiserer bynavn og kategorier
# - Renser forurensingsnavn
# - Fjerner tomme rader 

# 2. validate_air_quality_data(): Denne funskjonen lager en rapport som består av: 
# - Antall manglende verdier per kolonne
# - Unike kategorier og forurensinger 
# - Basic statistikk for AQI verdier
# - Totalt antall rader

# 3. process_luftkvalitet_data(): Funksjonen kombinerer trinnene for rensing og validering:
