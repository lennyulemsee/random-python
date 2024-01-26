#!/usr/bin/python3

import requests
import pandas as pd
import json
"""
This API returns random jokes from a database.
The following URL returns 10 random jokes
"""
# get the data from the api endpoint
data = requests.get("https://official-joke-api.appspot.com/jokes/ten")
#change the data from json since it's delivered in json form
jsn_data = json.loads(data.text)
# change the data to a data frame
df = pd.json_normalize(jsn_data)
#my own challenge:
"""
# get the programmers jokes if any, and print the setup and the punchlines
programmer = df.loc[df['type'] == 'Programming']
print(programmer)
pro_setup = programmer.iloc[0]['setup']
pro_punch_line = programmer.iloc[0]['punchline']
print(pro_setup, pro_punch_line)
print(df)
# Drop the type and the ID column
"""
#df.drop(columns = ['type', 'id'], inplace=True)
print(df)

