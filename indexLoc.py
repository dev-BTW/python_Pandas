"""
    In this we will locate element(s) of a DF based on its index location using the iloc method 
"""

import pandas as pd 

data = {
    "name":["Luffy","Zoro","Sanji","Franky","Brook","Chopper","Nami","Robin"],
    "Gender":["Male","Male","Male","Male","Male","Male","Female","Female"],
    "Speciality":["Punch","Sword","Kick","Punch","Sword","Meds","Navigate",["Knowledge","Punch"]]
    }

df =  pd.DataFrame(data)
print(df.iloc[0],end="\n\n")
print(df.iloc[0,0],end="\n\n")
print(df.iloc[0,2])

