import requests
import json
import pandas as pd
import matplotlib.pyplot as plt



# NILU API endpoint
url = "https://api.nilu.no/aq/utd"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Convert JSON data to DataFrame
    df_nilu = pd.DataFrame(data)
    
    # Save DataFrame to CSV
    df_nilu.to_csv("luftkvalitet_nilu.csv", index=False)
    
    print("Luftkvalitetsdata lagret i luftkvalitet_nilu.csv")
else:
    print(f"Feil ved henting av data: {response.status_code}")



###################################
#Kode for å hente data fra CSV-fil#
###################################

#Laster inn datasett fra fil, hentet fra European Environment Agency (EEA)
df_eea = pd.read_csv("DataExtract.csv", low_memory=False)

#Definerer hvilke byer vi øsnker å undersøke (og alternative skrivemåter)
by_mapping = {
    "Oslo": ["Oslo"],
    "Paris": ["Paris"],
    "London": ["London"],
    "Berlin": ["Berlin"],
    "Madrid": ["Madrid"],
    "Amsterdam": ["Amsterdam"],
    "Rome": ["Rome", "Roma"],
    "Copenhagen": ["Copenhagen", "København"],
    "Ankara": ["Ankara"]
}

#Beregner gjennomsnittlig verdi og forurensningstype per by. 
avg_data = []
for visningsnavn, søkeord in by_mapping.items():
    df_by = df_eea[df_eea["Air Quality Station Name"].apply(
        lambda x: any(by.lower() in str(x).lower() for by in søkeord)
    )]
    #Gruppérer etter forurensningstype og tar gjennomsnittet av 'DetectionLimit' som måleverdi
    avg_pollutants = df_by.groupby("Air Pollutant")["Detection Limit"].mean()
    #Lagrer resultatene i en liste
    for pollutant, avg_value in avg_pollutants.items():
        avg_data.append({
            "By": visningsnavn,
            "Forurensning": pollutant,
            "Gjennomsnittlig verdi": avg_value
        })

#Konverterer til DataFrame
df_avg = pd.DataFrame(avg_data)

#Fjern ugyldige/manglende verdier (f.eks. 0 eller NaN)
df_avg = df_avg[df_avg["Gjennomsnittlig verdi"] > 0].dropna()

#Velger de 3 høyeste verdiene per by
df_top3 = df_avg.sort_values(by=["By", "Gjennomsnittlig verdi"], ascending=[True, False])
df_top3 = df_top3.groupby("By").head(3)

#Printer resultatet og lagrer i en CSV-fil
print(df_top3)
print(df_top3.to_string(index=False))
df_top3.to_csv("gjennomsnitt_by_forurensning.csv", index=False)




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

