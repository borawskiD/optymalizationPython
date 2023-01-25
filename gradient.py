from sympy import *
import numpy as np
from matplotlib import pyplot as plt
import math


def f(x):
    return x ** 2 - 4 * x


def f_prim(x):
    x_symbol = Symbol('x')
    y_prim = f(x_symbol).diff(x_symbol)
    return eval(str(y_prim))

def drawBasicGraph(min, max):
    a = min
    while a < max:
        plt.plot(a, f(a), 'k,')
        a+=0.1
    plt.plot(a, f(a), 'k,', label="f(x)")


drawBasicGraph(-25, 25)
learning_rate = 0.1
max_iterations = 100
epsilon = 0.00001
x0 = np.random.uniform(-25, 25)
plt.plot(x0, f(x0), 'rx')
current_precision = 1
counter = 0
while current_precision > epsilon and counter < max_iterations:
    old_x = x0
    x0 = x0 - learning_rate * f_prim(x0)
    current_precision = math.fabs(x0 - old_x)
    print("Iteration number: " + str(counter))
    print("Current x0: " + str(x0) + " f(x0) = " + str(f(x0)))
    plt.plot(x0, f(x0), 'b.')
    counter+=1

print("Znalezione minimum:")
print("Dla x: " + str(x0))
print("f(x): " + str(f(x0)))
plt.plot(x0, f(x0), 'b.', label="Punkty po drodze")
plt.plot(x0, f(x0), 'rv', label="Minimum lokalne")
plt.title("Metoda gradientowa")
plt.legend()
plt.show()

