# Miljødata - Semester Prosjekt

Denne README oppsummerer arbeidet knyttet til *TDT4114: Anvendt Programmering*. Det er levert to tidligere leveranser. Disse delene er oppsummert i `README_Mappe1.md` og `README_Mappe2.md`. Basert på tilbakemeldinger fra studass har vi samlet de viktigste analysene og visualiseringene i `rapport.ipynb`. Refleksjonsnotatet ligger i `Refleksjonsnotat.md`. Ellers er koden strukturert som følger: 

```
data  
├── clean                     # Renset data
├── outputs                   # Resultater
├── raw                       # Rådata fra API

src  
├── Mappe2_Dataanalyse        # Deskriptiv statistikk
├── Uthenting_API             # Henter data fra API
├── databehandling.py         # Prosesserer data
├── predict_polution.py       # Prediktiv analyse

test                          # Tester for viktige funksjoner
visualisering                 # Visualisering

rapport.ipynb                 # Viktigste visualiseringer og analyser
README_Mappe1.md              # Leveranse Del 1
README_Mappe2.md              # Leveranse Del 2
Refleksjonsnotat.md           # Refleksjonsnotat
requirements.txt              # Avhengigheter
```

For å kjøre koden, navigér til rot-mappen, og start med å laste ned avhengighetene gjennom 

```pip install -r requirements.txt```

Deretter kan du enten kjøre notebooken `rapport.ipynb` eller kjøre en visualiseringsfil direkte, for eksempel 

```python visualisering/main.py```
