def hello():
    return "hello world"

if __name__ == "__main__":
    print(hello())

# Optional print statement
print("heisann")

import requests
import pandas as pd

# NILU API endpoint
url = "https://api.nilu.no/aq/utd"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    
    # Save DataFrame to CSV
    df.to_csv("luftkvalitet_nilu.csv", index=False)
    
    print("✅ Luftkvalitetsdata lagret i luftkvalitet_nilu.csv")
else:
    print(f"❌ Feil ved henting av data: {response.status_code}")
