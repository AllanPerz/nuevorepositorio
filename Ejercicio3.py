# Limpiar la pantalla de la terminal antes de comenzar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitar al usuario dos números para realizar una división
numero1= float(input("Introduce el dividendo: "))
numero2 = float(input("Introduce el divisor: "))

# Verificar si el divisor es cero para evitar un error de división por cero
if numero2 == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    # Si el divisor no es cero, realizar la división e imprimir el resultado
    print(numero1/numero2)   
