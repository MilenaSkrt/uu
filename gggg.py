import sympy
import matplotlib.pyplot as plt

x = sympy.Symbol('x')

def f(x):
    return sympy.sin(x) * x

def simpson(left, right, n, function):
    h = (right - left) / (2 * n)

    tmp_sum = function(left) + function(right)

    for step in range(1, 2 * n):
        if step % 2 != 0:
            tmp_sum += 4 * function(left + step * h)
        else:
            tmp_sum += 2 * function(left + step * h)

    return tmp_sum * h / 6

def s(y):
    return simpson(0, y, 5, f)

y_values = [25, 32, 34, 20, 25]
s_values = [s(val) for val in y_values]

plt.plot(y_values, s_values)
plt.xlabel('y')
plt.ylabel('Integral of f(x) from 0 to y')
plt.title('Plot of Integral of f(x) from 0 to y')
plt.grid(True)
plt.show()
