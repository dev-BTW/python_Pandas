import pandas as pd

data = {
    "name":["Luffy","Zoro","Sanji","Franky","Brook","Chopper","Nami","Robin"],
    "Gender":["Male","Male","Male","Male","Male","Male","Female","Female"],
    "Speciality":["Punch","Sword","Kick","Punch","Sword","Meds","Navigate",["Knowledge","Punch"]]
    }


df = pd.DataFrame(data)
print(df,end="\n\n")

print("Name column from dataframe",end="\n\n")
x = df[["name"]] #Returns a dataframe of mentioned column name
print(x)