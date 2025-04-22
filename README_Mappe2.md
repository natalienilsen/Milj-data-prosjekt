# Mappe **DEL 2: Dataanalyse, Visualisering og Prediksjon**

Denne README viser arbeidet vårt knyttet til Mappe del 2 i prosjektet Miljødataanalyse, og vi har bygget videre på tidligere innsamlet data og gjort statistisk analyse, visualisering og prediktiv modellering.


### **Oppgave 4: Dataanalyse**

Pandas og NumPy ble brukt til å beregne statistiske mål som:

- Gjennomsnitt, median og standardavvik
- Per by og per datakilde (Google API, OpenWeather, NILU og EEA)

Analysen ble gjort for å vurdere nivå, spredning og kvalitet i luftmplingene. Det hjelper oss med å sammenlikne miljøbelastning på tvers av byer.

Det som ble analysert var AQI (Air Quality Index) og PM2.5, PM10, NO2 og O3-verdier. Resultatene ble deretter lagret som CSV-filer og visualisert i data/outputs/Mappe2_Statistikk.

Skjevheter ble håndtert ved å filtrere bort ugyldige verdier (NaN, -999, 0), og dropnp() og describe() ble brukt for datavalg og kvalitetssikring.


### **Oppgave 5: Visualisering**

Matplotlib og Seaborn er brukt for å lage visualiseringer som viser trender i luftkvalitet og forurensingsdata.

***Innhold:***

**valg_av_by.py:**

- Datasett: OpenWeather (per by)
- Innhold: viser PM2.5 over tid og gjennomsnitt for komponenter

**visualisering_byer.py:**

- Datasett: OpenWeather (alle byer)
- Innhold: boxplot av spredning, barplot av gjennomsnitt, heatmap av korrelasjon

**visualisering_by_forurensing.py:**

- Datasett: EEA
- Innhold: Sammenlikning av komponenter og byer

**visualisering_utvekslingsby.py:**

- Datasett: OpenWeather (København, Grenoble, Milano)
- Innhold: Sammanlikning av PM2.5 og heatmat for de tre utve