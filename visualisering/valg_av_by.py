import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- LASTER INN ALLE DATA ---
folder_path = "data/clean/byer"
filenames = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# --- OVERSIKT OVER TILGJENELIGE BYER ---
byer = [f.replace("_clean.csv", "").capitalize() for f in filenames]
print("Tilgjengelige byer:\n")
for i, by in enumerate(byer):
    print(f"{i+1}. {by}")

# --- BRUKERVALG ---
valgt_by = input("\nSkriv navnet på byen du vil lage grafer for: ").strip().lower()

# --- FEILSØK ---
match = None
for f in filenames:
    if valgt_by in f:
        match = f
        break

if not match:
    print("Fant ikke byen du skrev inn.")
else:
    filepath = os.path.join(folder_path, match)
    df = pd.read_csv(filepath)

    print(f"\nLaster inn data for: {match.replace('_clean.csv','').capitalize()}")

    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])

    # --- LINJEDIAGRAM FOR PM2.5 ---
    if "pm2_5" in df.columns:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x="datetime", y="pm2_5", color="seagreen")
        plt.title(f"PM2.5-nivå over tid i {valgt_by.capitalize()}")
        plt.ylabel("PM2.5 (μg/m³)")
        plt.xlabel("Tid")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Fant ikke kolonnen 'pm2_5' i filen.")

    # --- SØYLEDIAGRAM ---
    pollutant_cols = [col for col in df.columns if col in ["pm2_5", "pm10", "no2", "o3", "so2", "co"]]
    if pollutant_cols:
        gjennomsnitt = df[pollutant_cols].mean().reset_index()
        gjennomsnitt.columns = ["Komponent", "Gjennomsnitt"]

        plt.figure(figsize=(8, 5))
        sns.barplot(data=gjennomsnitt, x="Komponent", y="Gjennomsnitt", color="seagreen")
        plt.title(f"Gjennomsnittlig forurensningsnivå i {valgt_by.capitalize()}")
        plt.ylabel("μg/m³")
        plt.xlabel("Komponent")
        plt.tight_layout()
        plt.show()
    else:
        print("Fant ingen forurensningskomponenter å vise som søylediagram.")
