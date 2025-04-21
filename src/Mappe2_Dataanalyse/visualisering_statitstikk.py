import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- Leser inn CSV-filer ----------

# Google
df_google = pd.read_csv("data/outputs/Mappe2_Statistikk/statistikk_google.csv")
gjennomsnitt_google = df_google.loc[df_google["Statistikk"] == "Gjennomsnitt", "Verdi"].values[0]

# NILU
df_nilu = pd.read_csv("data/outputs/Mappe2_Statistikk/statistikk_nilu.csv")
gjennomsnitt_nilu = df_nilu.loc[df_nilu["Statistikk"] == "Gjennomsnitt", "Verdi"].values[0]

# OpenWeather – bruker snitt av alle byers snitt
df_open = pd.read_csv("data/outputs/Mappe2_Statistikk/statistikk_openweather.csv")
gjennomsnitt_openweather = df_open["Gjennomsnitt"].mean()

# ---------- Sammenligning ----------

data = {
    "Google (AQI)": gjennomsnitt_google,
    "OpenWeather (PM10)": gjennomsnitt_openweather,
    "NILU Oslo (PM2.5)": gjennomsnitt_nilu
}

farger = ["#4CAF50", "#2196F3", "#FF5722"]

plt.figure(figsize=(8, 6))
bars = plt.bar(data.keys(), data.values(), color=farger)

# Legg på verdier over søylene
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y + 1, f"{y:.1f}", ha='center', va='bottom')

plt.title("Sammenligning av gjennomsnittlig luftforurensning fra tre kilder")
plt.ylabel("Forurensningsverdi")
plt.ylim(0, max(data.values()) + 10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()


# ---------- Lagre figuren ----------
output_dir = "data/outputs"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "sammenligning_gjennomsnitt_kilder.png")
plt.savefig(output_path)
print(f"🖼️ Visualisering lagret som: {output_path}")


plt.show()
