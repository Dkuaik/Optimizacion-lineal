# Optimización de una función lineal por el método de fibonacci

import sympy
import numpy as np
import matplotlib.pyplot as plt

def fibonacci(f: str, a: float, b: float, epsilon: float, n: int) -> list:
    """
    Calculates the optimal point and the value of a function using the Fibonacci method.

    Parameters:
    f (str): The function to be optimized as a string.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    epsilon (float): The desired accuracy of the optimal point.
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the logs of every iteration.

    """
    # Convertir la función de cadena a una función simbólica
    x = sympy.symbols('x')
    f = sympy.sympify(f)
    
    # Generar la secuencia de Fibonacci
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    
    # Inicializar los puntos x_a y x_b
    L = b - a
    x_a = a + (fib[n-1] / fib[n]) * (L)
    x_b = b - (fib[n-1] / fib[n]) * (L)
    
    # Evaluar la función en los puntos x_a y x_b
    f1 = f.subs(x, x_a)
    f2 = f.subs(x, x_b)
    
    # Registro de primera iteración
    registro = [[1, a, b, x_a, x_b, f1, f2]]
    k=1
    # Iterar hasta que el intervalo sea menor que epsilon o se alcance el número máximo de iteraciones
    while k < n:
        if f1 > f2:
            a = x_a
            x_a = a + (fib[n-k-1] / fib[n]) * (b - a)
            x_b = b - (fib[n-k-1] / fib[n]) * (b - a)
            f1 = f2
            f2 = f.subs(x, x_b)
        else:
            b = x_b
            x_b = x_a
            x_a = a + (fib[n-k-2] / fib[n-k]) * (b - a)
            f2 = f1
            f1 = f.subs(x, x_a)
        registro.append([k+1, a, b, x_a, x_b, f1, f2])
        
        # Verificar si el intervalo es menor que epsilon
        if abs(b - a) < epsilon:
            break
    
    return registro

# Definir las condiciones iniciales
f = "x**2"  # Función a optimizar
a = 0  # Límite inferior del intervalo
b = 5  # Límite superior del intervalo
epsilon = 0.01  # Precisión deseada
n = 10  # Número de iteraciones máximas

# Calcular el resultado utilizando el método de Fibonacci
resultado = fibonacci(f, a, b, epsilon, n)

# Imprimir el resultado
for iteracion in resultado:
    print(f"Iteración {iteracion[0]}:")
    print(f"Intervalo: [{iteracion[1]}, {iteracion[2]}]")
    print(f"Punto óptimo: {iteracion[3]}")
    print(f"Valor óptimo: {iteracion[5]}")
    print()