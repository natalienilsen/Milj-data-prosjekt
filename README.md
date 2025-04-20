# Miljødata - Semester Prosjekt

Denne README oppsummerer arbeidet knyttet til **DEL 1: Utviklingsmiljø, datainnsamling og databehandling**.

## **Mappe, Del 1**

Dette prosjektet har som mål å samle inn, analyserer og visualisere miljødata, der vi har valgt å se på luftkvalitetsdata fra 10 Europeiske storbyer. Ved hjelp av åpne datakilder henter vi sanntidsdata og historiske målinger av luftforurensning, med fokus på partikler som PM2.5 og NO₂. Dataene bearbeides og lagres i strukturert form, for videre visualiseringog tolkning i Python.

#### **Innhold**

- Utviklingsmiljø
- Datakilder
- Datainnsamling
- Databehandling
- Visualisering
- Filstruktur

### **UTVIKLINGSMILJØ**

- Programmeringsspråk: Python 3.13.1
- Bibilioteker:

  - 'pandas' - databehandling.
  - 'requests' - hente data fra API´er.
  - 'matplotlib' - visualisering av data.
  - 'json' - lagre og lese data.
- Editor: Visual Studio Code + Jupyter Notebook
- Test: Notebook som bekrefter at miljøet fungerer
- GitHub-repo: https://github.com/natalienilsen/Milj-data-prosjekt

### **DATAKILDER/API**

##### **Google Air Quality API**

link: https://mapsplatform.google.com/maps-products/air-quality/

 **Hva hentes?**

- Vi har brukt Google Air Quality API for å hente ut sanntidsmålinger av luftkvalitetsindex (AQI) i Europeiske storbyer.
- Fra API´en henter vi ut kategori og dominerende forurensing per koordinat.

 **Hvorfor er den valgt?**

* Google Air Quality API er en pålitelig og gratis plattform å hente API fra.

 **Ulemper?**

* Datakilden krever API-nøkkel som er gratis i 30 dager. Vi må dermed bytte ut API nøkkelen hver 30´ende dag.

##### **European Environment Agency (EEA)**

link: https://www.eea.europa.eu/en/analysis/maps-and-charts/up-to-date-air-quality-data

    **Hva hentes?**

* Vi har hentet ut CSV-filer med historiske luftdata fra utvalgte storbyer i Europa.
* Deretter har vi filtrert dataen slik at vi ser på kolonnene som inneholder verdier for luftforurensning som PM2.5, NO2 m.m. fra storbyene.

  **Hvorfor er den valgt?**
* Denne kilden er åpen og gratis, og å kunne lagre dataen i en CSV. -fil, gjør det lettere å kontrollere hvilke kolonner som skal velges, og faktisk se dataen i et tabell.
* Datafilen inneholder de relevante luftkvalitetsparameterene vi er på utskikk etter.

 **Ulemper?**

* Dataen inneholder enkelte mangler og ulogiske verdier, og må derfor renses før analyse.


NILU

- Timesdata/aggregerbar
- API
- Sanntid
- Rådata (målinger)
- Norske byer


OpenWeather

- Timesdata (siste 5 dager)
- API
- Historikk
- Utvalgte byer





### **DATAINNSAMLING**

- Sanntidsdataen er hentet via request.post() fra Google Air Quality API.
- CSV-fil er lastet ned fra EEA sin nettside.
- 'pandas' er brukt for å lese, filtrere og analysere filene.

### DATABEHANDLING

Før analyse og visualisering har dataene:

* Blitt sjekket for mangler, ulogiske og dupliserte verdier.
* Rader som er ugyldige har blitt fjernet.
* Standardisering av variabler (f.eks navn på byer og forurensningstyper)
* Filtrert til topp 3 forurensingstyper per by
* Den ferdigbehandlede dataen er lagret i egne CSV-filer.

### VISUALISERING

Vi har brukt matplotlib til å visuali