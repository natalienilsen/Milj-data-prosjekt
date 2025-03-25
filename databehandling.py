import pandas as pd
import os

#--------------------------
#---BESKRIVELSE AV KODEN---
#--------------------------

#Denne koden svarer på oppgave 3 i mappe del 1. Målet er å klargjøre alle dataene for analyse og visualisering. 



#------------------------------------------------------
#---BESTM HVILKEN FIL MED RÅDATA SOM SKAL FINSKRIVES---
#------------------------------------------------------

filepath = "/Users/vildevikane/Desktop/Milj-data-prosjekt/luftkvalitet_test.csv"
#OBS, må være csv!


#----------------------------------------------------------
#---SJEKKER FOR IKKE-EKSISTERENDE VERDIER OG NULLVERDIER---
#----------------------------------------------------------
    
def check_odd_values(filepath):
    #Leser inn filen: dette kan kanskje gjøres om til en egen funksjon
    if not os.path.exists(filepath):
        print("Fant ikke filen :(")
    else:
        df = pd.read_csv(filepath)
    
    #NaN-sjekk
    print("Antall NaN-verdier pr kolonne: ")
    print(df.isna().sum()) #isna() gir en bool på om det finnes NaN, sum() gir antallet bool, True for hver kolonne

    #0-verdi-sjekk
    print("\n🔍 Sjekker etter null-verdier (0):")
    print((df == 0).sum())
    
    #Duplikater
    number_duplicates = df.duplicated().sum()
    print(f"Duplikater i datasettet: {number_duplicates} rader")
    
    #Ulogiske verdier (-9999, AQI >= 0, eller veldig høyt)
    if "AQI" in df.columns: 
        print("Ulogiske AQI-verdier: ")
        odd_values_AQI = df[(df["AQI"] <= 0) | (df["AQI"] == -9999) | (df["AQI"] > 500)]
        print(odd_values_AQI)
    else: 
        print("Filen inneholder ikke AQI.")
    
    #lag flere koder for ulogiske verdier utifra hvilken cvs fil. 
    #Med det mener jeg at hvis en fil inneholder CO2-verdier så kan vi lete etter CO2 verdier som er skyhøye. Slik det er gjort med AQI
    #Evnt så kan alt dette slås sammen til én kode sikkert. 
    


#--------------------------
#---RENSER DATAINNHOLDET---
#--------------------------

#Denne funker ikke helt 

new_file_name = input("Hva ønsker du at den nye, rensede filen skal hete? Tror du må skrive .csv på slutten")
print("Du skrev:", new_file_name)

def cleaning_data(filepath, save_to = new_file_name):
    #Leser inn filen: dette kan kanskje gjøres om til en egen funksjon
    if not os.path.exists(filepath):
        print("Fant ikke filen :(")
    else:
        df = pd.read_csv(filepath)
    
    print("Renser filen")
    
    #Fjerner rader med manglende verdier. 
    df.dropna()
    
    #Fjerner duplikater
    df.drop_duplicates()
    
    # Lagre renset data
    #Tror det er her den tuller seg
    os.makedirs(os.path.dirname(save_to), exist_ok=True)
    df.to_csv(save_to, index=False)
    print(f"Renset data lagret til: {save_to}\n")


#-----------------------------
#---STANDARISERER KOLONNENE---
#-----------------------------



#--------------------------------------
#---LAGRER RENSET DATA I EN NY MAPPE---
#--------------------------------------



#---------------------
#---HOVEDPROGRAMMET---
#---------------------

if __name__ == "__main__":
    check_odd_values(filepath)
    cleaning_data(filepath, save_to = new_file_name)