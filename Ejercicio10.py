# Limpiamos la consola para tener una mejor visualización de las tablas de multiplicar
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programa que imprime en la consola las tabla de multiplicar del 1 al 10.

# Utilizamos un bucle for para iterar sobre los números del 1 al 10
for i in range(1, 11):
    # Dentro del primer bucle, utilizamos otro bucle for para iterar sobre los números del 1 al 10
    for j in range(1, 11):
        # Imprimimos el resultado de la multiplicación de los dos números i y j
        print(i*j, end="\t") # Usamos end="\t" para separar los resultados con un tabulador
    # Imprimimos un salto de línea para separar cada tabla de multiplicar
    print("")
