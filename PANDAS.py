import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('pokemon_data.xlsx')
#suma cyfry w kolumnie
print( df['Attack'].sum())
#najwyzsza suma w kolumnie
print( df['Attack'].max())
#najnizsza suma w kolumnie
print( df['Attack'].min())
#srednia sum w kolumnie
print( df['Attack'].mean())
#dla zgrupowanej kolumny po nazwie wyswietla policzone wartosci kolumny z dyframi
print( df.groupby('Type 1')['Attack'].size())
print( df.groupby('Type 1')['Attack'].sum())
print( df.groupby('Type 1')['Attack'].min())
print( df.groupby('Type 1')['Attack'].max())
print( df.groupby('Type 1')['Attack'].mean())
print( df.groupby('Type 1')['Attack'].nunique())
print( df.groupby('Type 1')['Attack'].unique())
