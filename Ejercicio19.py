# Limpiar la pantalla antes de comenzar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programa que pide al usuario ingresar una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Introduce una palabra: ")
# Lista de vocales que vamos a buscar en la palabra
vocales = ['a', 'e', 'i', 'o', 'u']
# Recorremos la lista de vocales
for vocal in vocales:
    # Inicializamos el contador de veces que aparece la vocal
    times = 0
    # Recorremos cada letra de la palabra ingresada
    for letter in palabra:
        # Si la letra es igual a la vocal, incrementamos el contador
        if letter == vocal:
            times += 1
    # Mostramos el resultado por pantalla
    print("La vocal " + vocal + " aparece " + str(times) + " veces")  
