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
        df_google = df_google.dropna(subset=[kol])
        avg = df_google[kol].mean()
        median = df_google[kol].median()
        std = df_google[kol].std()

        print(f"🔹 Google API – Kolonne brukt: {kol}")
        print(f"Gjennomsnitt: {avg:.2f}, Median: {median:.2f}, Standardavvik: {std:.2f}")
        lagre_statistikk_csv(avg, median, std, kol, "Google API", "data/outputs/statistikk_google.csv")
    else:
        print("❌ Fant ingen AQI/PM10/PM2_5 i Google-data")
else:
    print(f"❌ Fant ikke Google-data: {google_path}")


###########################
### 1: OpenWeather-data ###
###########################

openweather_dir = "data/clean/byer"
openweather_summary = []

if os.path.exists(openweather_dir):
    print(f"\n🌍 Leser OpenWeather-filer i: {openweather_dir}")
    for file in os.listdir(openweather_dir):
        if file.endswith("_clean.csv"):
            city = file.replace("_clean.csv", "").capitalize()
            path = os.path.join(openweather_dir, file)
            df = pd.read_csv(path)
            kol = finn_aqi_kolonne(df)

            if kol:
                df = df.dropna(subset=[kol])
                avg = df[kol].mean()
                median = df[kol].median()
                std = df[kol].std()

                openweather_summary.append({
                    "By": city,
                    "Gjennomsnitt": round(avg, 2),
                    "Median": round(median, 2),
                    "Standardavvik": round(std, 2),
                    "Kolonne brukt": kol
                })
            else:
                print(f"⚠️ {city}: Fant ingen AQI/PM10/PM2_5 – hopper over.")

    if openweather_summary:
        df_open = pd.DataFrame(openweather_summary)
        print("🔹 OpenWeather – Statistikk per by:")
        print(df_open)
        df_open.to_csv("data/outputs/Mappe2_Statistikk/statistikk_openweather.csv", index=False)
    else:
        print("⚠️ Ingen byer med gyldig AQI-data funnet.")
else:
    print(f"❌ Fant ikke mappe: {openweather_dir}")


# -------------------------------
# 🇳🇴 3: NILU-data (kun Oslo, PM2.5)
# -------------------------------

nilu_path = "data/clean/luftkvalitet_nilu_clean.csv"

if os.path.exists(nilu_path):
    print(f"\n🇳🇴 Leser NILU-data: {nilu_path}")
    df_nilu = pd.read_csv(nilu_path)
    df_nilu.columns = df_nilu.columns.str.lower()

    # Filtrer til Oslo og PM2.5
    df_oslo = df_nilu[
        (df_nilu["municipality"].str.lower() == "oslo") &
        (df_nilu["component"].str.lower() == "pm2.5")
    ]

    if not df_oslo.empty:
        df_oslo = df_oslo.dropna(subset=["value"])
        avg = df_oslo["value"].mean()
        median = df_oslo["value"].median()
        std = df_oslo["value"].std()

        print(f"🔹 NILU Oslo – Komponent: PM2.5")
        print(f"Gjennomsnitt: {avg:.2f}, Median: {median:.2f}, Standardavvik: {std:.2f}")

        lagre_statistikk_csv(
            avg, median, std,
            kolonne="value",
            kilde="NILU (Oslo, PM2.5)",
            filsti="data/outputs/Mappe2_Statistikk/statistikk_nilu.csv"
        )
    else:
        print("❌ Fant ingen rader for Oslo med PM2.5")
else:
    print(f"❌ Fant ikke NILU-data: {nilu_path}")
