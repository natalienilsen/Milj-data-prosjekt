import pandas as pd
import numpy as np
import os

def clean_raw_data(filepath, save_to):
    if not os.path.exists(filepath):
        print("Fant ikke filen :(")
    else:
        df = pd.read_csv(filepath)

    print("Renser filen")

    #Fjerner rader med manglende verdier. 
    df = df.dropna()
    
    #Fjerner duplikater
    df = df.drop_duplicates()

    #Fjerner rare verdier
    if "AQI" in df.columns:
        df = df[df["AQI"] != -999] #beholder alle verdier som ikke er -999
        df = df[df["AQI"] > 0] #beholder alle verdier som er over 0
        df = df[df["AQI"] <= 500] #beholder alle verdier som er under/lik 500
    
    # Lagrer renset data til ny fil
    dirpath = os.path.dirname(save_to)
    if dirpath:  # unngå feil hvis det ikke er noen mappe i filnavnet
        os.makedirs(dirpath, exist_ok=True)
    df.to_csv(save_to, index=False)
    print(f"Renset data lagret til: {save_to}\n")
    
    
    