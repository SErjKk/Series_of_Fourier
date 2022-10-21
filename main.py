import math
import numpy as np
import matplotlib.pyplot as plt

# ВВОД НАЧАЛЬНЫХ УСЛОВИЙ, ВЫЧИСЛЕНИЕ И ПОСТРОЕНИЕ ГРАФИКОВ
def PLOT():
    k = str(input('Введите тип ряда Фурье (G - общий, С - по cos, S - по sin): '))
    x_min = int(input('Введите минимальное значение x: '))
    x_max = int(input('Введите максимальное значение x: '))
    n = int(input('Введите значение n для частичной суммы: '))
    print(' ')

    label = '$0.5x, x\in [0,2)$ \n' \
            '$1, x\in [2,4]$'

    dx = (x_max - x_min) * 100
    x = np.linspace(x_min, x_max, dx)

    plt.title('Вычисление тригонометрических рядов Фурье')
    plt.xlabel('Coordinate X')
    plt.ylabel('Coordinate Y')
    plt.grid(True)

    if k == "G":
        y_1 = [y_f1(i, n) for i in x]
        y_0 = [y_f0(i) for i in x]
        plt.plot(x, y_1, color='crimson', label = "ряд Фурье")
        plt.plot(x, y_0, color='dimgray', linestyle='--', label = label)
    if k == "C":
        y_0cos = [y_f0cos(i) for i in x]
        y_1cos = [y_f1cos(i, n) for i in x]
        plt.plot(x, y_1cos, color='crimson', label = "ряд Фурье")
        plt.plot(x, y_0cos, color='dimgray', linestyle='--', label = label)
    if k == "S":
        y_0sin = [y_f0sin(i) for i in x]
        y_1sin = [y_f1sin(i, n) for i in x]
        plt.plot(x, y_1sin, color='crimson', label = "ряд Фурье")
        plt.plot(x, y_0sin, color='dimgray', linestyle='--', label = label)
    plt.legend()
    plt.show()

# ФУНКЦИИ ДЛЯ SIN
def y_f0sin(x_f0):
    if 4 > x_f0 >= 0:
        if 2 > x_f0 % 4 > 0:
            return x_f0 % 4 / 2
        else:
            if 2 <= x_f0 % 4 < 4:
                return 1
    if x_f0 >= 4:
        if 0 <= (x_f0 - 4) % 8 < 2:
            return -1
        if 2 <= (x_f0 - 4) % 8 < 4:
            return (x_f0 % 4 / 2) - 2
        if 4 <= (x_f0 - 4) % 8 < 6:
            return (x_f0 % 4) / 2
        if 6 <= (x_f0 - 4) % 8 < 8:
            return 1
def y_f1sin(x_f1sin, n_f):
    s = 0
    if x_f1sin % 4 == 0:
        return 0
    else:
        for i in range(1, n_f):
            s += (((2 * (2 * math.sin(math.pi * i * 0.5) - math.pi * i * math.cos(math.pi * i * 0.5))) / (
                        (math.pi ** 2) * (i ** 2))) +
                  ((2 * (math.cos(math.pi * i * 0.5) - math.cos(math.pi * i))) / (math.pi * i))) * math.sin(
                math.pi * i * x_f1sin * 0.25)
        return s

# ФУНКЦИИ ДЛЯ COS
def y_f0cos(x_f0):
    if 4 > x_f0 >= 0:
        if 2 > x_f0 % 4 > 0:
            return x_f0 % 4 / 2
        else:
            if 2 <= x_f0 % 4 < 4:
                return 1
    if x_f0 >= 4:
        if 0 <= (x_f0 - 4) % 8 < 2:
            return 1
        if 2 <= (x_f0 - 4) % 8 < 4:
            return (-(x_f0 % 4) / 2) + 2
        if 4 <= (x_f0 - 4) % 8 < 6:
            return (x_f0 % 4) / 2
        if 6 <= (x_f0 - 4) % 8 < 8:
            return 1
def y_f1cos(x_f1cos, n_f):
    s = 0
    for i in range(1, n_f):
        s += ((((2 * ((math.pi * i * math.sin(math.pi * i * 0.5)) + 2 * math.cos(math.pi * i * 0.5) - 2)) / (
                    (math.pi ** 2) * (i ** 2))) -
               (2 * (math.sin(math.pi * i * 0.5)) / (math.pi * i))) * math.cos(math.pi * i * x_f1cos * 0.25))
    s += 0.75
    return s

# ФУНКЦИИ ДЛЯ ОБЩЕГО СЛУЧАЯ
def y_f0(x_f0):
    if 2 > x_f0 % 4 > 0:
        return (x_f0 % 4) / 2
    else:
        if 2 <= x_f0 % 4 < 4:
            return 1
        else:
            return 0.5
def y_f1(x_f1, n_f):
    s = 0
    if x_f1 % 4 == 0:
        return 0.5
    else:
        for i in range(1, n_f):
            s += (((((-1) ** i) - 1) * math.cos(math.pi * x_f1 * i * 0.5)) / ((math.pi ** 2) * (i ** 2)) - math.sin(
                math.pi * x_f1 * i * 0.5) / (math.pi * i))
        s += 0.75
        return s

while True:
    PLOT()