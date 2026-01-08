#PANDAS
#series
#It is a 1-Dimensional labeled array that can hold any data type 
#[single column]

import pandas as pd
data = [100, 102, 104, 105]
series = pd.Series(data)
print(series)

#we can also set new label
series = pd.Series(data, index = ["a", "b", "c", "d"])
print(series)

#to access elements in series
#loc -> location of labels in series
print(series.loc["d"])

#to access elements in series using integer position using iloc
print(series.iloc[0])

print(series[series > 100])

#dictionary
calories = {"Day 1" : 1750, "Day 2": 876, "Day 3": 560}
series = pd.Series(calories)
print(series)

#Dataframes
#A tabular data structure with rows and columns [2Dimensional]
import pandas as pd
data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30,35,50]
        }
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
print(df.loc["Employee 1"])
print(df.iloc[0])

#to add new column
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)

#to add new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 67, "Job": "Manager"}], index = ["Employee 4", "Employee 5"])
df= pd.concat([df, new_row])
print(df)

#TASK
emp_data = {"Name": ["Sakthee", "Vanitha", "Jaisurya"],
             "ID": ["1001", "1002", "1003"],
             "Dept":["AI", "MBA", "ECE"]}
df = pd.DataFrame(emp_data, index=["Employee 1", "Employee 2", "Employee 3"])
print(df)

df["Location"] = ["Chennai", "Banglore", "Hyderabad"]
print(df)

new = pd.DataFrame([{"Name": "Prabha", "ID": "1004", "Dept": "CCE", "Location": "Pune"}], index = ["Employee 4"])
df= pd.concat([df, new])
print(df)

#importing
#to read csv data 
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')
df = pd.read_csv(r"C:\Users\sakthep\OneDrive - Capgemini\SAKTHEE\projects\python practice\python\.py files\Python concepts\data.csv")
print(df) #this prints first 5 and last 5 rows [means head and tail]
print(df.to_string()) #this prints all the rows and columns

#to read json data
import json
df = pd.read_json("metadata 4.json")
print(df)
print(df.to_string())

#selection by column for csv data
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')
df = pd.read_csv("data.csv")
print(df["Name"].to_string())
print(df[["Name", "Height", "Weight"]].to_string())

#selection by row
print(df.loc[0])

#passing the input and printing the particular data
df = pd.read_csv("data.csv", index_col = "Name")

#to print only height and weight of that data
print(df.loc["Pikachu",["Height", "Weight"]].to_string())

#to print between range
print(df.iloc[0:10])
print(df.iloc[0:10:2])
print(df.iloc[0:10:2, 0:2])

#by passing the input 
df = pd.read_csv("data.csv", index_col = "Name")
name = input("Enter a name: ")

try:
    print(df.loc[name])
except KeyError:
    print(f"{name} not found")

#Filtering -> keeping the rows that match a condition
#to print a pokemon name that has height > 2 meteres and above
import pandas as pd
df = pd.read_csv("data.csv")
h_data = df[df["Height"] >= 2]
w_data = df[df["Weight"] >= 50]
water_pk = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
ff_pk = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pk)
print(water_pk)
print(h_data)
print(w_data)

#aggregate functions using pandas
#we can find mean of any column that are non numeric

#but to find mean of numeric column we should pass keyword argument numeric_onl = True
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))

print(df.count()) #-> for count; no need to pass keyword argument

#single column
#since height is a numeric column so no need to pass keword argument
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())

#grouping the dataframe
#grouping all fire type in one group and grass type in another
group = df.groupby("Type1")
print(group["Height"].sum())
#this results all type 1 category with sum function

#Data Cleaning using pandas
#The process of fixing/removing incomplete, incorrect or irrelevant data
#75% of work done with pandas is data cleaning
import pandas as pd
df = pd.read_csv("data.csv")

#drop irrrelevant columns
#df = df.drop(columns=["Legendary"])

#to handle missing data
#if a row that is nan in type2 --> remove that column
df=df.dropna(subset=["Type2"])

#to replace nan values wiht someother string
df = df.fillna({"Type2" : "None"})
print(df.to_string())

#to fix inconsistent values
#to change to uppercase
#df["type1"] --> is a series; and from that series accessing "type1" column
df["Type1"]= df["Type1"].replace({"Grass": "GRASS",
                                  "Fire": "FIRE",
                                  "Water": "WATER"})
print(df.to_string())

#to standarize text
df["Name"] = df["Name"].str.lower()
print(df.to_string())

#to fix data types
#changing 0's to FALSE
df["Legendary"] = df["Legendary"].astype(bool)
print(df.to_string())

#to remove duplicates
df = df.drop_duplicates()
print(df.to_string())


