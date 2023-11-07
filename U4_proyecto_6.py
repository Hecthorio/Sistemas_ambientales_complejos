# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:52:38 2023

@author: hecto
"""

#TECNM/ITA
#M. en C. en Ing. Amb.
#Modelado de sistemas ambientales complejos
#Unidad 4
#Métodos numéricos en la solución de modelos ambientales complejos
#Ejercicio 6
#Estimación del perfil de concentraciones y temperaturas
#para un reactor de procesamiento por lotes no isotérmico
#por el método de Euler

#importar librerias
import numpy as np
import matplotlib.pyplot as plt

#damos de alta los valores iniciales para el modelo y el tamaño de paso
#o incremento (en el tiempo)
Ti = 15      #centrigrados
ti = 0       #segundos
ci = 1       #gmol/Litro
tf = 2       #segundo
dt = 0.01

#generar un vector con los valores de los tiempo
t = np.arange(ti,tf + dt,dt)

#damos de alta el sistema de ecuaciones
def temp(T,c):
    dT = 1000*np.exp(-10/(T+273))*c-10*(T-20)
    return dT

def con(T,c):
    dc = -np.exp(-10/(T+273))*c
    return dc

#generamos unas listas para guardar nuestra información
m = True
T = []
c = []

#agregar los valores iniciales a las listas
c.append(ci)
T.append(Ti)

#aplicamos el método de euler
for i in t:
    #evaluamos los valores de phi
    phi_1 = con(Ti,ci)
    phi_2 = temp(Ti,ci)
    
    #evaluamos los valores siguientes
    Tn = Ti + phi_2*dt
    cn = ci + phi_1*dt
    
    #definimos si la reacción es exo o endo
    if m == True:
        if Tn>Ti:
            print('La reacción es exotérmica ' + '🔥')
            m = False
        else:
            print('La reacción es endotermica' + '🧊')
            m = False
    
    #guardar la información de la evaluación
    T.append(Tn)
    c.append(cn)
    
    #actualizar los valores
    Ti = Tn*1
    ci = cn*1

#graficamos nuestros resultados
plt.plot(t,T[:-1], '--')
plt.show()
plt.plot(t,c[:-1])
plt.show()
plt.plot(c,T)
plt.show()
