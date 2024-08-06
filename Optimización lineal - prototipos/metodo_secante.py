# Metodo de la secante para optimización de funciones lineales

import sympy
import numpy as np
import matplotlib.pyplot as plt

def secante(f:str,a:float,b:float, epsilon:float, n:int) -> list:
    """
    Metodo de la secante para optimizar una función
    :param a: valor inicial (cota inferior del intervalo de busqueda)
    :param b: valor inicial (cota superior del intervalo de busqueda)
    :param epsilon: tolerancia
    :param n: numero maximo de iteraciones
    :return: lista de arrays con el registro de iteraciones [n-iteración, a_n, b_n, c_n, f(c_n)]
    """
    registro = []
    x = sympy.Symbol('x')
    f = sympy.sympify(f)
    d1f = sympy.diff(f, x)
    f = sympy.lambdify(x, f)
    d1f= sympy.lambdify(x, d1f)
    i = 1
    while i <= n: #condición sobre numero máximo de iteraciones
        c = b - d1f(b) * (b - a) / (d1f(b) - d1f(a))
        registro.append([i, a, b, c, f(c),d1f(c)]) #registro de iteraciones
        if abs(d1f(c)) < epsilon: #prueba de convergencia
            return registro
        a = b
        b = c
        i += 1
    return registro

f= '(x-5.56465)**2+5*x-8'
a = 10
b = 20
epsilon = 0.1
n = 100
registro=secante(f, a, b, epsilon, n)
for i in registro:
    print("iteracion ", i[0], " a: ", i[1], " b: ", i[2], " c: ", i[3], " f(c): ", i[4], " f'(c): ", i[5])	