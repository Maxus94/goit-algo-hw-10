import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np
import random

print("Defined integral for function x**3")
points_total = int(input('Enter number of points: '))
a = int(input('Enter lower boundary: '))
b = int(input('Enter upper boundary: '))

def f(x):
    return x ** 3

result, error = spi.quad(f, a, b)

print("Інтеграл quad: ", result, error)

points_inside = 0

points = [(random.uniform(a, b), random.uniform(0, b**3)) for _ in range(points_total)]
for point in points:
    if point[1] <= point[0] ** 3:
        points_inside += 1      
print("Monte-Karlo integral:", (points_inside / points_total) * (b-a) * f(b))

x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

for point in points:
    if point[1] <= point[0] ** 3:
        ax.scatter(point[0], point[1], color ='green', s = 2)       
    else:
        ax.scatter(point[0], point[1], color ='red', s = 2)


ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^3 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

