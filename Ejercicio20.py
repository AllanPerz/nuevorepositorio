# Limpia la pantalla de la terminal antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Lista de números del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Bucle que recorre la lista de números en orden inverso
for i in range(1, 11):
    # Imprime cada número en orden inverso, seguido de una coma
    print(numeros[-i], end=", ")