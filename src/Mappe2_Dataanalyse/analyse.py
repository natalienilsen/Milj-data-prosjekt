import os
import pandas as pd

# Funksjon som finner en brukbar AQI-representant
def finn_aqi_kolonne(df):
    for kandidat in ["aqi", "AQI", "pm10", "PM10", "pm2_5", "PM2_5"]:
        if kandidat in df.columns:
            return kandidat
    return None

#Funksjon som returnerer forklarende tekst til hver statistikk
def tolkning(stikkord):
    return {
        "Gjennomsnitt": "Gjennomsnittlig luftkvalitet",
        "Median": "50 % av verdiene er lavere/høyere",
        "Standardavvik": "Variasjon i verdiene"
    }.get(stikkord, "")

#Lagrer statistikken til CSV
def lagre_statistikk_csv(gjennomsnitt, median, std, kolonne, kilde, filsti):
    data = pd.DataFrame({
        "Statistikk": ["Gjennomsnitt", "Median", "Standardavvik"],
        "Verdi": [round(gjennomsnitt, 2), round(median, 2), round(std, 2)],
        "Kolonne brukt": [kolonne] * 3,
        "Kilde": [kilde] * 3,
        "Tolkning": [tolkning(k) for k in ["Gjennomsnitt", "Median", "Standardavvik"]]
    })
    data.to_csv(filsti, index=False)
    print(f"📁 Lagret: {filsti}")

##########################
### 1: Google API-data ###
##########################

google_path = "data/clean/luftkvalitet_google_clean.csv"

if os.path.exists(google_path):
    print(f"\n📘 Leser Google API-data: {google_path}")
    df_google = pd.read_csv(google_path)
    df_google.columns = df_google.columns.str.upper()

    kol = finn_aqi_kolonne(df_google)
    if kol:
       