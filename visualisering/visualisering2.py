import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np
import plotly.express as px  

def laste_data(filepath):
    #Laster inn fildata
    
    if not os.path.exists(filepath):
        print(f"Finner ikke filen: {filepath}")
        return None
    return pd.read_csv(filepath)


def lag_grafer(df):
    #Lager visualisering av data
    
    #------------------------------------
    #Passer for: /Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_byer_clean.csv
    #------------------------------------
    
    # 1.Søylediagram: Viser gjennomsnittlig AQI pr by
    if "AQI" in df.columns:
        plt.figure(figsize = (10, 6))
        sns.barplot(data=df, x = "By", y = "AQI", estimator = "mean", errorbar=None, color = "seagreen")
        plt.title("Gjennomsnittlig luftkvalitet for storbyer i Europa, [AQI per by]")
        plt.xticks(rotation = 45)
        plt.tight_layout()
        plt.show()
    
    # 2.Histogram: fordeling av AQI-verdier
    #denne kan forbedres
    if "AQI" in df.columns:
        plt.figure(figsize = (10,6))
        sns.histplot(df["AQI"], bins = 20, kde = True)
        plt.title("Fordeling av AQI-verdier")
        plt.xlabel("AQI")
        plt.ylabel("Antall målinger")
        plt.tight_layout()
        plt.show()
    
    # 3.Histogram: luftkvalitetskategori
    if "category" in df.columns:
        plt.figure(figsize = (10,6))
        sns.histplot(df["category"], bins = 20)
        plt.title("Fordeling av AQI-verdier")
        plt.xlabel("category")
        plt.ylabel("Antall målinger")
        plt.tight_layout()
        plt.show()
    
    #$. Histogram: Dominerende forurensning blandt storbyene
        if "Dominerende forurensning" in df.columns:
            plt.figure(figsize = (8,6))
            sns.histplot(df["Dominerende forurensning"], bins = 20, color="seagreen")
            plt.title("Dominerende forurensning")
            plt.xlabel("Type forurensning")
            plt.ylabel("Antall målinger")
            plt.tight_layout()
            plt.show()
        
    #----------------------------------------
    #Passer: /Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/gjennomsnitt_by_forurensning.csv
    #----------------------------------------
    
    # 1. Gruppert søylediagram: Forurensningstype vs verdi, gruppert etter by
    if "Forurensning" in df.columns:    
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x="Forurensning", y="Gjennomsnittlig verdi", hue="By")
        plt.title("Sammenligning av forurensningstyper per by")
        plt.xlabel("Forurensningstype")
        plt.ylabel("Gjennomsnittlig verdi (µg/m³)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 2. Søylediagram per by: hvilke komponenter har høyest verdi i hver by
    if "Forurensning" in df.columns:  
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x="By", y="Gjennomsnittlig verdi", hue="Forurensning")
        plt.title("Forurensningsnivåer per by etter komponent")
        plt.xlabel("By")
        plt.ylabel("Gjennomsnittlig verdi (µg/m³)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 3. Histogram: hvor ofte komponentene forekommer
    if "Forurensning" in df.columns:  
        plt.figure(figsize=(10, 5))
        sns.histplot(df["Forurensning"], bins=len(df["Forurensning"].unique()), color="seagreen")
        plt.title("Hyppighet av forurensningstyper")
        plt.xlabel("Forurensningstype")
        plt.ylabel("Antall forekomster")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    #-----------------------------------
    #Passer til: /Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_nilu_clean.csv   
    #-----------------------------------    
    
    # 1. Søylediagram: Gjennomsnittlig forurensning per kommune
    if "zone" in df.columns: 
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x="municipality", y="value", estimator=np.mean, errorbar=None, color="seagreen")
        plt.title("Gjennomsnittlig forurensningsnivå per kommune")
        plt.xticks(rotation=45)
        plt.ylabel("Verdi (µg/m³)")
        plt.xlabel("Kommune")
        plt.tight_layout()
        plt.show()
    
     # 2. Boxplot: Fordeling av målte verdier per komponent
    if "zone" in df.columns: 
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=df, x="component", y="value", palette="Greens")
        plt.title("Fordeling av målte verdier per komponent")
        plt.ylabel("Verdi (µg/m³)")
        plt.xlabel("Utslippstype")
        plt.tight_layout()
        plt.show()
    

if __name__ == "__main__":
    filepath = input("Skriv inn filsti til CSV-filen: ").strip()
    df = laste_data(filepath)
    if df is not None:
        lag_grafer(df)

            

        
        

    
    
