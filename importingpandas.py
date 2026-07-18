import pandas as pd
df=pd.read_csv("data.csv",index_col="No")
#print(df)
#print(df.to_string()) can print the entire csv file as a string
#pd.read_json can read JSON files
#-----selection by column------
#print(df["Name","Height","Weight"])
#To print the entire column as a string,add .to_string() after["Name"]
# ----SELECTION BY ROWS ------
#print(df.iloc[15:54:5])
# #In the above statement, I will get pokemon numbered 15 to 54, in intervals of 5; eg 15,20,25,30 etc
#When the index is not the number of the row, we use iloc instead of loc,because loc only looks for an index that matches what you put in the square brackets
#print(df.loc["Metapod"])
#-----The following code will run a simple search to find the no of a pokemon a user inputs
#pokemon=input("type a pokemon name to find its serial designation")
#try:
# print(df.loc[pokemon])
#except KeyError:
#    print(f"{pokemon} was not found.Try again")
#------------------------------------------------------
#------ Filtering rows--------
# this will fitler out pokemon shorter than 2 m, and leave only the tallest pokemon
#tall_pokemon=[df[df["Height"]>=2]]
#print(tall_pokemon)
#this will give me a list of legendary pokemon
#legendary_pokemon=[df[df["Legendary"]==1]]
#In this case, you can also input True instead of 1 to get the exact same list of legendary pokemon
#print(legendary_pokemon)
#You can also combine arguments with & to find entries that satisy 2 or more conditions at once
#-------------------------------------------------------
#----------AGGREGATING DATA------------------

#These aggregate functions apply to the entire dataframe
#df.mean takes the average of all numeric columns
#print(df.mean(numeric_only=True))
#df.sum takes the sum of all numeric columns
#print(df.sum(numeric_only=True))
#df.min takes all of the minimum values available in the numeric columns of the dataset
#print(df.min(numeric_only=True))
#df.max similarlytakes the maximum values
#print(df.max(numeric_only=True))
#df.count counts the amount of valid entries
#print(df.count())


#These functions are relevant for a single column
#print(df["Height"].mean())
#print(df["Height"].min())
#print(df["Height"].max())
#print(df["Height"].sum())
#print(df["Height"].count())
#--------grouping functions--------
#we can use grouping functions to find the mean,min,max,count and sum based on groups that the data can be split into
#in the following example, we group the pokemon by their main type (Type1) and then find the mean,min,sum,max and count of height or some other column for these specific groups
#group=df.groupby("Type1")
#eg
#print(group["Height"].mean())
#print(group["Weight"].max())
#print(group["Height"].count())
#---------------DATA CLEANING(MOST IMPORTANT)---------------
#We can drop irrelevant columns by using the df.drop functions
#df=df.drop(columns=["Legendary"])
# df.dropna drops a row which does not have a value for a certain column.In this example, we're dropping pokemon that don't have a second type
#df=df.dropna(subset=["Type2"])
#df.fillna fills emptyrows with whatever you want to fill it with
#df=df.fillna({"Type2":"N/A"})
#We can also replace the values in a column with something else.(This is usually used to fix inconsistencies)
#In this example, we will replace grass with GRASS
#df["Type1"]=df["Type1"].replace({"Grass":"GRASS"})
 #We can standardize text(Turn it uppercase/lowercase).In this example,we will turn all of the pokemons names lowercase
 #Make sure that any column subjected ti this isnt the index column
#df["Name"] = df["Name"].str.lower()
#We can change the datatype of the legendary column from 0/1 to boolean
#df["Legendary"]=df["Legendary"].astype(bool)

#We can drop duplicate values by doing this 
#df=df.drop_duplicates()