# Limpiar la pantalla antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que pide al usuario un número entero y muestra en pantalla si es par o impar

# Solicitar al usuario que ingrese un número entero
numero = int(input("Introduce un número entero: "))
# Verificar si el número es par o impar utilizando el operador módulo
if numero % 2 == 0:
    # Si el resto de la división entre 2 es 0, el número es par
    print("El número " + str(numero) + " es par")
else:
    # Si el resto de la división entre 2 no es 0, el número es impar
    print("El número " + str(numero) + " es impar")
