# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:52:10 2023

@author: hecto
"""

#M. en C. en ingenieria ambiental
#Modelado de sistemas ambientales complejos
#Héctor Olmos
#Unidad 1. Balances macroscopicos
#Ejercicio 1

#librerias:
import matplotlib.pyplot as plt

#Evaluación de la concentración de un contaminante
#despues de combinar un par de corrientes.

#Datos
V1 = 10     #flujo volumetrico, m3/s
c1 = 20     #concentración, mg/L
V2 = 5      #flujo volumetrico, m3/s
c2 = 40     #concentración, mg/L

#evaluamos v3
V3 = V1 + V2

#Evaluamos la concentración
c3 = (V1*c1 + V2*c2)/V3

#imprir el resutado en la pantalla
print('El resultado de la concentración es: ' + str(round(c3,3)) + ' mg/L')

#generar una lista
V1 = [0, 5, 10, 15, 20]
c3 = []
V3 = []

#generamos un ciclo para evaluar las concentraciones
for i in range(len(V1)):
    V3.append(V1[i] + V2)
    c3.append((V1[i]*c1 + V2*c2)/V3[i])
    print(i)

#graficar
plt.plot(V1, c3, '-o', color = 'k', markerfacecolor = 'None')
plt.xlabel('Flujo volumetrico, $\dot{V}_{1}$ ($m^3/s$)', fontsize = 14)
plt.ylabel('Concentración a salida, $c_{3}$ ($mg/L$)', fontsize = 14)
plt.title('Concentracion vs Flujo')
