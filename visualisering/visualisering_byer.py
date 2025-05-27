import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

def load_all_city_data():
    """Laster inn alle filene med data for mappen data/clean/byer"""
    
    # --- LASTER INN ALLE FILENE I MAPPEN CLEAN ---
    data_mappe = "data/clean/byer"
    alle_filer = glob.glob(os.path.join(data_mappe, "*.csv"))

    dataframes = []
    for filepath in alle_filer:
        df = pd.read_csv(filepath)
        bynavn = os.path.basename(filepath).replace("_clean.csv", "").capitalize()
        df["by"] = bynavn
        dataframes.append(df)

    # --- KOMBINERER ALLE FILENE ---
    alle_filer_df = pd.concat(dataframes, ignore_index=True)

    # --- DATAFRAME ---
    if "datetime" in alle_filer_df.columns:
        alle_filer_df["datetime"] = pd.to_datetime(alle_filer_df["datetime"])
    
    return alle_filer_df

def create_pm25_boxplot(df=None):
    """Lager boxplot for PM2.5 spredning per by"""
    
    if df is None:
        df = load_all_city_data()
    
    # --- BOXPLOT: SPREDNING PER BY --- 
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x="by", y="pm2_5", palette="Set3")
    plt.title("Spredning i PM2.5-nivå per by")
    plt.ylabel("PM2.5 (μg/m³)")
    plt.xlabel("By")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def create_average_pollution_barplot(df=None):
    """Lager søylediagram for gjennomsnittlig forurensning per by"""
    
    if df is None:
        df = load_all_city_data()
    
    # --- SJEKKER TYPE FORURENSNING ---
    pollutants = ["pm2_5", "pm10", "no2"]
    available = [p for p in pollutants if p in df.columns]

    # --- SØYLEDIAGRAM: GJENNOMSNITT PER BY --- 
    mean_df = df.groupby("by")[available].mean().reset_index()
    mean_melted = mean_df.melt(id_vars="by", var_name="Komponent", value_name="Gjennomsnitt")

    plt.figure(figsize=(12, 6))
    sns.barplot(data=mean_melted, x="Komponent", y="Gjennomsnitt", hue="by")
    plt.title("Gjennomsnittlig luftforurensning per by")
    plt.ylabel("μg/m³")
    plt.xlabel("Komponent")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def create_pollution_correlation_heatmap(df=None):
    """Lager korrelasjons-heatmap for forurensningskomponenter"""
    
    if df is None:
        df = load_all_city_data()
    
    # --- SJEKKER TYPE FORURENSNING ---
    pollutants = ["pm2_5", "pm10", "no2"]
    available = [p for p in pollutants if p in df.columns]

    # --- KORRELASJONS-HEATMAP --- 
    plt.figure(figsize=(6, 5))
    corr = df[available].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Korrelasjon mellom forurensningskomponentene")
    plt.tight_layout()
    plt.show()
    
    return corr

def visualize_all_cities():
    """Kjører alle visualiseringer for bydata"""
    df = load_all_city_data()
    create_pm25_boxplot(df)
    create_average_pollution_barplot(df)
    create_pollution_correlation_heatmap(df)
    return df

if __name__ == "__main__":
    # Kjør alle visualiseringer hvis filen kjøres direkte
    visualize_all_cities()