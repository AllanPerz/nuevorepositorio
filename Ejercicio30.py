import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que pide al usuario un número entero positivo mayor que 2 y muestra por pantalla si es un número primo o no.
numero = int(input("Introduce un número entero positivo mayor que 2: "))
divisor = 2
# Se verifica si el número es divisible por algún número entre 2 y él mismo.
while numero % divisor != 0:
    divisor += 1
# Si el divisor es igual al número, significa que no se encontraron divisores y por lo tanto es primo.
if divisor == numero:
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo")
