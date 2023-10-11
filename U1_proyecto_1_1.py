# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:29:33 2023

@author: hecto
"""

#TecNM, ITA
#M en C en ingenieria ambiental
#Modelado de sistemas ambientales complejos
#Unidad II
#Ejercicio 1.1
#Hectorio

#Continuación del ejercicio 1 (determminación de la concentración
#de un contaminante en función de las entradas).

#librerias
import matplotlib.pyplot as plt

#declramos las corrientes de entrada con sus concentraciones y corrientes
#de salida
Ve = [10, 5, 10, 20, 50]    #flujos a la entrada, (m3/s)
Ce = [20, 40, 50, 0.4, 0]   #concentraciones de los flujos de entrada (mg/L)

#declaramos nuestra función
def con(V,C):
    Vs = sum(V)     #sumatoria de los flujos
    suma = 0        #contador
    #generamos los productos de los flujos con las concentraciones
    for i in range(len(V)):
        suma = V[i]*C[i] + suma
    #evaluamos la concentración
    Cs = suma/Vs
    return Cs

Con_sal = con(Ve,Ce)

#la concentración de la corriente a la salida
print('El resultado de la concentración a la salida es: ' + str(round(Con_sal,4)) + ' mg/L')
print('El número de corrientes fue de: ' + str(len(Ve)))

#vamos a modificar una de las corrientes den entrada
Con_sal = []                            #lista donde se guardaran las concentraciones
Vx = [0, 10, 20, 50, 100, 150, 200, 500, 800, 1200, 1800, 2000]     #flujos volumetricos variables
posicion = 2                            #esta parametro define que flujo vol varia

#evaluamos la función con los diferentes flujos volumetricos
for i in range(len(Vx)):
    Ve[posicion] = Vx[i]
    Con_sal.append(con(Ve,Ce))
    
#graficamos
plt.plot(Vx,Con_sal, '-o', markerfacecolor = 'None', color = 'black')
plt.axhline(max(Ce), color = 'r', linestyle = '--')
plt.xlabel('Flujo volumetrico ($m^3/s$) de la corriente ' + str(posicion))
plt.ylabel('Concentración (mg/L)')
plt.title('Flujo volumetrico num ' + str(posicion) + ', concentración = ' + str(Ce[posicion]) + ' mg/L')
plt.ylim(0,max(Ce) + 10)