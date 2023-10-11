# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:16:36 2023

@author: hecto
"""
#TECNM/ITA
#M en C en Ing Amb
#Modelado de sistemas ambientales complejos
#Unidad 4
#Métodos numéricos en la solución de modelos ambientales complejos
#Ejercicio 1
#Evaluación de derivada hacia adelante de un conjunto de datos

#librerias
import pandas as pd

#leer base de datos de concentracion (si se usa .to_numpy el arreglo
#se convierte de un df a un array de numpy)
df = pd.read_csv('datos_con.csv').to_numpy()

#generamos una lista donde guardaremos las derivadas
dcdt = []

#Evaluar las derivadas a partir del siguiente ciclo
for i in range(len(df)-1):
    dcdt.append((df[i+1,0]-df[i,0])/(df[i+1,1]-df[i,1]))

#NOTA, EL RESULTADO DE LAS DERIVADAS EVALUADAS DE ESTA FORMA DEPENDE MUCHO!!
#DEL LOS INCREMENTOS EN LOS INTERVALOS NUMERICOS, OJO!!! ENTRE MÁS CORTO
#EL INTERVALO MEJOR
