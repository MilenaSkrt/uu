''''
Найти значение определенного интеграла sin(x) по 3 методам численного интегрирования: метод прямоугольника, метод трапеций и метод Симпсона.
Построить график значений ( y(x) - I(x)), где y(x) - определенный интеграл sin(x), вычисленный 3 методами, а I(x) - 1 - cos(x)
'''
import sympy
import numpy as np
import math
import matplotlib.pyplot as plt

x = sympy.Symbol('x')
def f(x):
    return sympy.sin(x)

''''
Метод Симпсона
'''

def simpson(left, right, n, function):
    h = (right - left) / n
    area = 0
    x = left
    for i in range(n - 1):
        area +=(function(x) + 4*function(x + h/2) + function(x + h))*(h/6)
        x += h
    return area

''''
Метод прямоугольников
'''

def rectangle (left, right, n, function):
    dx = (right - left) / n
    area = 0
    x = left
    for i in range(n-1):
        area += dx * function(x)
        x += dx
    return area
''''
Метод трапеций
'''

def trapezoid (left, right, n, function):
    h = (right - left) / n
    area = 0
    x = left
    for i in range(n-1):
        area += h * (function(x) + function(x + h)) / 2
        x += h
    return area


def s(y):
    return simpson(0,y,5,f)

def IntCos(y):
    return math.cos(y)-1

h = simpson(0,2* math.pi,2000 ,f)

h2 = trapezoid(0,2* math.pi,2000 ,f)
def h(y):
    return simpson(0, y, 100, f )

def h1(y):
    return rectangle(0, y, 100, f )

def h2(y):
    return trapezoid(0, y, 100, f )

t = np.linspace(0, 2 * np.pi, 100)
h_val = [h(val)-(1-math.cos(val)) for val in t]
h1_val = [h1(val)-(1-math.cos(val)) for val in t]
h2_val = [h2(val)-(1-math.cos(val)) for val in t]
plt.plot(t, h_val)
plt.plot(t, h1_val)
plt.plot(t, h2_val)
plt.show()

'''
t = np.linspace(0, 2 * np.pi, 100)
plt.plot(t, [h1]*len(t))
plt.show()
'''


