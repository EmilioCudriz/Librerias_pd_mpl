# Creacion de Dataframe a partir de diccionarios 

import pandas as pd

nombres_list = []
edad_list = []
asignatura_list = []
promedio_list = []

nn = int(input("Agrega el numero de datos que deseas introducir: "))

for i in range(0,nn):
    nombre_ = (input("Nombre: "))
    nombres_list.append(nombre_)
    
    edad_ = int(input("Edad: "))
    edad_list.append(edad_)
    
    asignatura_ = (input("Asignatura: "))
    asignatura_list.append(asignatura_)
    
    promedio_ = float(input("Calificacion: "))
    promedio_list.append(promedio_)
    
    i = i + 1
    
datos = {" Nombre":nombres_list, " Edad":edad_list, " Asignatura":asignatura_list, " Calificacion":promedio_list}
    
notas = pd.DataFrame(datos)

print(notas)


    