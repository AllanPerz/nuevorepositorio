# Limpiar la pantalla de la consola antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programa que pregunta por consola por los productos de una canasta de la compra, separados por comas,
# Y muestra por pantalla cada uno de los productos en una línea distinta.

# Solicitar al usuario que ingrese los productos de la canasta de la compra
canasta = input('Introduce los productos de la canasta de la compra separadas por comas: ')
# Reemplazar las comas por saltos de línea y mostrar los productos en líneas separadas
print(canasta.replace(',', '\n'))
