# Metodo de biseccion para encontrar el punto que optimiza a la funcion en un intervalo dado 
# A través del método de bisección con una funcion derivable en el intervalo.
# 

import matplotlib.pyplot as plt
import sympy
import numpy as np


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


f= '(x-3)**2'
a = -10
b = 10
epsilon = 0.1
n = 100
registro=biseccion(f, a, b, epsilon, n)
if registro == "No hay raiz en el intervalo":
    print("No hay raiz en el intervalo")
    exit()
for i in registro:
    print("iteracion ", i[0], " a: ", i[1], " b: ", i[2], " c: ", i[3], " f(c): ", i[4], " f'(c): ", i[5])
#imprimir función
# x = sympy.Symbol('x')
# f = sympy.sympify(f)
# f = sympy.lambdify(x, f)
# x = np.linspace(a, b, 100)
# y = f(x)
# plt.plot(x, y)
# plt.grid()
# plt.show()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Grafica de la convergencia de la raiz de la derivada
for element in registro:
    ax1.plot(element[0], element[4], 'ro', label="f'(c)")
ax1.set_xlabel('Iteraciones')
ax1.set_ylabel('f(c)')
ax1.grid()
# ax1.legend()

# Grafica de la convergencia del valor del punto medio
for element in registro:
    ax2.plot(element[0], element[3], 'bo', label='c')
ax2.set_xlabel('Iteraciones')
ax2.set_ylabel('c')
ax2.grid()
# ax2.legend()
plt.show()