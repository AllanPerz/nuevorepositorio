import os
os.system('cls' if os.name == 'nt' else 'clear') # Limpia la pantalla de la terminal
#Programa que pide al usuario un número entero 
#Y muestra en pantalla un triángulo rectángulo de altura el número introducido.
altura = int(input("Introduce la altura del triángulo (entero positivo): ")) # Pide al usuario la altura del triángulo

# Bucle que recorre cada fila del triángulo
for fila in range(altura):
    # Bucle que recorre cada columna de la fila actual
    for columna in range(fila+1):
        print("*", end="") # Imprime un asterisco sin salto de línea
    print("") # Salto de línea para pasar a la siguiente fila
