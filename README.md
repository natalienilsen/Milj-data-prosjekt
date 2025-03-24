# Milj-data-prosjekt
Updated upstream


Dette prosjektet samler inn og analyserer miljødata med fokus på luftkvalitet i europeiske storbyer. 
Ved hjelp av åpne datakilder henter vi sanntidsdata om luftforurensning, og utfører analyser av nivåer 
av partikler som PM2.5 og NO₂. Dataene bearbeides og lagres i strukturert form, for videre visualisering 
og tolkning i Python.

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
- Bibilioteker: 
    - 'pandas' - databehandling.
    - 'requests' - hente data fra API´er. 
    - 'matplotlib' - visualisering av data. 
    - 'json' - lagre og lese data. 
    - 'pandasql' - ???
- Editor: VS Code + Jupyter Notebook
- Test: test-notebook som bekrefter at miljøet fungerer
- GitHub-repo: https://github.com/natalienilsen/Milj-data-prosjekt



DATAKILDER/API


**Google Air Quality API**
link: https://mapsplatform.google.com/maps-products/air-quality/ 
        - Brukt for sanntidsmålinger av luftkvalitetsindex
        - Gir oss kategori og dominerende forurensing per koordinat
        - Krever API-nøkkel


**European Environment Agency (EEA)**
link: .....
        - CSV-fil med historiske luftdata fra byer i Europa
        - Brukes til å se trender når det kommer til luftkvalitet




**Kriterier for valg av datakilder**

- Åpen lisens
- God kvalitetsdata
- Relevante luftkvalitetsparametere: PM2.5, NO2, O3, AQI, osv
- Sanntids- og historiske data
- Pålitelig kilde



DATAINNSAMLING

- API-kall er utført med 'request.post()' til Google Air Quality API
- CSV-fil er lastet ned fra EEA sin nettside
- 'pandas' er brukt for å lese, filtrere og analysere filene


DATABEHANDLING