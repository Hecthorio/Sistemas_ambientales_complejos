# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:03:35 2023

@author: hecto
"""

#TecNM/ITA
#M. en C. en Ing Amb
#Modelado de sistemas ambientales complejos
#Unidad II
#ejercicio 2

#script para determinar perfil de concentraciones de un 
#sistema dinamico

#librerias
import numpy as np
import matplotlib.pyplot as plt
import time as tm

#Datos del sistema
V = 500     #m3
k = 0.4     #1/h
m = 140     #mg/h
Q = 1000    #m3/h

#definimos nuestra función
def con_bar(m,Q,k,V,t):
    c = m/(Q + k*V)*(1 - np.exp(-(Q + k*V)/V*t))
    return c

#elaborar el vector de periodos de tiempo que usaremos
#para la evaluación de la concentración
t = np.arange(0,7,0.1)

#evaluar la concentración
c = con_bar(m,Q,k,V,t)

#vector con los valores de flujo volumetrico
Q = np.arange(0,2100,450)

#graficar
for i in range(len(Q)):
    #evaluamos la concentración con ese flujo volumetrico
    c = con_bar(m, Q[i], k, V, t)
    #checar que se este tomando el valor adecuado
    print(Q[i])
    #graficamos
    plt.plot(t,c, label = 'Q = ' + str(Q[i]))
    plt.legend()
    plt.xlabel('Tiempo (h)')
    plt.ylabel('Concentración ($mg/m^3$)')
    plt.title('Concetración formaldehido en un bar')
plt.show()

#generamos unas matrices de flujo contaminantes y flujo
#volumetrico para generar una superficie de respuesta
m = np.arange(0,180,5)
Q = np.arange(0,2100,25)

#generamos las matrices
m, Q = np.meshgrid(m,Q)

#evaluar las concentraciones (matriz)
c = con_bar(m, Q, k, V, 4)

#obtener la grafica de superficie
fig = plt.figure(figsize = (10,8))
ax = plt.axes(projection = '3d')

superficie = ax.plot_surface(m, Q, c, cmap = 'viridis')
fig.colorbar(superficie, ax=ax, shrink=0.5, aspect=5)
ax.set_xlabel('Flujo formaldehido (mg/h)', fontsize = 14)
ax.set_ylabel('Flujo aire (m3/h)', fontsize = 14)
ax.set_zlabel('Concentración de formaldehido (mg/m3)', fontsize = 14)
ax.set_title('Superficie de respuesta (formaldehido)', fontsize = 18)
plt.show()

#evaluar las c_max y c_min en equilibiro
c_max = max(con_bar(m,Q,k,V,t[-1]).flatten())
c_min = min(con_bar(m,Q,k,V,t[-1]).flatten())

plt.figure()
#vamos a graficar una figura de contorno
for i in range(len(t)):
    c = con_bar(m,Q,k,V,t[i])
    plt.clf()    
    plt.contourf(m, Q, c, levels = np.linspace(c_min,c_max,100), vmax = c_max, vmin = c_min, cmap = 'turbo', extend = 'both')
    plt.xlabel('Emisión de formaldehido ($mg/h$)')
    plt.ylabel('Flujo volumentrico de aire fresco ($m^3/h$)')
    plt.draw()
    plt.colorbar().set_label('Concentración de formaldehido ($mg/m^3$)')
    plt.pause(0.1)
