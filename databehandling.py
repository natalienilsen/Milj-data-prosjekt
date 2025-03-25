import pandas as pd
import os

#--------------------------
#---BESKRIVELSE AV KODEN---
#--------------------------

#Denne koden svarer på oppgave 3 i mappe del 1. Målet er å klargjøre alle dataene for analyse og visualisering. 



#------------------------------------------------------
#---BESTM HVILKEN FIL MED RÅDATA SOM SKAL FINSKRIVES---
#------------------------------------------------------

filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/luftkvalitet_nilu.csv"
#OBS, må være csv!


#----------------------------------------------------------
#---SJEKKER FOR IKKE-EKSISTERENDE VERDIER OG NULLVERDIER---
#----------------------------------------------------------
def check_missing_and_zero(df):
    print("\n🔍 Sjekker etter manglende verdier (NaN):")
    print(df.isna().sum())
    print("\n🔍 Sjekker etter null-verdier (0):")
    print((df == 0).sum())
    
def check_NaN_and_zero(filepath):
    if not os.path.exists(filepath):
        print("Fant ikke filen :(")
    else:
        df = pd.read_csv(filepath)


#--------------------------
#---RENSER DATAINNHOLDET---
#--------------------------
def clean_data(df):
    """Fjerner duplikater og uregelmessige verdier"""
    # Fjern duplikater
    df = df.drop_duplicates()

    # Fjern rader med NaN
    df = df.dropna()

    # Fjern rader med AQI = -9999 eller AQI <= 0
    df = df[df['AQI'] > 0]
    df = df[df['AQI'] != -9999]

    return df

#-----------------------------
#---STANDARISERER KOLONNENE---
#-----------------------------
#****Denne er ikke riktig****#
def standardize_columns(df):
    """Standardiserer kolonnenavn til engelsk og snake_case"""
    df = df.rename(columns={
        "By": "city",
        "AQI": "aqi",
        "Kategori": "category",
        "Dominerende forurensning": "main_pollutant"
    })
    return df


#--------------------------------------
#---LAGRER RENSET DATA I EN NY MAPPE---
#--------------------------------------
def save_cleaned_data(df, output_path="data/clean/luftkvalitet_nilu.csv"):
    """Lagrer renset og formatert data til ny CSV-fil"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n✅ Renset data lagret til: {output_path}")


#---------------------
#---HOVEDPROGRAMMET---
#---------------------
input_fil = filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/luftkvalitet_nilu.csv"

def behandle_data(input_fil):
    """Hovedfunksjon for å kjøre alle stegene"""
    print("📥 Leser inn data...")
    df = load_data(input_fil)

    check_missing_and_zero(df)

    print("\n🧹 Rydder og renser data...")
    df = clean_data(df)

    print("\n🔠 Standardiserer kolonnenavn...")
    df = standardize_columns(df)

    save_cleaned_data(df)

    print("\n🚀 Data er klar for analyse og visualisering!")


# Kjør kun hvis filen kjøres direkte
if __name__ == "__main__":
    behandle_data("data/luftkvalitet_nilu.csv")
