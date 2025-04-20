import requests
import json
import pandas as pd
import matplotlib.pyplot as plt


#######################################
#Kode for å hente data fra Google Cloud
#######################################

#API-nøkkelen for Google Air Quality API
API_KEY = "AIzaSyA7SlToh7FabjrK6xORJTH2SsNmTj52rSA"  # ← husk å bytte!

#De utvalgte byene og deres geografiske koordinater
cities = {
    "London": (51.5074, -0.1278),
    "Paris": (48.8566, 2.3522),
    "Oslo": (59.9139, 10.7522),
    "Amsterdam": (52.3676, 4.9041),
    "København": (55.6761, 12.5683),
    "Berlin": (52.5200, 13.4050),
    "Moskva": (55.7558, 37.6176),
    "Madrid": (40.4168, -3.7038),
    "Ankara": (39.9208, 32.8541),
    "Roma": (41.9028, 12.4964)
}

#URL for API-kall
url = f"https://airquality.googleapis.com/v1/currentConditions:lookup?key={API_KEY}"

#Liste som samler resultatene
results = []

#for-løkke som går gjennom hver by og henter dataene
for city, (lat, lon) in cities.items():
    payload = {"location": {"latitude": lat, "longitude": lon}}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        index = data["indexes"][0]
        results.append({
            "By": city,
            "AQI": index["aqi"],
            "Kategori": index["category"],
            "Dominerende forurensning": index["dominantPollutant"]
        })
    else:
        print(f"❌ Feil for {city}: {response.status_code}")
        results.append({
            "By": city,
            "AQI": None,
            "Kategori": "Feil",
            "Dominerende forurensning": "-"
        })

#Lager en DataFrame som lagrer verdiene i en CSV-fil
df_google = pd.DataFrame(results)
print(df_google)

df_google.to_csv("luftkvalitet_byer.csv", index=False)




df_google = pd.DataFrame(results)

#Farger basert på AQI-kategori
farger = df_google["Kategori"].map({
    "Good air quality": "green",
    "Moderate air quality": "orange",
    "Unhealthy for sensitive groups": "red",
    "Unhealthy": "darkred",
    "Very unhealthy": "purple",
    "Hazardous": "black",
    "Feil": "gray"
})

#Lager et søylediagram for visualisering
plt.figure(figsize=(10, 6))
bars = plt.bar(df_google["By"], df_google["AQI"], color=farger)

#Legger på AQI-verdier
for bar in bars:
    yval = bar.get_height()
    if yval:  # hvis ikke None
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

#Legger til dominerende forurensning
for bar, pollutant in zip(bars, df_google["Dominerende forurensning"]):
    if bar.get_height():
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, pollutant,
                 ha='center', va='bottom', fontsize=8, color='gray')


plt.title("Luftkvalitet (AQI) i europeiske storbyer")
plt.ylabel("AQI (Air Quality Index)")
plt.ylim(0, max(df_google["AQI"].dropna()) + 20)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

