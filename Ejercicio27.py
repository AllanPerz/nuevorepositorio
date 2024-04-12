# Limpia la pantalla de la terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que solicita al usuario un número entero positivo
# y muestra en pantalla la cuenta regresiva desde ese número hasta cero, separados por comas.
numero_usuario = int(input("Introduce un numero entero positivo: "))

# Bucle que realiza la cuenta regresiva
for contador in range(numero_usuario, -1, -1):
    print(contador, end=" , ")
