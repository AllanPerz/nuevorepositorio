# Limpia la consola antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Este programa nos pide introducir una oracion y una letra 
# Y muestra en la consola cuantas veces aparece la letra en la oracion

# Solicita al usuario que introduzca una frase
Oracion = input("Introduce una frase: ")
# Solicita al usuario que introduzca una letra
Letra = input("Introduce una letra: ")
# Inicializa el contador de apariciones de la letra en 0
contador = 0
# Recorre cada caracter de la oración
for i in Oracion:
    # Si el caracter actual es igual a la letra buscada
    if i == Letra:
        # Incrementa el contador
        contador += 1
# Imprime en consola la cantidad de veces que aparece la letra en la oración
print("La letra ' %s ' aparece %2i veces en la frase '%s'." % (Letra, contador, Oracion))
