import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

#df = pd.read_csv('recent-grads.csv')
#df.plot(x="Rank", y=["P25th", "Median", "P75th"])
#plt.show()

#cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()
#print(cat_totals)
#cat_totals.plot(kind="bar", fontsize=4)
#plt.show()
#df[df["Major_category"] == "Engineering"]["Median"].plot(kind="hist")
#df1 = pd.read_excel('mieszkania1.xlsx')
#result = df1.groupby(['Rok'])
#for name,group in result:
##    print("\nGrupa")
#    print(name)
#    print(group)
#te na dole działaj i coś zwracają
#print(df1.groupby('Formy budownictwa' == 'komunalne' ))
#print(df1.groupby('Formy budownictwa').size())
#print(df1.groupby('Rok')['Formy budownictwa'].count())
#print(df1.groupby('Rok').agg({'Wartość':['min','max']}))


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#student_data = pd.DataFrame({
#    'school_code': ['s001','s002','s003','s001','s002','s004'],
#    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
#    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
#    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#    'age': [12, 12, 13, 13, 14, 12],
#    'height': [173, 192, 186, 167, 151, 159],
#    'weight': [35, 32, 33, 30, 31, 32],
#    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
#    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#wykres z danymi szkolnymi
#result = student_data.groupby(['school_code'])
#for name,group in result:
#    print("\nGrupa")
#    print(name)
#    print(group)
#print(type(result))
#grupaS = student_data.groupby('school_code').agg({'age':['mean','min','max']})
#print(grupaS)
#wynik = student_data.groupby(['school_code','class'])
#for name,group in wynik:
#    print('\nGrupa')
#    print(name)
#    print(group)
#print('\nSplit the said data on school_code wise:')
#grouped_single = student_data.groupby(['school_code'])
#print("Size of the grouped data - single column")
#print(grouped_single.size())
#print('\nSplit the said data on school_code and class wise:')
#grouped_mul = student_data.groupby(['school_code', 'class'])
#print("Size of the grouped data - multiple columns:")
#print(grouped_mul.size())

df = pd.read_excel('mieszkania1.xlsx')
#print(df.groupby(['Rok']))
#print(df.groupby('Formy budownictwa' == 'komunalne' ))
#print(df.groupby('Formy budownictwa').size())
print(df.groupby('Rok')['Formy budownictwa'].count())
#print(df.groupby('Rok').agg({'Wartość':['min','max']}))
#filt = df['Rok'] == '2018'
#print(df.loc[filt][('Formy budownictwa'=='komunalne')].sum())
print(df.pivot(index = 'Rok',columns = 'Formy budownictwa',values='Wartość').plot(kind='bar',figsize=(6,5)))
plt.xlabel('Rok')
plt.ylabel('Formy budownictwa')
plt.title('% mieszkan w danym roku')
plt.text(6,4,'NrIndeksu', fontsize=10, color='green')
plt.show()
#df = pd.read_csv("alphabetstockdata .csv")
#start_date = pd.to_datetime('2020-4-1')
#end_date = pd.to_datetime('2020-09-30')
#df['Date'] = pd.to_datetime(df['Date'])
#new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
#df2 = df.loc[new_df]
#plt.figure(figsize=(10,10))
#df2.plot(x='Date', y=['Open', 'Close']);
#plt.suptitle('Opening/Closing stock prices of Alphabet Inc.,\n 01-04-2020 to 30-09-2020', fontsize=12, color='black')
#plt.xlabel("Date",fontsize=12, color='black')
#plt.ylabel("$ price", fontsize=12, color='black')
#plt.show()

###PANDAS###
import numpy as np
import pandas as pd
#zad1,2
# plik = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(plik, header=0)
#tylko te rekordy gdzie imion było wiecej niz 1000
# print(df[df.Liczba > 1000])
# print('')
#ten rekord z takim samum imieniem
# print(df[df.Imie == 'RADOSŁAW'])
# print('')
#suma dzieci urodzonych w danym okresie
# print(df.Liczba.sum())
# print('')
#suma dizieci urodzonych w latach 2000 - 2005
# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())
# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# print('')
#Suma urodzonych chłopców i dziewczynek
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#Najbardzie popularne imie dla dziewczynki i chłopca
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
#zad3
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
#lista unikalnych imion sprzedawców
print(df['Sprzedawca'].unique())
print('')
#5 najwyzszych wartości zamówien
print(df.sort_values('Utarg', ascending=False).head(5))
print('')
#suma zamowien dla kazdego kraju
print(df.groupby('Sprzedawca').size())
print('')
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
print(df.groupby('Kraj').size())
print('')
#suma zamowien dla Polski w danym roku
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
      agg({'Utarg': ['sum']}))
print('')
#srednia kwota zamowienia w 2004 roku
print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False)
###WYKRESY####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
# zad1 Wykres liniowy który wyświetla liczbe dzieci urodzonych w danym roku
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot()
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.set_xticks(roczniki)
# wykres.tick_params(axis='x', labelrotation=40)
# wykres.legend()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.title("Liczba urodzonych dzieci dla każdego roku")
# plt.show()
# #zad2 wykres słupkowy który przedstawia sume chłopców i dziewcząt urodzonych
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń')
# wykres.legend()
# plt.xticks(rotation=0)
# plt.title("Liczba urodzonych chłopców i dziewczynek")
# plt.show()
#zad3 dziewczynki i chłopcy z ostatnich urodzeni w ostatnich 5 latach
# grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
# plt.legend()
# plt.show()
#zad4 ilosc zamówien przez poszczególnych sprzedawców
#df = pd.read_csv('zamowienia.csv', delimiter=';')
#policzone = df.groupby('Sprzedawca').size()
#policzone.plot.bar()
#plt.ylabel("liczba zamówień")
#plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
#plt.title('Ilość zamówień sprzedawców')
#plt.show()
#
x = np.arange(1, 21, 1)
plt.plot(x, 1/x, label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 20, 0, 1])
plt.legend()
plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
plt.show()







