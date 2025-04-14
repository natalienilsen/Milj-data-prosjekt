import os
import pandas as pd
import numpy as np

# ----------------------
# 📥 Last inn data
# ----------------------
filsti = "/Users/natalienilsen/Documents/Vårsemester_2025/Miljødataanalyse/data/clean/luftkvalitet_byer_clean.csv"

if not os.path.exists(filsti):
    print(f"❌ Fant ikke filen: {filsti}")
    exit()

print(f"✅ Leser inn: {filsti}")
df_google = pd.read_csv(filsti)
print("Kolonner i datasettet:", df_google.columns.tolist())

# ----------------------
# 🧹 Rens og standardiser data
# ----------------------
df_google.columns = df_google.columns.str.upper()
df_clean = df_google.dropna(subset=["AQI"])

# ----------------------
# 📊 Statistiske mål
# ----------------------
aqi_gjennomsnitt = df_clean["AQI"].mean()
aqi_median = df_clean["AQI"].median()
aqi_std = df_clean["AQI"].std()

print(f"Gjennomsnitt AQI: {aqi_gjennomsnitt:.2f}")
print(f"Median AQI: {aqi_median:.2f}")
print(f"Standardavvik AQI: {aqi_std:.2f}")

# ----------------------
# 💾 Lagre statistikk til CSV
# ----------------------
statistikk_df = pd.DataFrame({
    "Statistikk": ["Gjennomsnitt", "Median", "Standardavvik"],
    "AQI": [aqi_gjennomsnitt, aqi_median, aqi_std]
})

output_path = os.path.abspath("../data/analyse/statistikk_aqi.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
statistikk_df.to_csv(output_path, index=False)

print("📁 Statistikk lagret!")
print(f"📍 Full sti til filen: {output_path}")
