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
#lab3 zad3
print("Zad3")
produkty = {"Jajka": "sztuki", "Mięso wieprzowe": "kg", "Ser": "kg","Pomarańcze": "sztuki"}
sztuki = {k: v for k, v in produkty.items() if v.startswith('sztuki')}
print(sztuki)
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

a = 1
r = 4
ile = 10
ciag = [(a *(pow(r, (n - 1)))) for n in range(1, ile + 1)]
print(ciag)
#lab3 zad7
print("Zad7")
ciag1 = [a * r ** (n - 1) for n in range(1, ile + 1)]
print(ciag1)
#lab3 zad8
print("Zad8")
#lab3 zad9
print("Zad9")
#lab3 zad10
print("Zad10")

wynik = []
for i in range(0,100):
    if (i % 4 == 0):
        wynik.append(i)
print(wynik)

#lab3 zad11

print("zad11")
plik = open('liczby.txt', 'r')
p = plik.readlines()

print(p)


