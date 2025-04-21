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