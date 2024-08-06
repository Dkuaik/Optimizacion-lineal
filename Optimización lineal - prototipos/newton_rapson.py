# Optimización de una función lineal por el metodo de Newton-Rapson


import sympy
import numpy as np
import matplotlib.pyplot as plt

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


f= '(x-5)**2'
x0 = 10
epsilon = 0.1
n = 100
registro=newton_rapson(f, x0, epsilon, n)
for i in registro:
    print("iteracion ", i[0], " x: ", i[1], " f(x): ", i[2], " f'(x): ", i[3])

#imprimir función
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Grafica de la convergencia de la función a optimizar
for element in registro:
    ax1.plot(element[0], element[2], 'ro', label="f'(c)")
ax1.set_xlabel('Iteraciones')
ax1.set_ylabel('f(c)')
ax1.grid()
# ax1.legend()

# Grafica de la convergencia del valor del punto medio
for element in registro:
    ax2.plot(element[0], element[1], 'bo', label='c')
ax2.set_xlabel('Iteraciones')
ax2.set_ylabel('c')
ax2.grid()
# ax2.legend()
plt.show()