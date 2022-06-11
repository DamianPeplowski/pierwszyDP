import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('pokemon_data.xlsx')
#print(df)
#zlicza wszystkie typ1 pokemonów
#plt.subplot(1, 2, 1)
#x = df.groupby('Type 1').size()
#x.plot.bar()
#plt.ylabel("liczba Pokemonów")
#plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
#plt.title('Główny rodzaj pokemona')
#zlicza wszystkie typ1 pokemonów
#plt.subplot(1, 2, 2)
#y = df.groupby('Type 2').size()
#y.plot.bar()
#plt.ylabel("liczba Pokemonów")
#plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
#plt.title('Drugi rodzaj pokemnona')
#plt.subplots_adjust(wspace=0.85)
#plt.show()
#liczy wszystkie nazwy pokemonow
#print(df.Legendary[df.Legendary == True].count())
#print(df['Name'].nunique())
#liczy w kolumnie typ 1 ile razy pojawia sie typ Grass
#print(df.loc[df['Type 1'] == 'Grass'].count()[0])
#print(df['Type 1'].value_counts().Grass)
#print(df['Type 2'].value_counts().Grass)

#print(df.groupby('Type 1').value_counts().Grass)
#wykres kołowy

#type1 = df.loc[df['Type 1'] == 'Grass'].count()[0]
#type2 = df.loc[df['Type 2'] == 'Grass'].count()[0]
#plt.figure(figsize=(8,5))
#labels = ['Type 1', 'Type 2']
#colors = ['#abcdef', '#aabbcc']
#plt.pie([type1, type2], labels = labels, colors=colors, autopct='%.2f %%')
#plt.title('W w pierwszym czy drugim typie jest więcje pokemonow trawiastych')
#plt.show()

#kolejny wykres kołowy
#x = df.loc[(df['Type 1'] == 'Dragon') & (df.Legendary == True)].count()[0]
#y = df.loc[(df['Type 1'] == 'Dragon') & (df.Legendary == False)].count()[0]
#smoki = ['Legendarne pokemony smocze','Zwykłe pokeomony smocze']
#plt.pie([x,y], labels=smoki)
#plt.show()

#print(df.loc[(df['Type 1'] == 'Dragon') & (df.Legendary == False)].count()[0])
#df.groupby(['Type 1']).value_counts().Grass.plot(y, kind='pie')
#y = df.Legendary[df.Legendary == True].count()
#print(df.loc[(df['Type 1'] == 'Dragon') & (df.Legendary == True)].value_counts())
#dfdragon = df['Type 1'] == 'Dragon'
#dflegend = df['Legendary'] == True
#print(df[dfdragon & dflegend])

#data = {
#    'Product': ['Box', 'Bottles', 'Pen', 'Markers', 'Bottles', 'Pen', 'Markers', 'Bottles', 'Box', 'Markers', 'Markers',
#                'Pen'],
#    'State': ['Alaska', 'California', 'Texas', 'North Carolina', 'California', 'Texas', 'Alaska', 'Texas',
#              'North Carolina', 'Alaska', 'California', 'Texas'],
#    'Sales': [14, 24, 31, 12, 13, 7, 9, 31, 18, 16, 18, 14]}
#df1 = pd.DataFrame(data, columns=['Product', 'State', 'Sales'])
#x = df1.groupby(['State'])['Sales'].sum()
#x.plot.bar()
#plt.show()


df2 = pd.DataFrame({'continent' : ['Asia','NorthAmerica','NorthAmerica','Europe','Europe', 'Europe','Asia', 'Europe', 'Asia'],
               'country' : ['China', 'USA', 'Canada', 'Poland', 'Romania', 'Italy', 'India', 'Germany', 'Russia'],
               'GDP(trillion)' : np.random.randint(1, 9 , 9),
               'Member_G20' : np.random.choice(['N', 'Y'], 9)})

#print(df2)
#grp=df.groupby(['continent'])
#selected_group = grp.get_group('Europe')
#print(selected_group[selected_group['Member_G20']=='Y'])
#print(selected_group[selected_group['Member_G20']=='Y']['GDP(trillion)'].sum())

#selected_group = grp.get_group('Asia')
#print(selected_group[selected_group['Member_G20']=='Y'])
#print(selected_group[selected_group['Member_G20']=='Y']['GDP(trillion)'].sum())

plt.subplot(1, 2, 1)
wykres = df2.groupby(['continent']).apply(lambda x: x[x['Member_G20'] == 'Y' ]['GDP(trillion)'].sum())
wykres.plot.bar()
plt.subplot(1, 2, 2)
wykres1 = df2.groupby(['continent']).apply(lambda x: x[x['Member_G20'] == 'N' ]['GDP(trillion)'].sum())
wykres1.plot.bar()
plt.show()