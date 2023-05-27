import pandas as pd

plantillaP = pd.read_csv(
'Plantilla_pruebaPANDAS.csv', sep=';', decimal=',')
                         


plantilla = plantillaP.head()

print(plantilla)

print("----------------")

print("")
print("")
print("Plantilla de info: ")

plantilla.info()

print("----------------")

print("")

sz = plantilla.size
print(sz)
print("----------------")

print("")


n = 3

print(plantilla.head(n))  #Devuelve las n primeras filas del DataFrame df.

print("")

print(plantilla.tail(n))  #Devuelve las n últimas filas del DataFrame df.

print("----------------")

print("")
print("")
print("Asignar cabecera a las columnas:")


print(plantilla.set_index("Pto").head())



print("--------------------------------")
print("")




plantilla['Signo-Elevacion'] = pd.Series([True, True, True, False, True])

print(plantilla)
print("")
