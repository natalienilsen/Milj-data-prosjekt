import requests

# Din OpenAQ API-nøkkel
API_KEY = "828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf"

# Liste over de 15 største byene i Europa
cities = [
    "London", "Berlin", "Madrid", "Roma", "Paris", "București", "Wien", "Hamburg",
    "Warszawa", "Budapest", "Barcelona", "München", "Milano", "Sofia", "Brussel"
]

# Base URL for OpenAQ API v3
base_url = "https://api.openaq.org/v3/latest"

# Headers med API-nøkkelen
headers = {
    "X-API-Key": API_KEY
}

# Hente data for hver by
for city in cities:
    params = {"city": city, "limit": 1}
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            measurements = data['results'][0]['measurements']
            print(f"Luftkvalitet i {city}:")
            for measurement in measurements:
                print(f"  - {measurement['parameter']}: {measurement['value']} {measurement['unit']}")
        else:
            print(f"Ingen data tilgjengelig for {city}.")
    else:
        print(f"Feil ved henting av data for {city}: {response.status_code} - {response.text}")


