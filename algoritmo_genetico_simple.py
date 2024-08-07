# Algoritmo genetico simple aplicado a la funciones sugeridas por el aritulo
# The Genetic Algorithm for finding the maxima of single-variable functions.
# Funciones especificadas en el archivo txt

import random
import sympy
from operadores_geneticos import * 
import numpy as np
import matplotlib.pyplot as plt

class Individuo:
    def __init__(self, x: float, aptitud: float):
        """
        Inicializa un nuevo individuo con un valor x y su aptitud correspondiente.
        
        :param x: Valor del individuo.
        :param aptitud: Aptitud del individuo.
        """
        self.x = x
        self.aptitud = aptitud
        self.bits = 0

    def __str__(self):
        """
        Devuelve una representación en cadena del individuo.
        
        :return: Cadena que representa al individuo.
        """
        return f'valor: {self.x}, aptitud: {self.aptitud}, binario: {self.bits}'

    def __repr__(self):
        """
        Devuelve una representación oficial en cadena del individuo.
        
        :return: Cadena que representa al individuo.
        """
        return f'Individuo({self.x}, {self.aptitud}, binario: {self.bits})'

# Operador de cruza de punto 

def cruza_punto(padre1:str, padre2:str, punto:int)->list:
    """
    Operador de cruza de punto
    :param padre1: cadena de bits del padre 1
    :param padre2: cadena de bits del padre 2
    :param punto: punto de cruza (debe ser un entero valido en el intervalo [1,longuitud-1] de los padres)
    :return: lista con los hijos
    """
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return [hijo1, hijo2]

# Operador de mutacion de bit

def mutacion_bit(cadena:str, probabilidad:float)->list:
    """
    Operador de mutación de bit
    :param cadena: cadena de bits a mutar
    :param probabilidad: probabilidad de mutación
    :return: cadena de bits mutada
    """
    cadena = list(cadena)
    for i in range(len(cadena)-2):
        if random.random() < probabilidad:
            if cadena[i+1]=='0':
                cadena[i+1]='1'
            else:
                cadena[i+1]='0'
    cadena=''.join(cadena)
    return cadena

# Operador de seleción por ruleta

def seleccion_ruleta(poblacion: list, aptitudes: list,num_seleccionados:int) -> list:
    """
    Operador de selección por ruleta
    :param poblacion: lista de individuos
    :param aptitudes: lista de aptitudes correspondientes a los individuos
    :param num_seleccionados: número de individuos a seleccionar
    :return: lista de individuos seleccionados
    """
    # poblacion=[list(i) for i in poblacion]
    # Calcular la suma total de las aptitudes
    suma_aptitudes = sum(aptitudes)
    
    # Calcular la probabilidad de selección para cada individuo
    probabilidades = [aptitud / suma_aptitudes for aptitud in aptitudes]
    
    # Calcular la probabilidad acumulada
    prob_acumulada = []
    acumulado = 0
    for prob in probabilidades:
        acumulado += prob
        prob_acumulada.append(acumulado)
    
    # Seleccionar individuos
    seleccionados = []
    for i in range (num_seleccionados):
        r = random.random()
        for j in range(len(prob_acumulada)):
            if r < prob_acumulada[j]:
                seleccionados.append(poblacion[j])
                break
    return seleccionados

def evaluar_aptitud(f:str, x:float) -> float:
    """
    Evalua una funcion en un punto
    :param f: funcion a evaluar
    :param x: punto a evaluar
    :return: valor de la funcion en el punto
    """
    x = sympy.Symbol('x')
    f = sympy.sympify(f)
    f = sympy.lambdify(x, f)
    return f(x)+100000

def float_to_bin(x:float, inicio_intevalo)->str:
    """
    Convierte un numero flotante positivo a binario
    :param x: numero flotante
    :param inicio_intevalo: inicio del intervalo de busqueda
    :return: cadena de bits
    """
    x-=inicio_intevalo
    return bin(int(x*10**16))[2:]

def bin_to_float(x:str,inicio_intervalo)->float:
    """
    Convierte una cadena de bits a un numero flotante
    :param x: cadena de bits
    :param inicio_intervalo: inicio del intervalo de busqueda
    :return: numero flotante
    """
    if isinstance(x, list):
        x=''.join(x)
    if isinstance(x, int):
        x=bin(x)[2:]
    return int(x,2)/10**16+inicio_intervalo

