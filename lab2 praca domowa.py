
import sys as system
import math
from tkinter import E

#zadanie1

listaa = ['box', 'MMA', 'Koszykówka', 'Piłka Nożna']
listaa.reverse()
print(listaa)
listaa.extend(('hokej', 'skoki narciarskie'))
print(listaa)

#zadanie2
slownik = {'tys': 'tysiąc', 'zł':'złotówka', 'UE': 'Unia Europejska', 'TSUE': 'Trybunał Sprawiedliwości Unii Europejskiej'}
print(slownik)
#zadanie3
gry = {'Wiedzmin 3':'250h','TES:Skyrim':'350h','God of War':'100h','Horizon Zero Dawn':'80h','Dark Souls:Trilogy':'220h'}
print(gry)
print(len(gry.keys()))
#zadanie4

system.stdout.write("Wpisz dowolne zdanie: ")
napis = system.stdin.readline()
system.stdout.write(napis)
print('Liczba pojawiających sie liter a: ', napis.count('a'))

#zadanie5
a = int(input("wpisz liczbę a: "))
b = int(input("wpisz potęgę b: "))
c = int(input("wpisz liczbe c która zostanie dodana: "))
d = (a**b)+c
print("Równanie ma wynik: ", d)

#zadanie6
x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
z = int(input("Podaj trzecią liczbę: "))

if x > z and x > y:
    print("Pierwsza liczba jest największa")
elif y > z and y > z:
    print("Druga liczba jest największa")
elif z > x and z > y:
    print("Trzecia liczba jest największa")

#zadanie7

int = [5, 23, 12, 876, 67, 6]
kwadrat = [ ]
for i in int:
    prw = i * i
    kwadrat.append(prw)
    print("Kwadrat {} to {}".format(i, prw))

float=[0.23,0.45,2.34,8.54,4.52,1.23]
kwadrat2 = [ ]
for i in float:
    prw1 = i * i
    kwadrat2.append(prw1)
    print("Kwadrat {} to {}".format(i, prw1))
#zadanie8
#zadanie9



