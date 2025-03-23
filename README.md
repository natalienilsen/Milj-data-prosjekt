# Milj-data-prosjekt


Dette prosjektet skal analysere luftkvalitet i europeiske storbyer ved å bruke åpne datakilder og visualisering i Python. 

Denne README oppsummerer arbeidet knyttet til **DEL 1: Utviklingsmiljø, datainnsamling og databehandling**.


Innhold:

- Utviklingsmiljø
- Datakilder
- Datainnsamling
- Databehandling
- Visualisering
- Filstruktur


UTVIKLINGSMILJØ

- Bruker Ptyhon 3.13.1
- Bibilioteker: 'pandas', 'requests', 'matplotlib', 'json', 'pandasql'
- Editor: VS Code + Jupyter Notebook
- Test: test-notebook som bekrefter at miljøet fungerer
- GitHub-repo: https://github.com/natalienilsen/Milj-data-prosjekt



DATAKILDER


**Google Air Quality API**

- Brukt for sanntidsmålinger av luftkvalitetsindex
- Gir oss kategori og dominerende forurensing per koordinat
- Krever API-nøkkel

**European Environment Agency (EEA)**

- CSV-fil med historiske luftdata fra byer i Europa
- Brukes til å se trender når det kommer til luftkvalitet

**Kriterier for valg av datakilder**

- Åpen lisens
- God kvalitetsdata
- Relevante luftkvalitetsparametere: PM2.5, NO2, O3, AQI, osv
- Sanntids- og historiske data


DATAINNSAMLING

- API-kall er utført med 'request.post()' til Google Air Quality API
- CSV-fil er lastet ned fra EEA sin nettside
- 'pandas' er brukt for å lese, filtrere og analysere filene


DATABEHANDLING
