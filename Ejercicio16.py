# Limpia la pantalla de la terminal antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que almacena las asignaturas de un estudiante en una lista y la muestra en pantalla.

# Lista de asignaturas
Clases = ["Administración I", "Español I", "Matematicas", "Introduccion a la Ingenieria Computacional", "Analisis y Diseño de Algoritmos"]
# Imprime la lista de asignaturas en pantalla
print(Clases)