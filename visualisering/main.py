import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np 

from visualisering2 import laste_data
from visualisering2 import lag_grafer


if __name__ == "__main__":
    #legg inn hvilken datafil som skal visualiseres med grafer
    filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/data/clean/luftkvalitet_nilu_clean.csv"
    df = laste_data(filepath)
    
    if df is not None:
        lag_grafer(df)