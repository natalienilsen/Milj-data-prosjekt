import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np
import plotly.express as px 

def compare_exchange_cities():
    """Sammenligner byene som hver i gruppen er på utveksling i"""
    
    # --- LESER DATA ---
    df_kobenhavn = pd.read_csv("data/clean/byer/københavn_clean.csv")
    df_grenoble = pd.read_csv("data/clean/byer/grenoble_clean.csv")
    df_milano = pd.read_csv("data/clean/byer/milano_clean.csv")

    # --- LEGGER INN BYNAVN --- 
    df_kobenhavn["by"] = "København"
    df_grenoble["by"] = "Grenoble"
    df_milano["by"] = "Milano"

    # --- KOMBINERER DATA TIL ÉN DATAFRAME --- 
    df = pd.concat([df_kobenhavn, df_grenoble, df_milano])

    # --- KONVERTERER TID ---
    df["datetime"] = pd.to_datetime(df["datetime"])

    # --- SAMMENLIGNER PM2.5 --- 
    if "pm2_5" in df.columns:
        plt.figure(figsize=(12, 6))
        for by in df["by"].unique():
            subset = df[df["by"] == by]
            plt.plot(subset["datetime"], subset["pm2_5"], label=by)

        plt.title("Sammenligning av PM2.5-nivåer i tre byer")
        plt.xlabel("Tid")
        plt.ylabel("PM2.5 (μg/m³)")
        plt.legend()
        plt.tight_layout()
        plt.show()

    return df

def create_correlation_heatmap(df=None):
    """Lager heatmap for korrelasjon mellom forurensningskomponenter"""
    
    if df is None:
        # Last inn data hvis ikke gitt
        df_kobenhavn = pd.read_csv("data/clean/byer/københavn_clean.csv")
        df_grenoble = pd.read_csv("data/clean/byer/grenoble_clean.csv")
        df_milano = pd.read_csv("data/clean/byer/milano_clean.csv")
        
        df_kobenhavn["by"] = "København"
        df_grenoble["by"] = "Grenoble"
        df_milano["by"] = "Milano"
        
        df = pd.concat([df_kobenhavn, df_grenoble, df_milano])

    # --- HEATMAP ---
    # Velg relevante numeriske kolonner for korrelasjon
    subset = df[["co", "no", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"]]

    # Beregn korrelasjonsmatrisen
    corr = subset.corr()

    # Lag heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
    plt.title("Korrelasjon mellom forurensningskomponentene")
    plt.tight_layout()
    plt.show()
    
    return corr

if __name__ == "__main__":
    # Kjør funksjonene hvis filen kjøres direkte
    df = compare_exchange_cities()
    create_correlation_heatmap(df)