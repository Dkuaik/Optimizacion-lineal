# optimización de la función a traves de la seccion dorada
# no basado en la derivada de la función

import sympy
import numpy as np
import matplotlib.pyplot as plt
import math

def seccion_dorada(f:str,a:float,b:float,epsilon:float,n:int)->list:
    """
    Metodo de la seccion dorada para optimizar una función
    :param a: valor inicial (cota inferior del intervalo de busqueda)
    :param b: valor inicial (cota superior del intervalo de busqueda)
    :param epsilon: tolerancia
    :param n: numero maximo de iteraciones
    :return: lista de arrays con el registro de iteraciones [n-iteración, a_n, b_n, c_n, d_n, f(c_n), f(d_n)]
    """
    phi=2/(math.sqrt(5)-1)
    print(phi)
    tao=2-phi
    registro = []
    x = sympy.Symbol('x')
    f = sympy.sympify(f)
    f = sympy.lambdify(x, f)
    num_iteraciones = 1
    while num_iteraciones <= n: #condición sobre numero máximo de iteraciones
        alpha1 = a * (1-tao) + b * tao
        alpha2 = a * tao + b * (1-tao)
        registro.append([num_iteraciones,a,b,alpha1,alpha2,f(alpha1),f(alpha2)]) #registro de iteraciones
        if abs(alpha1 - alpha2) < epsilon: #prueba de convergencia
            return registro
        if f(alpha1) < f(alpha2):
            b = alpha2
        else:
            a = alpha1
        num_iteraciones += 1
    return registro

f= '(x-5.56465)**2+5*x-8'
a = 10
b = 20
epsilon = 0.1
n = 100
registro=seccion_dorada(f, a, b, epsilon, n)
for i in registro:
    print("iteracion ", i[0], " a: ", i[1], " b: ", i[2], " alpha1: ", i[3], " alpha2: ", i[4], " f(alpha1): ", i[5], " f(alpha2): ", i[6])