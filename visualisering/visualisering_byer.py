import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

#Denne filen tar inn alle filene med data for mappen data/clean/byer, og lager visualisering av dataene 

# --- LASTER INN ALLE FILENE I MAPPEN CLEAN ---
data_mappe = "data/clean/byer"
alle_filer = glob.glob(os.path.join(data_mappe, "*.csv"))

dataframes = []
for filepath in alle_filer:
    df = pd.read_csv(filepath)
    bynavn = os.path.basename(filepath).replace("_clean.csv", "").capitalize()
    df["by"] = bynavn
    dataframes.append(df)

# --- KOMBINERER ALLE FILENE ---
alle_filer_df = pd.concat(dataframes, ignore_index=True)

# --- DATAFRAME ---
if "datetime" in alle_filer_df.columns:
    alle_filer_df["datetime"] = pd.to_datetime(alle_filer_df["datetime"])

# --- SJEKKER TYPE FORURENSNING ---
pollutants = ["pm2_5", "pm10", "no2"]
available = [p for p in pollutants if p in alle_filer_df.columns]

# --- BOXPLOT: SPREDNING PER BY --- 
plt.figure(figsize=(12, 6))
sns.boxplot(data=alle_filer_df, x="by", y="pm2_5", palette="Set3")
plt.title("Spredning i PM2.5-nivå per by")
plt.ylabel("PM2.5 (μg/m³)")
plt.xlabel("By")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- SØYLEDIAGRAM: GJENNOMSNITT PER BY --- 
mean_df = alle_filer_df.groupby("by")[available].mean().reset_index()
mean_melted = mean_df.melt(id_vars="by", var_name="Komponent", value_name="Gjennomsnitt")

plt.figure(figsize=(12, 6))
sns.barplot(data=mean_melted, x="Komponent", y="Gjennomsnitt", hue="by")
plt.title("Gjennomsnittlig luftforurensning per by")
plt.ylabel("μg/m³")
plt.xlabel("Komponent")
plt.tight_layout()
plt.show()

# --- KORRELASJONS-HEATMAP --- 
plt.figure(figsize=(6, 5))
corr = alle_filer_df[available].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korrelasjon mellom forurensningskomponentene")
plt.tight_layout()
plt.show()