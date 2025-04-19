import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# --- LASTER INN ALLE FILENE I MAPPEN CLEAN ---
data_mappe = "data/clean/byer"
alle_filer = glob.glob(os.path.join(data_mappe, "*.csv"))

dataframes = []
for filepath in alle_filer:
    df = pd.read_csv(filepath)
    bynavn = os.path.basename(filepath).replace("_clean.csv", "").capitalize()
    df["by"] = bynavn
    dataframes.append(df)

# === 2. Kombiner alle filer ===
combined_df = pd.concat(dataframes, ignore_index=True)

# === 3. Sørg for at datetime er riktig format ===
if "datetime" in combined_df.columns:
    combined_df["datetime"] = pd.to_datetime(combined_df["datetime"])

# === 4. Sjekk hvilke forurensningskomponenter som finnes ===
pollutants = ["pm2_5", "pm10", "no2"]
available = [p for p in pollutants if p in combined_df.columns]

# === 5. Linjediagram for PM2.5 over tid ===
if "pm2_5" in available:
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=combined_df, x="datetime", y="pm2_5", hue="by")
    plt.title("PM2.5-nivå over tid")
    plt.ylabel("PM2.5 (μg/m³)")
    plt.xlabel("Tid")
    plt.xticks(rotation=45)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()

# === 6. Boxplot – spredning per by ===
plt.figure(figsize=(12, 6))
sns.boxplot(data=combined_df, x="by", y="pm2_5", palette="Set3")
plt.title("Spredning i PM2.5-nivå per by")
plt.ylabel("PM2.5 (μg/m³)")
plt.xlabel("By")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 7. Søylediagram – gjennomsnitt per by ===
mean_df = combined_df.groupby("by")[available].mean().reset_index()
mean_melted = mean_df.melt(id_vars="by", var_name="Komponent", value_name="Gjennomsnitt")

plt.figure(figsize=(12, 6))
sns.barplot(data=mean_melted, x="Komponent", y="Gjennomsnitt", hue="by")
plt.title("Gjennomsnittlig luftforurensning per by")
plt.ylabel("μg/m³")
plt.xlabel("Komponent")
plt.tight_layout()
plt.show()

# === 8. (Valgfritt) Korrelasjonsheatmap av hele datasettet ===
plt.figure(figsize=(6, 5))
corr = combined_df[available].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korrelasjon mellom forurensningskomponentene")
plt.tight_layout()
plt.show()