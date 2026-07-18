import pandas as pd
data ={
    "Name": ["spongebob","Patrick","Squidward","Sandy"],
    "Age":[20,20,36,24]
}
df=pd.DataFrame(data,index=["employee 1","employee 2","employee 3","employee 4"])
df["job"]=["cook","unemployed","cashier","scientist"]
new_row=pd.DataFrame([{"Name":"Eugene","Age":50,"job":"Owner"},{"Name":"Gary","Age":20,"job":"Pet"}], index=["employer","employee 5"])
df=pd.concat([df,new_row])
print(df)