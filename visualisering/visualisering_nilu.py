import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Sørg for at filen eksisterer
filsti = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_nilu_clean.csv"

if not os.path.exists(filsti):
    print(f"❌ Fant ikke filen: {filsti}")
else:
    # Last inn data
    df = pd.read_csv(filsti)

    # 🎨 Grønn fargepalett
    sns.set_palette("Greens")
    #plt.style.use("seaborn-whitegrid")

    # 1. Søylediagram: Gjennomsnittlig forurensning per kommune
    plt.figure(figsize=(10, 5))
    #sns.barplot(data=df, x="municipality", y="value", estimator=np.mean, color="green")
    sns.barplot(data=df, x="municipality", y="value", color="green")
    plt.title("Gjennomsnittlig forurensningsnivå per kommune")
    plt.xticks(rotation=45)
    plt.ylabel("Verdi (µg/m³)")
    plt.xlabel("Kommune")
    plt.tight_layout()
    plt.show()

    # 2. Boxplot: Fordeling av målte verdier per komponent
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x="component", y="value", palette="Greens")
    plt.title("Fordeling av målte verdier per komponent")
    plt.ylabel("Verdi (µg/m³)")
    plt.xlabel("Komponent")
    plt.tight_layout()
    plt.show()

    # 3. Tidsserie: Endring i forurensning over tid i Oslo
    df_oslo = df[df["municipality"].str.lower() == "oslo"]
    if not df_oslo.empty:
        df_oslo = df_oslo.copy()  # unngår SettingWithCopyWarning
        df_oslo["fromtime"] = pd.to_datetime(df_oslo["fromtime"])
        plt.figure(figsize=(12, 5))
        sns.lineplot(data=df_oslo, x="fromtime", y="value", hue="component", palette="Greens")
        plt.title("Tidsserie: Forurensning i Oslo")
        plt.xlabel("Tid")
        plt.ylabel("Verdi (µg/m³)")
        plt.tight_layout()
        plt.show()
