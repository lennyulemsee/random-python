#!/usr/bin/python3
import pandas as pd
df = pd.read_csv("output-onlinetools.csv")
print()
df2 = df[["private", "hair"]]
data = [12, 4, 64, 75, 50]
s = pd.Series(data)
li = list() 
for word in df[1]:
    li.append(word)
print(type(df))
print(li)
print(s)
print(df)
print(df[1:3])
print(df2)
