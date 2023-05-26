import pandas as pd
import numpy as np

notas = pd.Series({"Economia":27, "Calculo":40, "C.Sociales":25, "Programacion":30, "Lenguas":32, "Etica":40})
print(notas)
print("")
print("------------------------------")
print("Aplicaciones de SERIES: ")
print("")

print(notas["Calculo"]) #Escribir el nombre del elemento o la posicion del elemento en la Array

print(notas.count()) #Devuelve el numero de elementos en la lista (no cuenta elementos nulos)

print(notas.sum()) #Realiza la suma de todos los valores numericos de los elementos

print(notas.min()) #Arroja el valor minimo de los elemntos

print(notas.max()) #Arroja el valor maximo de los elementos 

print(notas.mean()) #Arroja el promedio o media de los elementos

print(notas.describe()) #IMPORTANTE: Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles.

print("------------------------------")
print("")

# Aplicar operaciones a las series de PANDAS

#se les puede aplicar operaciones normales, como si fueran vectores
#Ejemplo:
print("")
print("Calculos con series: ")
print("------------------------------")

unoo = notas/notas.max()
print(unoo)
print("-------------------------------")
# Aplicacion de condicionales:
print("")
print("Condicionales: ")
print("")

print("--------------------------------")
print("Notas superiores a 30:")
print(notas[notas>30])
print("---------------------------------")
print("")


print("---------------------------------")
print("Orden N (Min-Max): ")
print(notas.sort_values(ascending=True))  #Organiza los valores de forma CRECIENTE
print("Orden N (Max - Min): ")
print(notas.sort_values(ascending=False)) #Organiza los valores de forma DECRECIENTE
print("---------------------------------")

print("")

print("---------------------------------")
print("Orden A-Z: ")
print(notas.sort_index(ascending=True))  #Organiza la serie en orden alfabetico (De A-Z)
print("Orden Z-A: ")
print(notas.sort_index(ascending=False)) #Organiza la serie en orden alfabetico al contrario (De Z-A)
print("---------------------------------")




