import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np 


def laste_data(filepath):
    #Laster inn fildata
    
    if not os.path.exists(filepath):
        print(f"Finner ikke filen: {filepath}")
        return None
    return pd.read_csv(filepath)


def lag_grafer(df):
    #Lager visualisering av data
    
    #------------------------------------
    #Passer for: luftkvalitet_byer_clean
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
    
    # 3.Boxplot: AQI etter luftkvalitetskategori
    # denne likte jeg ikke, lite intuitiv synes jeg
    if "category" in df.columns:
        plt.figure(figsize= (10,6))
        sns.boxplot(data=df, x = "category", y = "AQI")
        plt.title("AQI per luftkvalitetskategori")
        plt.xticks(rotation=45)
        plt.tight_layout
        plt.show()
    
    # 4.Histogram: luftkvalitetskategori
    if "category" in df.columns:
        plt.figure(figsize = (10,6))
        sns.histplot(df["category"], bins = 20)
        plt.title("Fordeling av AQI-verdier")
        plt.xlabel("category")
        plt.ylabel("Antall målinger")
        plt.tight_layout()
        plt.show()
    
    #5. Histogram: Dominerende forurensning blandt storbyene
    if "Dominerende forurensning" in df.columns:
        plt.figure(figsize = (8,6))
        sns.histplot(df["main_pollutant"], bins = 20, color="seagreen")
        plt.title("Dominerende forurensning")
        plt.xlabel("Type forurensning")
        plt.ylabel("Antall målinger")
        plt.tight_layout()
        plt.show()

    #----------------------------------------
    #Passer: gjennomsnitt_by_forurensing_clean
    #----------------------------------------
    
    #6. Søylediagram: 
    if "gjennomsnittlig verdi" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.barplot(data=df, x="by", y="gjennomsnittlig verdi", estimator="mean", errorbar=None)
        plt.title("Gjennomsnittlig forurensningsnivå per by")
        plt.ylabel("Gjennomsnittlig verdi")
        plt.xlabel("By")
        plt.tight_layout()
        plt.show()
        
    #7. 
    # 2. Punktplot: alle målinger for Oslo
    if "forurensning" in df.columns:
        oslo_df = df[df["by"] == "Oslo"]
        plt.figure(figsize=(7, 4))
        sns.scatterplot(data=oslo_df, x="forurensning", y="gjennomsnittlig verdi", color="green", s=100)
        plt.title("Forurensningsnivå i Oslo")
        plt.ylabel("Verdi")
        plt.xlabel("Forurensningstype")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 3. Gruppert søylegraf: forurensning per by og type
    if "forurensning" in df.columns:
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x="forurensning", y="gjennomsnittlig verdi", hue="by")
        plt.title("Sammenligning av forurensningstyper per by")
        plt.ylabel("Gjennomsnittlig verdi")
        plt.xlabel("Forurensningstype")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    #-----------------------------------
    #Passer til: luftkvalitet_nilu_clean    
    #-----------------------------------    
    
    # 1. Søylediagram: Gjennomsnittlig forurensning per kommune
    if "zone" in df.columns: 
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x="municipality", y="value", estimator=np.mean, color="seagreen")
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
        plt.xlabel("Komponent")
        plt.tight_layout()
        plt.show()

    # 3. Tidsserie: Endring i forurensning over tid i Oslo
    #Denne var ikke så bra
    if "zone" in df.columns: 
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
    


if __name__ == "__main__":
    #legg inn hvilken datafil som skal visualiseres med grafer
    filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_nilu_clean.csv"
    df = laste_data(filepath)
    
    if df is not None:
        lag_grafer(df)