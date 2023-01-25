import math
import numpy as np
from matplotlib import pyplot as plt
def f(x):
    return 0.1 * x ** 2 - 4 * x - 100 * math.sin(x) + 4 * math.exp(2)

def drawBasicGraph(min, max):
    a = min
    while a < max:
        plt.plot(a, f(a), 'k.', markersize='1')
        a+=0.1
    plt.plot(a, f(a), 'k.', label="f(x)")


x0 = np.random.uniform(-20,20)
globalMin = x0
T = 2500.0
C = 0.995
f0 = f(x0)
counter = 0
drawBasicGraph(-45,30)
plt.plot(x0, f(x0), 'bx', label="Punkt poczatkowy", markersize='7')
while T > 1:
    x1 = x0 + np.random.uniform(-1,1)
    f1 = f(x1)
    P = np.exp(-(f1-f0)/T)
    if f1 < f0 or P > np.random.uniform(0,1):
        x0 = x1
        f0 = f1
        if T > 2.0:
            plt.plot(x0, f(x0), 'r.', markersize='2')
        else:
            plt.plot(x0, f(x0), 'b.', markersize='2')
        if f(x0) < f(globalMin):
            globalMin = x0
    T = T * C
    print("Iteration number: " + str(counter))
    print("Current min")
    print("x = " + str(x0))
    print("f(x) = " + str(f0))
    counter+=1
plt.plot(x0, f(x0), 'r.', markersize='1', label="Punkty przebyte")
plt.plot(x0, f(x0), 'b.', markersize='1', label="Punkty dla T<2")
plt.plot(globalMin, f(globalMin), 'gv', markersize='5', label="Minimum")
plt.legend()
plt.title("Symulowane wyzarzanie")
plt.savefig('annealing.png', dpi=1000)
plt.show()
