
# Limpiar la consola dependiendo del sistema operativo
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que pregunta ingresos y edad y te dice si  puedes tributar o no.
#Para tributar debes ser mayor de 18 años y tener ingresos de 1000$ o mas

# Solicitar la edad al usuario
edad = int(input("¿Cual es tu edad? "))

# Solicitar los ingresos mensuales al usuario
ingresos = float(input("¿Cuales son tus ingresos mensuales? "))

# Comprobar si el usuario cumple con los requisitos para tributar
if edad > 18 and ingresos >= 1000:
    print("Tienes que cotizar")
else: 
    # En caso de no cumplir con los requisitos, informar que no debe cotizar
    print("No tienes que cotizar")  
