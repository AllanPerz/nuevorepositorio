# Limpiar la pantalla de la consola antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que pide al usuario ingresar un número entero positivo
#Y imprime todos los números impares desde 1 hasta ese número separados por comas.

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Utilizar un bucle for para recorrer el rango de números desde 1 hasta el número ingresado
# Incrementando de 2 en 2 para obtener solo los números impares
for i in range(1, numero+1, 2):
    # Imprimir los números impares seguidos de una coma y un espacio
    print(i, end=", ")
