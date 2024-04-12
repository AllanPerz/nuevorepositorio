# Limpiar la pantalla de la terminal antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que almacena en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8
# y muestra en pantalla el menor y el mayor de los precios.
prices = [50, 75, 46, 22, 80, 65, 8] # Lista de precios
min = max = prices[0] # Inicializar las variables min y max con el primer precio de la lista
for price in prices: # Recorrer la lista de precios
    if price < min: # Si el precio actual es menor que el mínimo actual
        min = price # Actualizar el mínimo
    elif price > max: # Si el precio actual es mayor que el máximo actual
        max = price  # Actualizar el máximo
# Imprimir el precio mínimo y máximo
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))