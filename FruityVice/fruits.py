#!/usr/bin/python3

import requests
import json
import pandas as pd
"""
using an API through the requests library.
We will use the APIs end point url to get to it.

The fruityvice API web service provides data for all kinds of fruits.\
        You can use fruityvice to learn about fruits. It's a free web service.
"""

fruit_vice_endpoint_url = "https://fruityvice.com/api/fruit/all"

data = requests.get(fruit_vice_endpoint_url)
results = json.loads(data.text)
df = pd.DataFrame(results)
print(df)
print()
# some of the information is still nested. we use pd.json_normalize method to
# flatten the data (put everything into headers and columns.
df2 = pd.json_normalize(results)
print(df2)

# get the family and genus of pinapple
pineapple = df2.loc[df2['name'] == 'Pineapple']
print(pineapple)
print((pineapple.iloc[0]['family']), (pineapple.iloc[0]['genus']))

# find out how many calories are contained in a banana
banana = df2.loc[df2['name'] == 'Banana']

banana_cals = banana.iloc[0]['nutritions.calories']
print(banana_cals)
