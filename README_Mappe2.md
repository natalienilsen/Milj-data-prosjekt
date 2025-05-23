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
- Innhold: Sammanlikning av PM2.5 og heatmat for de tre utvekslingsbyene

**visualisering2.py**

- Datasett: NILU, Google, EEA
- Innhold: støtter mange datasett, laget søyle- , histogram- og boxplots

**Visualiseringstypene som er brukt er:**

- Søylediagram: for å vise sammenlikning av gjennomsnittlig forurensingtype per kilde
- Linjediagram: for å vise utvikling over tid
- Boxplot: for å vise variasjon og outliers
- Heatmap: for å vise sammenhenger mellom komponenter

Vi valgte statistisk visualisering for å prioritere presisjon og lesbarhet.

Manglende data ble behandlet med dropna() før plot.

### **Oppgave 6: Prediktiv Analyse**



### Oppgave 7: Testing

Vi har laget enhetstester v.h.a unittest slik som beskrevet i pensum. Testene er lagert for å sikre at viktige funksjoner i prosjektet fungerer som de skal.

##### Vi har valgt å teste følgende unksjoner:

databehandling.py:

- Sjekker at ugyldige AQI-verdier fjernes. For eksempel -999 eller over 500.
- Sjekker at duplikater og NaN-verdier er håndtert korrekt.
- Sjekker at bynavn blir normalisert
- Sjekker at valideringsfunkjonen returnerer korrekt struktur
- Sjekker at kolonner er tilstade og inneholder forventede datatyper.

Her dekker testene både positive og negative scenarier.

For å kjøre testene bruker vi 'bash' og deretter '**python -m unittest test/test_databehandling_unittest.py**'

##### Testfiler:

 **test/test_databehandling_unittest.py**: Inneholder testklassen TestDatabehandling og 5 separate tester:

* test_setup_creates_raw_file
* test_clean_and_save_data
* test_city_standardization
* test_validate_luftkvalitet_data
* test_validate_with_missing_column

##### Rammeverk og struktur

Vi har brukt unittest som følger standard i Python:

- Alle testklasser arver fra unittest.TestCase
- Hver test begynner med test_...
- setUp() og tearDown() brukes for å lage og slette testfiler
- asssertTrue, assertEqual, assertIn, assertRaises brukes som assert-metoder.
