import numpy as np
import matplotlib.pyplot as plt
#wykres liniowy z 3 liniami
# Sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()
#wykres konczący sie w pół
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
# shows the current axis limits values
print(plt.axis())
# set new axes limits
# Limit of x axis 0 to 100
# Limit of y axis 0 to 200
plt.axis([0, 100, 0, 200])
# Display the figure.
plt.show()
#2 wykresy w kształcie X
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
#kilka wykresów
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

