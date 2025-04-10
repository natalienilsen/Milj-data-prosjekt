import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def last_in_data(filepath):
    """Laster inn data til DataFrame."""
    if not os.path.exists(filepath):
        print(f"❌ Fant ikke filen: {filepath}")
        return None
    return pd.read_csv(filepath)


def lag_grafer(df):
    """Lager og viser tre visualiseringer basert på data."""

    # 1. Søylediagram: Gjennomsnittlig AQI per by
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="city", y="aqi", estimator="mean", errorbar=None)
    plt.title("Gjennomsnittlig luftkvalitet (AQI) per by")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 2. Histogram: Fordeling av AQI-verdier
    plt.figure(figsize=(8, 5))
    sns.histplot(df["aqi"], bins=20, kde=True)
    plt.title("Fordeling av AQI-verdier")
    plt.xlabel("AQI")
    plt.ylabel("Antall målinger")
    plt.tight_layout()
    plt.show()

    # 3. Boxplot: AQI etter luftkvalitetskategori
    if "category" in df.columns:
        plt.figure(figsize=(9, 5))
        sns.boxplot(data=df, x="category", y="aqi")
        plt.title("AQI per luftkvalitetskategori")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    filsti = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_byer_clean.csv"
    df = last_in_data(filsti)

    if df is not None:
        lag_grafer(df)


