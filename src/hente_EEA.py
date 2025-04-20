import requests
import json
import pandas as pd
import matplotlib.pyplot as plt


###################################
#Kode for å hente data fra CSV-fil#
###################################

#Laster inn datasett fra fil, hentet fra European Environment Agency (EEA)
df_eea = pd.read_csv("DataExtract.csv", low_memory=False)

#Definerer hvilke byer vi øsnker å undersøke (og alternative skrivemåter)
by_mapping = {
    "Oslo": ["Oslo"],
    "Paris": ["Paris"],
    "London": ["London"],
    "Berlin": ["Berlin"],
    "Madrid": ["Madrid"],
    "Amsterdam": ["Amsterdam"],
    "Rome": ["Rome", "Roma"],
    "Copenhagen": ["Copenhagen", "København"],
    "Ankara": ["Ankara"]
}

#Beregner gjennomsnittlig verdi og forurensningstype per by. 
avg_data = []
for visningsnavn, søkeord in by_mapping.items():
    df_by = df_eea[df_eea["Air Quality Station Name"].apply(
        lambda x: any(by.lower() in str(x).lower() for by in søkeord)
    )]
    #Gruppérer etter forurensningstype og tar gjennomsnittet av 'DetectionLimit' som måleverdi
    avg_pollutants = df_by.groupby("Air Pollutant")["Detection Limit"].mean()
    #Lagrer resultatene i en liste
    for pollutant, avg_value in avg_pollutants.items():
        avg_data.append({
            "By": visningsnavn,
            "Forurensning": pollutant,
            "Gjennomsnittlig verdi": avg_value
        })

#Konverterer til DataFrame
df_avg = pd.DataFrame(avg_data)

#Fjern ugyldige/manglende verdier (f.eks. 0 eller NaN)
df_avg = df_avg[df_avg["Gjennomsnittlig verdi"] > 0].dropna()

#Velger de 3 høyeste verdiene per by
df_top3 = df_avg.sort_values(by=["By", "Gjennomsnittlig verdi"], ascending=[True, False])
df_top3 = df_top3.groupby("By").head(3)

#Printer resultatet og lagrer i en CSV-fil
print(df_top3)
print(df_top3.to_string(index=False))
df_top3.to_csv("gjennomsnitt_by_forurensning.csv", index=False)


