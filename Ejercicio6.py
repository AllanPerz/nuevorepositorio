# Limpiar la pantalla antes de comenzar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que te pide ingresar una palabra y la imprime 10 veces

# Solicitar al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")
# Utilizar un bucle for para imprimir la palabra 10 veces
for i in range(10):
    print(palabra)
