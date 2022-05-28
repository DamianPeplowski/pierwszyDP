import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Zad1.

x = np.arange(1, 21)
y = 1/x
plt.plot(x, y, label = 'f(x) = 1/x')
plt.axis([1, x.size, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.show()

#Zad2.
x = np.arange(1, 21)
y = 1/x
plt.plot(x, y, 'g>:', label = 'f(x) = 1/x')
plt.axis([0, x.size, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.show()

#Zad3.
x = np.arange(0, 31, 0.1)
sinx = np.sin(x)
cosx = np.cos(x)
plt.plot(x, sinx, 'g', label = 'sin(x)')
plt.plot(x, cosx, 'r', label = 'cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#Zad5.
plt.rcParams['font.size'] = 8
plt.rcParams['figure.figsize'] = [15.0, 5.0]
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header = 0)
#Wykres1
grupa = df.groupby('Plec')
etykiety = list(grupa.groups.keys())
wartosci = list(grupa.agg('Liczba').sum())

plt.subplot(1, 3, 1)
plt.bar(x = etykiety, height=wartosci, color=['green', 'red'])
plt.xlabel('Płeć')
plt.ylabel('Ilość')
plt.title('Ilość narodzonych dziewczynek i chłopców w całym okresie')
#Wykres2
k = df[df['Plec'] == 'K']
kLata = k.groupby('Rok')
kSumaWRoku = list(kLata.agg('Liczba').sum())

m = df[df['Plec'] == 'M']
mLata = m.groupby('Rok')
mSumaWRoku = list(mLata.agg('Liczba').sum())
print(kLata.groups.keys()) #poszczególne lata

plt.subplot(1, 3, 2)
plt.plot(kLata.groups.keys(), kSumaWRoku, 'g', label = 'Kobiety')
plt.plot(mLata.groups.keys(), mSumaWRoku, 'r', label = 'Mężczyźni')
plt.xlabel('Lata')
plt.ylabel('Ilość')
plt.title('Ilość narodzonych kobiet i meżczyzn w każdym roku')
plt.legend()
#Wykres3
grupa = df.groupby('Rok')
etykiety = list(grupa.groups.keys())
wartosci = list(grupa.agg('Liczba').sum())

plt.subplot(1, 3, 3)
plt.bar(x = etykiety, height=wartosci)
plt.xlabel('Lata')
plt.ylabel('Ilość')
plt.title('Suma narodzonych dzieci w każdym roku')
plt.subplots_adjust(hspace=2.5, wspace=0.5)
plt.show()

#Zad6.
df = pd.read_csv('zamowienia.csv', header = 0, sep=';', decimal='.')
print(df)
seria = df.groupby('Sprzedawca')['Sprzedawca'].size()
print(seria)
explode = np.random.randint(0, 5, seria.size) / 10
plt.pie(x = seria, labels = seria.keys(), shadow=True, explode=explode, autopct=lambda pct: "{:2f}%".format(pct))
plt.show()