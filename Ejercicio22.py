# Limpiar la pantalla de la terminal antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que guarda en un diccionario los precios de las frutas de la tabla
# Pregunta al usuario por una fruta y un número de kilos
# Muestra en pantalla el precio de ese número de kilos de fruta
frutas = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}

# Solicitar al usuario que ingrese la fruta deseada
fruta = input ('¿Qué fruta quieres? ').title()

# Solicitar al usuario que ingrese la cantidad de kilos deseada
kg = float (input('¿Cuántos kilos? '))

# Verificar si la fruta ingresada está en el diccionario de frutas
if fruta in frutas:
    # Calcular el precio total y mostrarlo en pantalla
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, 'Lps')
else:    
    # Informar al usuario que la fruta no está disponible
    print("Lo siento, la fruta", fruta, "no está disponible.")
