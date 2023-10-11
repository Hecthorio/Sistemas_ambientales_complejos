# Sistemas_ambientales_complejos
Este repositorio contiene scripts con *modelos ambientales* donde se abordan problemas relacionados con *métodos numéricos* y *modelado*. Estos scripts los elaboré junto con mis alumnos de la **Maestria en Ciencias en Ingenieria Ambiental** del **ITA**.

<img src = emisiones.jpg>

## Breve descripción de los scripts
* U1_proyecto_1 : En este proyecto se aborda la predicción de la concentración de un contaminante a la salida de una combinación de corrientes con diferentes concentraciones del mismo contaminante. El modelo que define este sistema se puede representar por un balance de materia por componente como se muestra a continuación:
  
$$V \frac{dC}{dt} = \sum_{i=0}^{k} C_{k,i}\dot{V} - C \sum_{j=k+1}^{p}\dot{V_p} + Vr_i $$

El sistema se evalua en estados estacionario.

* **U1_proyecto_1_1** : Aquí se aborda el mismo problema pero generando variaciones en una de las corrientes.
  
* **U2_proyecto_2** : En este script se analiza el cambio de la concentración de formaldehido en un cuarto cerrado con fumadores, este sistema se modela usando el balance de materia pero en estado no estacionario, además de obtener los perfiles de concentración se genera un barrido para analizar como impacta el flujo de aire fresco y la cantidad de emisiones dentro del sistemas.
  
* **U3_proyecto_1** : Un contaminante se difunde dentro de un pozo hasta llegar a la supuerficie, este fenomeno se modela por un balance microscopico definido por el siguiente modelo:

$$ N_{\alpha} = J_{\alpha}^{ * } + x_{\alpha} \sum_{\beta=1}^{N} N_{\beta} = J_{\alpha}^{* } + x_{\alpha} c v^{* } = J_{\alpha}^{* } + c_{\alpha}v^{*} $$

$$ J_{\alpha} = c \mathcal{D}_ {\alpha,\beta} \nabla^2 x_{\alpha}$$

El script regresa los perfiles de concentración de cada uno de los componentes.

* **U4_proyecto_1** : Este script evaluan las derivada de un conjunto de datos (datos_con.csv) discretos aplicando una discretización hacia adelante

$$\frac{df(x)}{dx} \approx \frac{f(x+\Delta x) - f(x)}{\Delta x}$$
  
* **U4_proyecto_2** : Se aplica el Modelo de Retención de Agua en un Reservorio para evaluar la importancia del tamaño del incremento en la evaluación de una derivada numérica. El script muestra el porcentaje de error entre la aproximación y el resultado analitico.

$$R(t) = \frac{A}{1+Be^{-Ct}}$$

## Comentarios
La mayroia de los scripts requeiren modulos de las librerias Numpy y Matplotlib para poder correrlas en el equipo
