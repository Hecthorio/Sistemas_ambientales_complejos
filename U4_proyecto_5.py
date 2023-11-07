# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:29:44 2023

@author: hecto
"""

#TECNM/ITA
#M. en C. en Ing. Amb.
#Modelado de sistemas ambientales complejos
#Unidad 4
#Métodos numéricos en la solución de modelos ambientales complejos
#Ejercicio 5
#Estimar el flujo de agua a partir de datos historicos de precipitación pluvial.
#Este analsis se aborda aplicando la definición de una interpolación lineal

#importar las librerias
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#leer la base de datos
#damos de alta la ruta y el nombre del archivo
ruta = 'C:/Users/hecto/OneDrive/Documentos/ITA/Modelación Sist. Ambientales Complejos AGO-DIC 2023/datos/'
nombre_archivo = 'precipitacion.csv'

#ahora si, leemos el archivo
df = pd.read_csv(ruta + nombre_archivo)

#definir la función para obtener la interpolación
def inter_lin(fxo, fx1, xo, x1, x):
    y = fxo + (x - xo)*(fx1 - fxo)/(x1 - xo)
    return y

#definimos el valor de la precipitación para evaluar el flujo
preci = 102

#nuestos datos de la base de datos NO estan ordenados
#vamos a ordenarlos 1ro con la siguiente función
df = df.sort_values('precipitacion')

#filtrar los datos que sean mayores y menores a "preci"
a = df['precipitacion'] < preci
a = df[a]
a = a.iloc[-1]
xo = a.iloc[0]
fxo = a.iloc[1]

a = df['precipitacion'] > preci
a = df[a]
a = a.iloc[0]
x1 = a.iloc[0]
fx1 = a.iloc[1]

#vamos a mandar llamar la función para evaluar el flujo
flujo = inter_lin(fxo,fx1,xo,x1,preci)

#graficamos la información
plt.plot(df['precipitacion'], df['flujo'], '--o', label = 'Datos historicos')
plt.plot(preci,flujo,'^', markersize = 12, markerfacecolor = 'None', label = 'Precipitación ' + str(round(preci,2)) + 'cm\n' +
         'Flujo ' + str(round(flujo,2)) + '$m^3/s$')
plt.legend()
plt.xlabel('Precipitación (cm)')
plt.ylabel('Flujo ($m^3/s$)')