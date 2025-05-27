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

- Vi implementerte her en prediktiv modell basert på lineær regresjon med mål om å forutsi fremtidige nivåer av luftforurensning. Dette ble representert ved AQI basert på miljødata hentet fra tidligere renset CSV-fil.

Manglende verdier ble håndtert ved rensing av data, slik at modellen vår alltid opererte på gyldige verdier.

Kategori-variabler trengte vi ikke forholde oss til da vi så på hver by isolert - om man ønsker å lage en felles modell for flere byer vil man kunne bruke byen som feature ved å one-hot encode den.

Datene ble deretter delt inn i trenings- og testsett, og modellen ble så trent og evaluert ved hjelp av R² og RMSE.

**Visualiseringer**

1. Linjediagram

- Viste endringer i AQI over tid for å observere trender
- Grunnlag for valg: Linjediagram er godt egnet for tidsserier og gir et klart bilde av utviklingen

2. Søylediagram

- Brukt for å vise antall manglende verdier per kolonne
- Grunnlag for valg: Gjør det mulig å raskt se hvilke variabler som hadde størst datamangler

3. Scatterplot

- Viser modellens presisjon ved å sammenligne faktisk og predikert AQI
- Brukt for å vise avvik mellom forutsagte og faktiske verdier
- Grunnlag for valg: Effektive for å vise forholdet mellom to variabler

Visualiseringene ble laget ved bruk av Matplotlib og Seaborn.
Vi tilpasset aksene, titlene og brukte fargepaletten 'coolwarm' for å forbedre lesbarheten og det estetiske uttrykket til modellene.

### Oppgave 7: Testing

Vi har laget enhetstester v.h.a unittest slik som beskrevet i pensum. Testene er lagert for å sikre at viktige funksjoner i prosjektet fungerer som de skal.

##### Vi har valgt å teste følgende funksjoner fra databehandling.py:

- Sjekker at ugyldige AQI-verdier fjernes. For eksempel -999 eller over 500.
- Sjekker at duplikater og NaN-verdier er håndtert korrekt.
- Sjekker at bynavn blir normalisert
- Sjekker at valideringsfunkjonen returnerer korrekt struktur
- Sjekker at kolonner er tilstade og inneholder forventede datatyper.

Her dekker testene både positive og negative scenarier.

Vi har samlet alle testene i en Jupyter Notebook under /test for å kunne kjøre testene én og én.

##### Testfiler:

**test/test-notebook.ipynb:** Inneholder testklassen TestDatabehandling og 5 separate tester:

test_raw_file_created --> Sjekker at testfiler er lagret korrekt og har strukturen vi forventer

test_clean_and_save_data --> Sjekker at renset data fjerner de ugyldige verdiene og at kolonnene er standardisert.

test_validate_luftkvalitet_data--> Sjekker at valideringsrapporten har riktig format og innhold

test_check_odd_values_output--> Tester at funksjonen skriver ut info om NaN og duplikater.

test_file_not_found--> Sjekker at manglene filer blir håndtert riktig og at de ikke krasjer.

##### Rammeverk og struktur

Vi har brukt unittest som følger standard i Python:

- Alle testklasser arver fra unittest.TestCase
- Hver test begynner med test_...
- setUp() og tearDown() brukes for å lage og slette testfiler
- asssertTrue, assertEqual, assertIn, assertRaises brukes som assert-metoder.
