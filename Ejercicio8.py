# Limpiar la pantalla antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programa que pregunta al usuario una cantidad a invertir, el interés anual y el número de años.
# Y muestra en pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Solicitar al usuario la cantidad a invertir
cantidad = float(input("¿Cantidad a invertir? "))
# Solicitar al usuario el interés anual
interes = float(input("¿Interés porcentual anual? "))
# Solicitar al usuario el número de años
años = int(input("¿Años?"))
# Calcular el capital obtenido cada año y mostrarlo en pantalla
for i in range(años):
    cantidad *= 1 + interes / 100  # Actualizar la cantidad con el interés anual
    print("Capital tras " + str(i + 1) + " años: " + str(round(cantidad, 2)))  # Mostrar el capital tras cada año
