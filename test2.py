#API_key = 828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf

import requests

# Sett inn din API-nøkkel her
API_KEY = "828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf"

# API-endepunkt for å hente sanntidsdata
url = "https://api.openaq.org/v3/latest"

# Parametere (f.eks. for London)
params = {
    "city": "London",
    "limit": 5,  # Begrens antall resultater
}

# Headers (inkluderer API-nøkkel)
headers = {
    "Authorization": f"Bearer {API_KEY}"  # OpenAQ krever en "Bearer Token"
}

# Send forespørselen
response = requests.get(url, headers=headers, params=params)

# Sjekk om forespørselen var vellykket
if response.status_code == 200:
    data = response.json()  # Konverterer svaret til JSON
    print(data)  # Skriv ut luftkvalitetsdata
else:
    print(f"Feil {response.status_code}: {response.text}")  # Feilmelding

