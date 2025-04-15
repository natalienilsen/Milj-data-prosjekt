import requests
import pandas as pd
import time
from datetime import datetime, timedelta

# ✅ 1. API-nøkkel (legg inn din her)
#API_KEY = "220fb7436d25f0132afe42878d605a3f"
API_key = "d01166dee6e6b98d1e4cf86e314c721b"

# ✅ 2. Koordinater for Oslo
lat = 59.91273 #breddegrad
lon = 10.74609 #lengdegrad

# ✅ 3. Tidsperiode (de siste 5 dagene)
end_time = int(time.time())
start_time = int((datetime.utcnow() - timedelta(days=5)).timestamp())

# ✅ 4. Kall til API
#url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start_time}&end={end_time}&appid={API_key}"

#url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}"

#url uten &exclude, sto at dette var optional
url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}"

#eksempel url med koordinater
eks_url = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API_key}"

response = requests.get(eks_url)

if response.status_code == 200:
    data = response.json()

    # ✅ 5. Rens data og lag DataFrame
    records = []
    for entry in data['list']:
        dt = datetime.utcfromtimestamp(entry['dt'])
        components = entry['components']
        components["datetime"] = dt
        records.append(components)

    df = pd.DataFrame(records)
    print(df.head())

    # ✅ 6. (Valgfritt) Lagre som CSV
    df.to_csv("data/clean/oslo_air_quality_5days.csv", index=False)
    print("✅ Data lagret som oslo_air_quality_5days.csv")

else:
    print(f"🚨 Noe gikk galt: {response.status_code}")
