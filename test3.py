import requests

# Din OpenAQ API-nøkkel
api_key = '828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf'

# Landkode for ønsket land (f.eks. 'DE' for Tyskland)
country_code = 'DE'

# API-endepunkt for å hente stasjoner i et spesifikt land
url = f'https://api.openaq.org/v3/locations?country={country_code}'

# HTTP-headers med API-nøkkel
headers = {
    'X-API-Key': api_key
}

# Gjør en GET-forespørsel til API-et
response = requests.get(url, headers=headers)

# Sjekk om forespørselen var vellykket
if response.status_code == 200:
    data = response.json()
    # Iterer gjennom stasjonene og skriv ut navn og location_id
    for location in data['results']:
        print(f"Stasjon: {location['name']}, ID: {location['id']}")
else:
    print(f'Feil ved henting av data: {response.status_code}')
