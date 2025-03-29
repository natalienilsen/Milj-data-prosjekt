# Milj-data-prosjekt


Dette prosjektet samler inn og analyserer miljødata med fokus på luftkvalitet i europeiske storbyer.
Ved hjelp av åpne datakilder henter vi sanntidsdata om luftforurensning, og utfører analyser av nivåer
av partikler som PM2.5 og NO₂. Dataene bearbeides og lagres i strukturert form, for videre visualisering
og tolkning i Python.
=====================

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
- Bibilioteker:

  - 'pandas' - databehandling.
  - 'requests' - hente data fra API´er.
  - 'matplotlib' - visualisering av data.
  - 'json' - lagre og lese data.
  - 'pandasql' - ???
    ================
- Bibilioteker: 'pandas', 'requests', 'matplotlib', 'json', 'pandasql'
- Editor: VS Code + Jupyter Notebook
- Test: test-notebook som bekrefter at miljøet fungerer
- GitHub-repo: https://github.com/natalienilsen/Milj-data-prosjekt


DATAKILDER/API

**Google Air Quality API**
link: https://mapsplatform.google.com/maps-products/air-quality/

    Hva hentes? :
        Vi har brukt Google Air Quality API for å hente ut sanntidsmålinger av luftkvalitetsindex i storbyer i Europa.
        Fra API´en henter vi ut kategori og dominerende forurensing per koordinat.

    - Brukt for sanntidsmålinger av luftkvalitetsindex
        - Gir oss kategori og dominerende forurensing per koordinat

    Hvorfor er den valgt? :
        Google Air Quality API er en pålitelig og gratis plattform å hente API fra.

    Ulemper :
        Datakilden krever API-nøkkel som er gratis i 30 dager. Vi må dermed bytte ut API nøkkelen hver 30´ende dag.

    - Krever API-nøkkel

**European Environment Agency (EEA)**
link: .....
    Hva hentes? :
        Vi har hentet ut CSV-filer med historiske luftdata fra utvalgte storbyer i Europa.
        - CSV-fil med historiske luftdata fra byer i Europa
        - Brukes til å se trender når det kommer til luftkvalitet

    Hvorfor er den valgt? :

    Ulemper? :

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
- Pålitelig kilde

DATAINNSAMLING

- API-kall er utført med 'request.post()' til Google Air Quality API
- CSV-fil er lastet ned fra EEA sin nettside
- 'pandas' er brukt for å lese, filtrere og analysere filene

DATABEHANDLING
==============
