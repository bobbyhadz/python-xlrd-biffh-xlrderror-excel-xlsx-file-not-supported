# xlrd.biffh.XLRDError: Excel xlsx file; not supported

import pandas as pd

df = pd.read_excel(
    'example.xlsx',
    engine='openpyxl'
)

print(df)