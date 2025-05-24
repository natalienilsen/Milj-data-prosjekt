import requests
import pandas as pd
import time
from datetime import datetime, timedelta

API_key = "d01166dee6e6b98d1e4cf86e314c721b"  # sett inn gyldig nøkkel

lat = 59.91273
lon = 10.74609

end_time = int(time.time())
start_time = int((datetime.utcnow() - timedelta(days=5)).timestamp())

# Riktig URL for luftkvalitet (historisk)
#denne funker
url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start_time}&end={end_time}&appid={API_key}"

eks_url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API_key}"

print("URL:", url)  # valgfritt for feilsøking

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    records = []
    for entry in data["list"]:
        dt = datetime.utcfromtimestamp(entry["dt"])
        components = entry["components"]
        components["datetime"] = dt
        records.append(components)

    df = pd.DataFrame(records)
    print(df.head())

    df.to_csv("data/clean/oslo_air_quality_5days.csv", index=False)
    print("Dataen er lagret som oslo_air_quality_5days.csv")

else:
    print(f"Noe gikk galt: {response.status_code}")