def algoritmo_genetico_simple(f:str, n:int, n_generaciones:int, p_c:float, p_m:float, intv_busq:list) -> list:
    """
    Algoritmo genetico simple para optimizar una funcion
    :param f: funcion a optimizar
    :param n: numero de individuos
    :param n_generaciones: numero maximo de generaciones
    :param p_c: probabilidad de cruza
    :param p_m: probabilidad de mutacion
    :param intv_busq: Intervalo de busqueda
    :return: lista de arrays con el registro de iteraciones [n-iteración, aptitud, individuo]
    """
    suma_aptitud_positiva=100000
    Longitud = intv_busq[1]-intv_busq[0]
    x= sympy.Symbol('x')
    f= sympy.sympify(f)
    f= sympy.lambdify(x,f)
    hist_por_generacion = []
    new_gen = []
    # Inicializar poblacion
    poblacion = []
    for _ in range(n):
        individuo = Individuo(random.uniform(intv_busq[0],intv_busq[1]),0)
        individuo.aptitud=f(individuo.x)+suma_aptitud_positiva
        individuo.bits = float_to_bin(individuo.x, intv_busq[0]) #transformacion lineal para pasar a binario
        poblacion.append(individuo)
    # print(poblacion)
    hist_por_generacion.append(poblacion)
    n_gen=0
    # apareamiento
    while n_gen < n_generaciones:
        n_gen+=1
        # Evaluacion
        # for individuo in poblacion:
        #     individuo.aptitud = f(individuo.x)+100000
        # Selección
        aptitudes = [individuo.aptitud for individuo in poblacion]
        # Cruza
        for _ in range(n//2):
            padres=seleccion_ruleta(poblacion, aptitudes, 2)
            if random.random() < p_c:
                punto_random = random.randint(1, len(padres[0].bits)-1) #generacion del punto de corte
                hijos=cruza_punto(padres[0].bits, padres[1].bits, punto_random)
                hijo1 = Individuo(bin_to_float(hijos[0], intv_busq[0]),0)
                hijo1.bits=hijos[0]
                hijo2 = Individuo(bin_to_float(hijos[1], intv_busq[0]),0)
                hijo2.bits=hijos[1]
            else:
                hijo1 = padres[0]
                hijo2 = padres[1]
            new_gen.append(hijo1)
            new_gen.append(hijo2)
        # mutacion
        for individuo in new_gen:
            individuo.bits=mutacion_bit(individuo.bits, p_m)
            individuo.aptitud = f(individuo.x)+suma_aptitud_positiva
        poblacion = new_gen
        new_gen = []
        # Calcular aptitud promedio de la generación
        hist_por_generacion.append(poblacion)
        # print(f'Generación {n_gen} completada, aptitud promedio: {np.mean([individuo.aptitud for individuo in poblacion])}')
    return hist_por_generacion


f= '-(x**6+x**5-10*x**2-10*x-12)/(x**2+6)'
# Ejecutar el algoritmo genético
evolucion = algoritmo_genetico_simple(f, 50, 100, 0.8, 0.1, [-4, 4])

# Graficar generaciones contra aptitud promedio
generaciones = range(1, len(evolucion) + 1)
val_optimo=-100000000
aptitud_optima=0
x= sympy.Symbol('x')
f= sympy.lambdify(x,sympy.sympify(f))
f_optima=[]
for generacion in evolucion:
    for individuo in generacion:
        if individuo.aptitud>aptitud_optima:
            aptitud_optima=individuo.aptitud
            val_optimo=individuo.x
    mejor_individuo = max(generacion, key=lambda individuo: individuo.aptitud)
    f_optima.append(f(mejor_individuo.x))
print('El punto optimo es:', val_optimo,'El valor optimo es',f(val_optimo), 'con aptitud:', aptitud_optima)
plt.plot(generaciones, f_optima)
plt.xlabel('Generaciones')
plt.ylabel('Valor optimo')
plt.show()

# Escribir la historia de las generations en un archivo
with open('historia_generaciones.txt', 'w') as f:
    for i, generacion in enumerate(evolucion):
        f.write(f'Generación {i + 1}\n')
        for individuo in generacion:
            f.write(f'{individuo}\n')
        f.write('\n')