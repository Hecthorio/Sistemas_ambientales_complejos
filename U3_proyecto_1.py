# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:19:48 2023

@author: hecto
"""

#TECNM/ITA
#M en C en Ing Amb
#Modelado de sistemas ambientales complejos
#Unidad 3
#Modelos microscopicos
#Ejercicio 1
#Modelo que define el perfil de fracciones molares de un contaminante
#evaporandoce dentro de un pozo

#declaramos librerias
import matplotlib.pyplot as plt
import numpy as np

#Datos (CF)
z1 = 0      #m
z2 = 1      #m
xA1 = 0.99  #adimen
xA2 = 0.01   #adimen

#declaramos nuestra función
def frac_mol_A(z,z1,z2,xA1,xA2):
    xA = 1 - (1 - xA1)*((1-xA2)/(1-xA1))**((z-z1)/(z2-z1))
    xB = 1 - xA
    return xA, xB

#declarar los valores de z que se van a evaluar
z = np.arange(z1, z2 + 0.05, 0.05)

#evaluar los valores de xA paea cada valor de z
xA, xB = frac_mol_A(z, z1, z2, xA1, xA2)

#graficamos el perfil de fracciones molares
plt.plot(z,xA, label = '$x_A$', marker = 's', markerfacecolor = 'None')
plt.plot(z,xB, label = '$x_B$', marker = '^')
plt.plot([0,1],[1,1], 'k--', label = '$x_A + x_B = 1$')
plt.legend()
plt.xlabel('Distancia (m)')
plt.ylabel('Fracción mol')
plt.title('Perfil de concentraciones de los componentes A y B')
plt.show()