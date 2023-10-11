# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:37:34 2023

@author: hecto
"""

#TECNM/ITA
#M en C en Ing Amb
#Modelado de sistemas ambientales complejos
#Unidad 4
#Métodos numéricos en la solución de modelos ambientales complejos
#Ejercicio 2
#Evaluación de derivada hacia adelante de un conjunto de una función, 
#modificando el tamaño del incremento en el tiempo

#Vamos a usar una función que define la retención de un reservorio
#de agua

#declaramos las librerias
import numpy as np
import matplotlib.pyplot as plt

#Definir algunos parámetros del modelo
A = 1000 #volumen del reservorio (L)
B = 5    #Velocidad de llenado del reservorio (adimensional)
C = 1    #constante de tiempo (1/s)

#definimos en que pto queremos evaluar la derivada y el incremento
dt = 0.01   #este valor entre más pequeño, mejor. Pero OJO, no tanto xd
t = 10      #segundos

#definimos la función
def reservorio(A,B,C,t):
    R = A/(1 + B*np.exp(-C*t))
    return R

#vamos a definir una función para evaluar la derivada de la función
def derivada_num(A,B,C,t,dt):
    dRdt = (reservorio(A,B,C,t+dt) - reservorio(A,B,C,t))/dt
    return dRdt

#ahora definiremos la derivada analitica para comparar el error
#entre la aproximación numerica y analitica
def derivada_an(A,B,C,t):
    R = A*B*C*np.exp(-C*t)/(1+B*np.exp(-C*t))**2
    return R

#vamos a declarar un vector de incrementos de "t" para evaluar como
#el incremento afecta al error en la evaluación de la derivada
dt = np.arange(0.0000000000001, 2, 0.1)

#evaluamos el error entre la analitica y la numerica
error = abs((derivada_num(A,B,C,t,dt) - derivada_an(A,B,C,t))/derivada_an(A,B,C,t))*100

#graficar el error entre la función analitica y numerica en función
#del incremento de la derivada
plt.plot(dt,error)
plt.xlabel('$\Delta t$')
plt.ylabel('% Error')
plt.grid()
plt.title('Error de la evaluación de la derivada en t = ' + str(t) + ' s')
