import requests
import pandas as pd
import time
from datetime import datetime, timedelta


# --- HVORDAN BRUKE DENNE FILEN ---
#1. Endre city, lat og lon til ønsket by
#2. Sett inn din API-nøkkel i API_key
#3. Kjør filen
#4. Dataen lagres til en unik fil per by


# --- SETT BYINFORMASJON HER ---
city = "Tallinn"
lat = 59.43696 #breddegrad
lon = 24.75353 #lengdegrad

# --- API-NØKKEL ---
API_key = "d01166dee6e6b98d1e4cf86e314c721b"

# --- TIDSPERIODE: 5 SISTE DAGER ---
#Fra OpenWeather kan vi bare hente ut for max 5 dager når vi har gratis API-nøkkel. 
end_time = int(time.time())
start_time = int((datetime.utcnow() - timedelta(days=5)).timestamp())

# --- URL ---
url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start_time}&end={end_time}&appid={API_key}"

# --- API-KALL ---
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # --- BEARBEIDER DATA ---
    records = []
    for entry in data["list"]:
        dt = datetime.utcfromtimestamp(entry["dt"])
        components = entry["components"]
        components["datetime"] = dt
        records.append(components)

    df = pd.DataFrame(records)

    # --- LAGRE FIL ---
    safe_city = city.lower().replace(" ", "_")
    file_path = f"data/raw/byer/{safe_city}_air_quality.csv"
    df.to_csv(file_path, index=False)

    print(f"Data for {city} lagret til: {file_path}")
    print(df.head())

else:
    print(f"API-feil ({response.status_code}): Klarte ikke å hente data for {city}")

