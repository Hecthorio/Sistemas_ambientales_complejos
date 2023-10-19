# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:58:14 2023

@author: hecto
"""

#TECNM/ITA
#M. en C. en Ing. Amb.
#Modelado de sistemas ambientales complejos
#Unidad 4
#Métodos numéricos en la solución de modelos ambientales complejos
#Ejercicio 4
#La parte baja del río Colorado consiste en una serie de 
#cuatro almacenamientos.
#Puede escribirse los balances de masa para cada uno de ellos,
#lo que da por resultado el conjunto siguiente de ecuaciones 
#algebraicas lineales simultáne

#definir el sistema de ecuaciones
def sist_ec(c1o,c2o,c3o,c4o):
    c1 = 750.5/13.42
    c2 = (300 + 13.422*c1o)/12.252
    c3 = (102 + 12.252*c2o)/12.377
    c4 = (30 + 12.377*c3o)/11.797
    return c1,c2,c3,c4

#definir las condiciones iniciales
c1o = 1
c2o = 1
c3o = 1
c4o = 1
error = 1000
n = 0   #contador

print('{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}'.format('n','c1','c2','c3','c4','error'))
print('{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}'.format(n, round(c1o,2), round(c2o,2), round(c3o,2), round(c4o,2), error))

#aplicar el método de Gauss-Seidel
while error > 0.00001:
    c1, c2, c3, c4 = sist_ec(c1o,c2o,c3o,c4o)
    error = abs((c1-c1o)/c1)*100 + abs((c2-c2o)/c2)*100 + abs((c3-c3o)/c3)*100 + abs((c4-c4o)/c4)*100
    c1o = c1*1
    c2o = c2*1
    c3o = c3*1
    c4o = c4*1
    n = n + 1
    print('{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}'.format(n, round(c1o,2), round(c2o,2), round(c3o,2), round(c4o,2), error))
    if n > 100:
        break

##############################################################################
#Otra manera de solucionar puede ser dar de alta la matriz de coeficientes   #
#y el vector solución.                                                       #
##############################################################################

#importamos libreria
import numpy as np

#damos de alta la matriz de coeficientes y solución
A = np.array([[13.42,    0,      0,      0],
              [-13.422,  12.252, 0,      0],
              [0,       -12.252, 12.377, 0],
              [0,        0,     -12.377, 11.797]])

B = np.array([750, 300, 102, 30])

#damos de alta los valores iniciales y lista donde se
#guardaran los datos nuevo
co = np.array([1, 1, 1, 1])
c = []

#damos de alta variables auxiliares
n = 0
error = 1000
sumatoria = 0

#imprimimos el encabezado de la tabla
#OJO el * sirve para desempaquetar la lista generada
#: indica que se aplica un formato a la cadena de texto
#< indica que el texto se alinea a la izquierda
#8 indica que se dejan 8 espacios
#generamos los titulos de la tabla sumando listas
titulos = ['n'] + ['c' + str(i + 1) for i in range(len(B))] + ['error']

#imprimimos el encabezado, desempaquetando (*) la lista con el formato
print(*[f'{i:<8}' for i in titulos])

#generamos una variable que tiene los valores de co conectando str con join
valores = ' '.join([f'{round(i,2):<8}' for i in co])

#imprimimos los valores junto con n y el error sumando str
print(f'{n:<8} ' + valores  + f' {round(error,2):<8}')

#aplicamos el algoritmo de Gauss-Seidel
#filas (i), columnas (j)
while error > 0.0001:
    for i in range(len(B)):
        for j in range(len(B)):
            sumatoria = sumatoria + A[i][j]*co[j]
        c.append((B[i] - sumatoria + A[i][i]*co[i])/A[i][i])
        sumatoria = 0
    c = np.array(c)
    error = sum(abs((c - co)/c)*100)
    co = c*1
    n = n + 1
    c = []
    valores = ' '.join([f'{round(i,2):<8}' for i in co])
    print(f'{n:<8} ' + valores  + f' {round(error,2):<8}')
    if n > 100:
        break