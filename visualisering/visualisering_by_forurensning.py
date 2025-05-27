import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_pollution_by_city_data():
    """Last inn data for gjennomsnitt by forurensning"""
    return pd.read_csv("data/clean/gjennomsnitt_by_forurensning.csv")

def create_pollution_comparison_by_type(df=None):
    """Gruppert søylediagram: Forurensningstype vs verdi, gruppert etter by"""
    
    if df is None:
        df = load_pollution_by_city_data()
    
    # Sett Seaborn-stil
    sns.set(style="whitegrid", palette="Greens")
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="Forurensning", y="Gjennomsnittlig verdi", hue="By")
    plt.title("Sammenligning av forurensningstyper per by")
    plt.xlabel("Forurensningstype")
    plt.ylabel("Gjennomsnittlig verdi (µg/m³)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def create_pollution_comparison_by_city(df=None):
    """Søylediagram per by: hvilke komponenter har høyest verdi i hver by"""
    
    if df is None:
        df = load_pollution_by_city_data()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="By", y="Gjennomsnittlig verdi", hue="Forurensning")
    plt.title("Forurensningsnivåer per by etter komponent")
    plt.xlabel("By")
    plt.ylabel("Gjennomsnittlig verdi (µg/m³)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def create_pollution_frequency_histogram(df=None):
    """Histogram: hvor ofte komponentene forekommer"""
    
    if df is None:
        df = load_pollution_by_city_data()
    
    plt.figure(figsize=(10, 5))
    sns.histplot(df["Forurensning"], bins=len(df["Forurensning"].unique()), color="seagreen")
    plt.title("Hyppighet av forurensningstyper")
    plt.xlabel("Forurensningstype")
    plt.ylabel("Antall forekomster")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_pollution_by_city():
    """Kjører alle visualiseringer for forurensning per by"""
    df = load_pollution_by_city_data()
    create_pollution_comparison_by_type(df)
    create_pollution_comparison_by_city(df)
    create_pollution_frequency_histogram(df)
    return df

if __name__ == "__main__":
    # Kjør alle visualiseringer hvis filen kjøres direkte
    visualize_pollution_by_city()
