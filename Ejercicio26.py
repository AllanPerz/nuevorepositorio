# Limpiar la pantalla para mejor visualización del programa
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que solicita al usuario su edad y muestra todos los años cumplidos
edad_usuario = int(input("¿Cuántos años tienes? "))
# Bucle para mostrar cada año cumplido
for anio in range(edad_usuario):
    print("Has cumplido " + str(anio+1) + " años")
