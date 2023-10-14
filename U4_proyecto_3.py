# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:17:27 2023

@author: hecto
"""

#TECNM/ITA
#M. en C. en Ing. Amb.
#Modelado de sistemas ambientales complejos
#Unidad 4
#Métodos numéricos en la solución de modelos ambientales complejos
#Ejercicio 3
#Evaluación del nivel de oxígeno, concentración (mg/L), en un río 
#aguas abajo de la descarga de un drenaje, aplicando el método de newton-raphson.

#librerias
import numpy as np
import matplotlib.pyplot as plt

#definimos la función que modela este sistema
#(OJO, la función está iguala a cero)
def fun_zero(c,x):
    f = 10-20*(np.exp(-0.15*x) - np.exp(-0.5*x)) - c
    return f

#definimos la derivada de la función anterior
def der_fun_zero(c,x):
    df = -20*(-0.15*np.exp(-0.15*x) + 0.5*np.exp(-0.5*x))
    return df

#vamos a declarar la concentración y evaluamos a que distancia
#tenemos esa concentración del contaminante
xo = 2       #km (valor inicial)
c = 5        #mg/L
n = 0        #contador


#evaluamos la función con la condición inicial
f = fun_zero(c,xo)          #evaluamos la función

#definimos el algotimos del método de newton-raphson
while abs(f) > 0.000001:
    df = der_fun_zero(c, xo)    #evaluamos derivada de la fun
    xi = xo - f/df              #evaluamos el nuevo valor
    print(xo)                   #imprimimos el valor de xo en c/iteración
    xo = xi*1                   #actualizamos el valor de x
    if n > 100:
        break
    n = n + 1
    f = fun_zero(c,xo)          #evaluamos la función

#vamos a graficar la función y posicionar el pto que encontramos (raíz)
#generar un vector de valores en x (distancia)
x = np.arange(0,10,0.1)

#evaluar al función con los valores de x (distancia)
#OJO, sumamos c porque la función esta definida para
#determinar una raíz y no concentración
con = fun_zero(c, x) + c

#graficamos la función
plt.plot(x, con, '-o', color = 'k', markerfacecolor = 'w', label = 'Perfil de concentración')
plt.plot([0,xo],[f+c, f+c], '--', color = 'b')
plt.plot([xo,xo],[0, f+c], '--', color = 'b')
plt.plot(xo, c, 's', color ='r', label = 'C = ' + str(round(f+c,4)) + ' mg/L \n' + 'x = ' + str(round(xo,4)) + ' km')
plt.legend()
plt.xlim(0,3)
plt.ylim(0,10)
plt.xlabel('Distancia (km)')
plt.ylabel('Concentración ($mg/L$)')
plt.title('Nivel de oxígeno en un río aguas abajo de la descarga de un drenaje')