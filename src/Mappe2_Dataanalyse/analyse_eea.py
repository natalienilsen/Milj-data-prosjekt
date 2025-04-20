import pandas as pd
import os

# --------------------------------------
# 📥 1. Les inn EEA-data (DataExtract.csv)
# --------------------------------------

filepath = "data/raw/DataExtract.csv"

if not os.path.exists(filepath):
    print(f"❌ Fant ikke EEA-datasett: {filepath}")
    exit()

df = pd.read_csv(filepath, low_memory=False)
print("✅ Lest EEA-data")

# --------------------------------------
# 🧹 2. Filtrer til utvalgte byer
# --------------------------------------

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

# Liste for resultat
resultater = []

for visningsnavn, søkeord in by_mapping.items():
    df_by = df[df["Air Quality Station Name"].apply(
        lambda x: any(by.lower() in str(x).lower() for by in søkeord)
    )]

    if not df_by.empty:
        df_by = df_by[df_by["Detection Limit"] > 0]
        snitt = df_by["Detection Limit"].mean()

        resultater.append({
            "By": visningsnavn,
            "Gjennomsnitt (Detection Limit)": round(snitt, 2),
            "Antall målinger": len(df_by)
        })

# --------------------------------------
# 📤 3. Lagre som CSV
# --------------------------------------

df_resultat = pd.DataFrame(resultater)

# Lagre per by + snitt totalt
output_dir = "data/outputs"
os.makedirs(output_dir, exist_ok=True)

df_resultat.to_csv(f"{output_dir}/statistikk_eea.csv", index=False)
print("📁 Lagret: statistikk_eea.csv")

# Vis total snittverdi på tvers av byer
snitt_total = df_resultat["Gjennomsnitt (Detection Limit)"].mean()
print(f"\n📊 EEA – Gjennomsnitt på tvers av byene: {snitt_total:.2f}")
