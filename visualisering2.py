import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def laste_data(filepath):
    #Laster inn fildata
    
    if not os.path.exists(filepath):
        print(f"Finner ikke filen: {filepath}")
        return None
    return pd.read_csv(filepath)


def lag_grafer(df):
    #Lager visualisering av data
    
    # 1.Søylediagram: Viser gjennomsnittlig AQI pr by
    plt.figure(figsize = (10, 6))
    sns.barplot(data=df, x = "By", y = "AQI", estimator = "mean", errorbar=None, color = "green")
    plt.title("Gjennomsnittlig luftkvalitet for storbyer i Europa, [AQI per by]")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()
    
    # 2.Histogram: fordeling av AQI-verdier
    plt.figure(figsize = (10,6))
    sns.histplot(df["AQI"], bins = 20, kde = True)
    plt.title("Fordeling av AQI-verdier")
    plt.xlabel("AQI")
    plt.ylabel("Antall målinger")
    plt.tight_layout()
    plt.show()
    
    # 3.Boxplot: AQI etter luftkvalitetskategori
    if "category" in df.columns:
        plt.figure(figsize= (10,6))
        sns.boxplot(data=df, x = "category", y = "AQI")
        plt.title("AQI per luftkvalitetskategori")
        plt.xticks(rotation=45)
        plt.tight_layout
        plt.show()
    
    # 4.Histogram: luftkvalitetskategori
    plt.figure(figsize = (10,6))
    #sns.barplot(data=df, x = "category", y = "Antall målinger", estimator = "mean", errorbar=None, color = "green")
    sns.histplot(df["category"], bins = 20)
    plt.title("Fordeling av AQI-verdier")
    plt.xlabel("category")
    plt.ylabel("Antall målinger")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_byer_clean.csv"
    df = laste_data(filepath)
    
    if df is not None:
        lag_grafer(df)