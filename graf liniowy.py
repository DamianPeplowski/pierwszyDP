import matplotlib.pyplot as plt
import numpy as np

X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X,Y)
plt.xlabel('X os')
plt.ylabel('Y os')
plt.title('Linia')
plt.show()

x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel('os X')
plt.ylabel('os Y')
plt.title('Linia zlamana')
plt.show()

x1 = [10,20,30]
y1 = [20,40,10]

x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x1,y1, color='blue', linewidth=3, label='Linia grb 3')
plt.plot(x2,y2, color='Yellow', linewidth=5, label='Linia grb 5')
plt.xlabel('Os X')
plt.ylabel('Os Y')
plt.title('Dwie linie')
plt.legend()
plt.show()


t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()

X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
print(plt.axis())
plt.axis([0, 100, 0, 200])
plt.show()

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
# create data
x = [1, 2, 3, 4, 5]
y = [3, 3, 3, 3, 3]
# plot lines
plt.plot(x, y, label="line 1", linestyle="-")
plt.plot(y, x, label="line 2", linestyle="--")
plt.plot(x, np.sin(x), label="curve 1", linestyle="-.")
plt.plot(x, np.cos(x), label="curve 2", linestyle=":")
plt.legend()
plt.show()

#with open('tekst.txt') as f:
#    data = f.read()
#data = data.split('\n')
#x = [row.split(' ')[0] for row in data]
#y = [row.split(' ')[1] for row in data]
#plt.plot(x,y)
#plt.xlabel('Os X')
#plt.ylabel('Os Y')
#plt.title('Graf z tekstu')
#plt.show()

