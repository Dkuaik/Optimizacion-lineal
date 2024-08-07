import matplotlib.pyplot as plt
import sympy
import numpy as np
import math

def biseccion(f:str, a:float, b:float, epsilon:float, n:int) -> list:
    """
    Metodo de biseccion para encontrar raices de una funcion
    :param f: funcion a evaluar
    :param a: limite inferior
    :param b: limite superior
    :param epsilon: tolerancia
    :param n: numero maximo de iteraciones
    :return: lista de arrays con el registro de iteraciones [n-iteración, a_n, b_n, c_n, f(c_n)]
    """
    registro = []
    x = sympy.Symbol('x')
    f = sympy.sympify(f)
    d1f = sympy.diff(f, x)
    d1f= sympy.lambdify(x, d1f)
    f = sympy.lambdify(x, f)
    if d1f(a) * d1f(b) > 0:
        return "No hay raiz en el intervalo"
    i = 1
    while i <= n: #condición sobre numero máximo de iteraciones
        registro.append([i, a, b, (a + b) / 2, f((a + b) / 2),d1f((a + b) / 2)]) #registro de iteraciones
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < epsilon: #prueba de convergencia
            return registro
        i += 1
        if d1f(c) * d1f(a) > 0: #Elección del intervalo para siguiente iteración
            a = c
        else:
            b = c
    return registro

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

def newton_rapson(f:str, x0:float, epsilon:float, n:int) -> list:
    """
    Metodo de Newton-Rapson para optimizar una función
    :param f: funcion a evaluar
    :param x0: valor inicial
    :param epsilon: tolerancia
    :param n: numero maximo de iteraciones
    :return: lista de arrays con el registro de iteraciones [n-iteración, x_n, f(x_n), f'(x_n)]
    """
    registro = []
    x = sympy.Symbol('x')
    # definición de la función y sus derivadas
    f = sympy.sympify(f)
    d1f = sympy.diff(f, x)
    d2f = sympy.diff(d1f, x)
    # lambdify para convertir la función simbólica en una función numérica
    f = sympy.lambdify(x, f)
    d1f= sympy.lambdify(x, d1f)
    d2f= sympy.lambdify(x, d2f)
    i = 1
    while i <= n: #condición sobre numero máximo de iteraciones
        registro.append([i, x0, f(x0), d1f(x0)]) #registro de iteraciones
        x1 = x0 - d1f(x0)/d2f(x0)
        if abs(x1 - x0) < epsilon: #prueba de convergencia
            return registro
        x0 = x1
        i += 1
    return registro

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
