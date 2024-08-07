import random

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
            if cadena[i+1]==0:
                cadena[i+1]=1
            else:
                cadena[i+1]=0
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
    return seleccionados