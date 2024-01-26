#!/usr/bin/python3

import pandas as pd
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

def loader():
    async def download(url, filename):
        response = await pyfetch(url)
        if response.status == 200:
            with open(filename, 'wb') as f:
                f.write(await response.bytes())
    download(filename, 'excel_example.xlsx')
    df = pd.read_excel('excel_example.xlsx')
    print(df)
loader()

