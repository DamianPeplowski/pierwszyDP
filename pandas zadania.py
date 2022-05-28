import pandas as pd
import numpy as np

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
df.to_excel('imiona.xlsx', sheet_name='arkusz pierwszy')

#print(df[df['Liczba']>1000])
#print(df[df['Imie']=='DAMIAN'])
#print(df['Liczba'].sum())
#print(df.sort_values(by='Liczba', ascending=False))

df = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal=',')
print(df)
df.to_csv('zamowienia.csv', index=False)
