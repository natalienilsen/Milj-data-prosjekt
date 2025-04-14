
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Last inn data
df = pd.read_csv("data/clean/gjennomsnitt_by_forurensning.csv")

# Sett Seaborn-stil
sns.set(style="whitegrid", palette="Greens")

# 1. Gruppert søylediagram: Forurensningstype vs verdi, gruppert etter by
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Forurensning", y="Gjennomsnittlig verdi", hue="By")
plt.title("Sammenligning av forurensningstyper per by")
plt.xlabel("Forurensningstype")
plt.ylabel("Gjennomsnittlig verdi (µg/m³)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Søylediagram per by: hvilke komponenter har høyest verdi i hver by
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="By", y="Gjennomsnittlig verdi", hue="Forurensning")
plt.title("Forurensningsnivåer per by etter komponent")
plt.xlabel("By")
plt.ylabel("Gjennomsnittlig verdi (µg/m³)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram: hvor ofte komponentene forekommer
plt.figure(figsize=(10, 5))
sns.histplot(df["Forurensning"], bins=len(df["Forurensning"].unique()), color="seagreen")
plt.title("Hyppighet av forurensningstyper")
plt.xlabel("Forurensningstype")
plt.ylabel("Antall forekomster")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
