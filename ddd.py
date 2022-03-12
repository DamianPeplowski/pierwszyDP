import math
import sys
import random

print(sys.version)
# print('Damian')
#a = 5
#b = 15
# print(b**a)
# print(a-b)
# print(a*b)
# print(a+b)
# print(b/a)
# print(b//a)
# print(math.pow(a, b))
# print('potegowanie')
# musi byc nawias bo inaczej  3 bedzie do potegi
# print((2/3) ** a)
# print(math.pow(2/3, a))
#
# c = 12.3
# print(c)
# d = 3+2j
# print(d)
#
# e = 'Bardzo pomysłowy komentarz'
# print(e)
#
# print(a+c)
# print(type(e))
#nazwa_zmiennej-wartosc

# f = 'Wizualizacja'
# g = ' danych'
# print(f+g)



# if warunek 1 - instrukcja warunek 1
# elif warunek 2 - instrukcja warunek 2
# else warunek n - instrukcja warunek n else instrukcja
# x==y x!=y x>y x<y x>=y x<=y

# a = 7
# b = 9
#
# if a > b:
#     print('liczba a jest wieksza od liczby b')
# elif a < b:
#     print('liczba a jest mniejsza od b')
# else:
#     print('liczby sa równe')

# a = input("Podaj liczbę a: ")
# b = input("Podaj liczbę b: ")
# c = input("Podaj liczbę c: ")
# d = input("Podaj liczbę d: ")
# print(a)
# print(b)
# print(c)
# print(d)

# print(type(a))
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a > b) & (c > d):
#     print('liczba a jest wieksza od liczby b i liczba c jest wieksza od liczby d')
# else:
#     print('liczba a nie jest wieksza od liczby b lub liczba c nie jest wieksza od liczby d')

# Pętla for | for licznik in sekwencja
#   instrukcja lub blok instrukcji
#else:
#    instrukcje po zakonczeniu działania pętli
# czesto wykorzystywany przy range(start,stop,step)
#start-element początkowy
#stop-element koncowy
#step-kroki o ile zmieniamy element startowy i koncowy

# for i in range(0, 6, 1):
#     print(i)

# lista = ['Napis',3,4,5.6]
# for element in lista:
#     print(element)
# else:
#     print('wyświetlanie elementów z listy zostało zakończone')

#while warunek(wykonywana dopoki warunek ejst spełniony)
#     instrukcja lub blok instrukcji
#     instrukcja
#else
#    instrukcja lub blok instrukcji po zakończeniu dziaałania pętli

# licznik = 0
# while licznik !=10:
#     print(licznik)
#     licznik += 1
# else:
#     print('zostało wyświetlonych '+ str(licznik) + ' liczb')

#funkcja break przerywa pętle

# lista = [4, 6, 2, 3, 5, 9, 1]
# liczba = input("wczytaj liczbę: ")
# licznik = 0
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print(liczba + "-" + str(lista[licznik]) + ' =0')
#         break
#     else:
#         licznik += 1
# else:
#     print("żadna z liczb, które są w liście nie dął odpowiedniego wyniku")

# lista = [4, 6, 2, 3, 5, 9, 1]
# lista2 = [7, 3, 4, 6]
# suma = []
# for a in lista:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# try
#     operacja np int(wartości)
#     instrukcje
# except nazwa błędu
#     instrukcja co ma byc zrobione gdy napotkamy błąd
# else błąd instrukcji bez błędu

# liczba1 = input('podaj pierwszą liczbę')
# liczba2 = input('podaj drugą liczbę')
# try:
#     wynik = int(liczba1) / (liczba2)
#      print('wynik = ' + str(wynik))
# except ZeroDivisionError:
#       print('Nie dzeli się przez 0')
# except ValueError:
#      print('Nie wczytano liczby całkowitej')
#

# lista = ['cos', 4, 23, 5, 6, 7, [1, 2, 3]]
# print(lista)
# print(lista[5])
# lista.append(9)
# print(lista)
# lista.insert(1, 'element')
# print(lista)
# lista.pop(7)
# print(lista)
# lista.remove('element')
# print(lista)
# lista.extend(11, 22, 33)
# print(lista)

#słownik = {1: 22, 'klucz':'wartość', 3.4: 5 }
##słownik[4] = 45
#print(słownik)
#słownik.pop(4)
#print(słownik)
#print(słownik.keys())
#print(słownik.values())

#del słownik[1]
#print(słownik)

#zad1


#lab3 zad1
print("Zad1")
a = [1 - x for x in range(11)]
b = [2**i for i in range(8)]
c = [x for x in b if x/2 ]
print(a)
print(b)
print(c)
#lab3 zad2
print("Zad2")

lista1 = [138, 2, 13, 334, 545,876, 337, 568, 9, 10 ]
lista = []
lista2 = [i for i in lista1 if i % 2 ==0]
print(lista2)
#lab3 zad3 nieskonczone
print("Zad3")
produkty = {"Jajka": "sztuki", "Mięso wieprzowe": "kg", "Ser": "kg"}
print(produkty)
#lab3 zad4
print("Zad4")
a2 = int(input("wpisz liczbę a: "))
b2 = int(input("wpisz liczbę b: "))
c2 = int(input("wpisz liczbę c: "))

if ((a2+b2>c2) and (a2+c2>b2) and (b2+c2>a2)):
    if ((a2*a2+b2*b2==c2*c2) or (a2*a2+c2*c2==b*b2) or (c2*c2+b2*b2==a2*a2)):
        print("To jest trójkąt prostokątny")
    else:
        print("To nie jest trójkąt prostokątny")
else:
    print("Nie można zbudować trójkąta")

#lab3 zad5
print("Zad5")
a1 = 1
b1 = 2
h = 3
P = (a1+b1)*h
Pt = P/2
print(Pt)
#lab3 zad6
print("Zad6")
#lab3 zad7
print("Zad7")
#lab3 zad8
print("Zad8")
zakupy = {"Sok owocowy":"2.99","Pomarańcze":"6.99"}
print(zakupy)
#lab3 zad9
print("Zad9")
#lab3 zad10
print("Zad10")
#zapisz otworz go do pliku
for i in range(100):
    if i % 4 == 0:
        print(i)

#lab3 zad11
print("Zad11")

plik = open("wypisywanie.txt", "r")



