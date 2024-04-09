from math import *
from scipy import integrate
import sympy

x = sympy.Symbol('x')
def f(x):
    return sin(x)*x

def simpson(left, right, n, function):
   h = (right - left) / (2 * n)

   tmp_sum = function(left) + function(right)

   for step in range(1, 2 * n):
       if step % 2 != 0:
           tmp_sum += 4 * function(left + step * h)
       else:
           tmp_sum += 2 * function(left + step * h)

   return tmp_sum * h / 6

print(simpson(0,x, 5,f))
