"""
DF= dataframe
"""

import pandas as pd

data = {
    "name":["Luffy","Zoro","Sanji","Franky","Brook","Chopper","Nami","Robin"],
    "Gender":["Male","Male","Male","Male","Male","Male","Female","Female"],
    "Speciality":["Punch","Sword","Kick","Punch","Sword","Meds","Navigate",["Knowledge","Punch"]]
    }

df = pd.DataFrame(data)

#Retrieve Multiple columns 
nameSpeciality = df[["name","Speciality"]] #Returns a new DF which contains character name speciality 
print(nameSpeciality)

