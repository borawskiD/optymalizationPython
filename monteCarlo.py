import math
import numpy as np
from matplotlib import pyplot as plt
def F(x):
    return 0.1 * x ** 2 - 4 * x - 100 * math.sin(x) + 4 * math.exp(2)

def drawBasicGraph(min, max):
    a = min
    while a < max:
        plt.plot(a, F(a), 'k,')
        a+=0.1
    plt.plot(a, F(a), 'k,', label="f(x)")

def monteCarlo(min, max, x0, f_x0, number_of_iteration):
    i = 0
    plt.plot(x0, F(x0), 'bx', label="Punkt startowy")
    while i < number_of_iteration:
        x1 = np.random.uniform(min, max)
        if F(x1) < f_x0:
            f_x0 = F(x1)
            x0 = x1
            plt.plot(x1,F(x1), 'b.')
        else:
            plt.plot(x1,F(x1), 'r,')
        i+=1
    plt.plot(x1, F(x1), 'b.', label="Lepsze punkty (po drodze)")
    plt.plot(x1, F(x1), 'r,', label="Odwiedzone punkty")
    plt.plot(x0, F(x0), 'bv', label="Minimum globalne")
    print("Znalezione minimum:")
    print("Dla x: " + str(x0))
    print("f(x): " + str(f_x0))

number_of_iteration = 1000
min = -100
max = 100
x0 = np.random.uniform(min,max)
f_x0 = F(x0)

drawBasicGraph(min,max)
monteCarlo(min,max,x0,f_x0, number_of_iteration)
plt.title("Metoda Monte Carlo")
plt.legend(loc="upper right")
plt.show()

