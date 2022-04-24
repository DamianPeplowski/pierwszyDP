import numpy as np

#zad1
print("Zad1")
a = np.arange(start=3, stop=48, step=3)
print(a)
#zad2
print("Zad2")

lista = [0.49, 11.78, 0.94, 56.35, 787.95, 33.54, 4.55, 9.55, 1.54]
print([int(lista) for lista in lista])

#zad3
print("zad3")

p = []
for i in range(10):
    p.append(np.arange(10*i, 10*(i+1)))

p = np.array(p)
print(p)

#zad5
print("zad5")

w=[13,25,65]
odw=w[::-1]

d = np.diag(odw)
print(d)

#zad6
print("zad6")




#zad8

#zad9
print("Zad9")
n, m = 5, 5

macierz = np.zeros((n, m), dtype=int)
macierz[0 // m][0 % m] = 0
macierz[1 // m][1 % m] = 1

pr = 0
p = 1

for i in range(2, n * m):
    c = pr + p
    macierz[i // m][i % m] = c
    pr = p
    p = c

print(macierz)
