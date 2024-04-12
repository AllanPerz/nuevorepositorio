# Limpia la pantalla de la consola antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear') 

# Programa que almacena las asignaturas de un estudiante en una lista y la muestra en pantalla
# Yo estudio <Clase>, donde <Clase> es cada una de las asignaturas de la lista.

Clases = ["Administración I", "Español I", "Matematicas", "Introduccion a la Ingenieria Computacional", "Analisis y Diseño de Algoritmos"] # Lista de clases
for asignatura in Clases: # Bucle que recorre la lista de clases
    print("Yo estudio " + asignatura) # Imprime en pantalla la frase con el nombre de cada clase
