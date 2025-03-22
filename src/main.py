import pandas as pd

# Last inn datasettet
df = pd.read_csv("DataExtract.csv", low_memory=False)

# Definer byene og alternative navn
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

# Samle gjennomsnittlig verdi per by og forurensning
avg_data = []
for visningsnavn, søkeord in by_mapping.items():
    df_by = df[df["Air Quality Station Name"].apply(
        lambda x: any(by.lower() in str(x).lower() for by in søkeord)
    )]
    avg_pollutants = df_by.groupby("Air Pollutant")["Detection Limit"].mean()
    for pollutant, avg_value in avg_pollutants.items():
        avg_data.append({
            "By": visningsnavn,
            "Forurensning": pollutant,
            "Gjennomsnittlig verdi": avg_value
        })

# Lag DataFrame
df_avg = pd.DataFrame(avg_data)

# Fjern ugyldige/manglende verdier
df_avg = df_avg[df_avg["Gjennomsnittlig verdi"] > 0].dropna()

# Velg de 3 høyeste verdiene per by
df_top3 = df_avg.sort_values(by=["By", "Gjennomsnittlig verdi"], ascending=[True, False])
df_top3 = df_top3.groupby("By").head(3)

# Vis resultat
print(df_top3)
