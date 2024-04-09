import numpy as np
import math as math
from math import sqrt


def n_kr(n):
    while n % 4 != 0:
        n = n + 1
    return n


e = 0.001  # Заданная точность
a = 1  # Нижняя граница интегрирования
b = 8  # Верхняя граница интегрирования
# Производим рассчет шага интегрирования
n_np = round((b - a) / (e ** (0.25)))
n = n_kr(n_np)  # Число итераций(округляем до первого числа, кратного четырем)
h = round((b - a) / n, 3)  # Шаг интегрирования
# Заполняем массив данных x и f(x)

x = np.arange(1, 8.01, h).tolist()  # Заполняем список x числами от 1 до 8 с шагом h
k = 0
fx = []  # Создаем пустой список значений функции f(x)
for k in range(0, 1):
    for i in x:
        zn = sqrt(pow(i, 3) + 16)  # Считаем значение функции f(x) в точках из списка x, функция задается самостоятельно
        fx.append(zn)  # Заполняем список fx значениями функции f(x) в указанных точках

Ih1_s1 = 0  # Вспомогательная переменная, элемент формулы Симпсона
Ih1_s2 = 0  # Вспомогательная переменная, элемент формулы Симпсона

for i in range(0, 40):
    if i % 2 != 0:
        Ih1_s1 += fx[i]  # Ссумируем значения функции f(x) в точках с четным номером
    if i % 2 == 0 and i != 40 and i != 0:
        Ih1_s2 += fx[i]  # Ссумируем значения функции f(x) в точках с нечетным номером

Ih1 = h / 3 * (fx[0] + fx[40] + 4 * (Ih1_s1) + 2 * (Ih1_s2))  # Считаем интеграл с шагом h

Ih2_s1 = 0  # Вспомогательная переменная, элемент формулы Симпсона
Ih2_s2 = 0  # Вспомогательная переменная, элемент формулы Симпсона

for i in range(2, 39, 4):
    Ih2_s1 += fx[i]

for i in range(4, 37, 4):
    Ih2_s2 += fx[i]

Ih2 = 2 * h / 3 * (fx[0] + fx[40] + 4 * (Ih2_s1) + 2 * (Ih2_s2))  # Считаем интеграл с шагом 2h

print('Значение определенного интеграла, посчитаного с шагом h равно', Ih1)
print('Значение определенного интеграла, посчитанного с шагом 2h равно', Ih2)

Ih_check = abs(Ih1 - Ih2) / 15  # Оценка точности проведенных вычислений методом Ругне Кутты

if Ih_check < e:
    print('Интеграл посчитан верно, точность составила:', Ih_check, ', что выше, чем заданная точность', e)
else:
    print('Интеграл посчитан неверно, точность составила:', Ih_check, ', что ниже, чем заданная точность', e)
0