import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#--------------------------
#---BESKRIVELSE AV KODEN---
#--------------------------

#Denne koden svarer på oppgave 3 i mappe del 1. Målet er å klargjøre alle dataene for analyse og visualisering. 

#----------------------------------------------------------
#---SJEKKER FOR IKKE-EKSISTERENDE VERDIER OG NULLVERDIER---
#----------------------------------------------------------

def check_odd_values(filepath):
    if not os.path.exists(filepath):
        print("Filen finnes ikke.")
        return

    df = pd.read_csv(filepath)

    #NaN-sjekk
    print("Antall NaN-verdier pr kolonne: ")
    print(df.isna().sum()) #isna() gir en bool på om det finnes NaN, sum() gir antallet bool, True for hver kolonne

    #0-verdi-sjekk
    print("\nSjekker etter null-verdier (0):")
    print((df == 0).sum())
    
    #Duplikater
    number_duplicates = df.duplicated().sum()
    print(f"Duplikater i datasettet: {number_duplicates} rader")

    #Ulogiske verdier (-9999, AQI >= 0, eller veldig høyt)
    if "AQI" in df.columns: 
        print("Ulogiske AQI-verdier: ")
        odd_values_AQI = df[(df["AQI"] <= 0) | (df["AQI"] == -9999) | (df["AQI"] > 500)]
        print(odd_values_AQI)
    else: 
        print("Filen inneholder ikke AQI.")


#--------------------------------------------------------------
#---RENSER DATAINNHOLDET OG LAGRER RENSET DATA I EN NY MAPPE---
#--------------------------------------------------------------

def clean_and_save_data(filepath, save_to):
        #Leser inn filen: dette kan kanskje gjøres om til en egen funksjon
    if not os.path.exists(filepath):
        print("Fant ikke filen :(")
    else:
        df = pd.read_csv(filepath)
    
    print("Renser filen")
    
    #Fjerner rader med manglende verdier. 
    df = df.dropna()
    
    # Konverterer kolonnenavn til lowercase og fjerner mellomrom
    df.columns = df.columns.str.lower().str.strip()

    
    #Fjerner duplikater
    df = df.drop_duplicates()
    
    #Fjerner rare verdier
    if "AQI" in df.columns:
        df = df[df["AQI"] != -999] #beholder alle verdier som ikke er -999
        df = df[df["AQI"] > 0] #beholder alle verdier som er over 0
        df = df[df["AQI"] <= 500] #beholder alle verdier som er under/lik 500
      
    #Standariserer kolonnenavn
    df.columns = df.columns.str.lower().str.strip()
        
    # Renser bynavn
    if 'city' in df.columns:
        # Konverterer til store bokstaver for bynavn og fjerner mellomrom 
        df['city'] = df['city'].str.strip().str.title()
        
    # Renser kategori kolonner
    if 'category' in df.columns:

        # Standardiserer air quality kategorier
        category_mapping = {
            'excellent': 'Excellent air quality',
            'good': 'Good air quality',
            'moderate': 'Moderate air quality',
            'poor': 'Poor air quality',
            'very poor': 'Very poor air quality',
            'severe': 'Severe air quality',
        }

        df['category'] = df['category'].str.lower().map(category_mapping)

        # Rens main_pollutant column
        if 'main_pollutant' in df.columns:

            # Standardiserer forurensingsnavene
            df['main_pollutant'] = df['main_pollutant'].str.lower()
            
    # Lagrer renset data til ny fil
    dirpath = os.path.dirname(save_to)
    if dirpath:  # unngå feil hvis det ikke er noen mappe i filnavnet
        os.makedirs(dirpath, exist_ok=True)
    df.to_csv(save_to, index=False)
    print(f"Renset data lagret til: {save_to}\n")
    
    
#-----------------------------------------------------------
#---Validerer den rensede dataen og returnerer en rapport---
#-----------------------------------------------------------

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

#---------------------
#---HOVEDPROGRAMMET---
#---------------------        
        
if __name__ == "__main__":    
    # 1.Velg hvilken fil med rådata som skal renses
    filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/raw/gjennomsnitt_by_forurensning.csv"
    
    # 2.Sjekker feil
    check_odd_values(filepath)

    # 3.Spør etter nytt filnavn til den rensede filen
    new_file_name = input("Hva ønsker du at den nye, rensede filen skal hete? (f.eks. 'data/clean/luftkvalitet_clean.csv'): NB! Husk å skriv data/clean/ ")
    print("Du skrev:", new_file_name)
    
    # 4. Validerer den rensede dataen
    #validation_report = validate_luftkvalitet_data(filepath)

    # 5.Rens og lagre i ny mappe: /data/clean
    clean_and_save_data(filepath, new_file_name)
