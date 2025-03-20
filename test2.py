#API_key = 828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf

import requests

#url = "https://api.openaq.org/v3/locations/8118"
headers = {"X-API-Key": "828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf"}

#response = requests.get(url, headers=headers)

#url = "https://api.openaq.org/v3/parameters/2/latest?limit=1000" 
url = "https://api.openaq.org//v3/countries/{6}?limit=1000" 
#headers = {"X-API-Key": "828ce8950001217e876b9e1e29a137ab72e5bf2a75e5a431f021d67d802eecbf"}

response = requests.get(url, headers=headers)

response = requests.get(url, headers=headers) 

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Feil ved API-forespørselen:", response.status_code)


#/v3/countries/{countries_id}