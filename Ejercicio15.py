# Limpiar la consola antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que pide al usuario que introduzca una palabra en la consola y muestre por pantalla la palabra invertida.
Palabra = input("Introduce una frase: ") # Pedir al usuario que introduzca una frase
print(Palabra[::-1]) # Mostrar la frase invertida usando slicing con paso -1
