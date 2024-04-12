import os
# Limpiar la pantalla de la consola antes de ejecutar el programa
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que pregunta al usuario la fecha de su nacimiento en formato día/mes/año y lo muestra en pantalla, el día, el mes y el año.
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")

# Imprimir el día extrayendo los dos primeros caracteres de la cadena de texto
print('Día', fecha[:2])

# Imprimir el mes extrayendo los caracteres en la posición 3 y 4 de la cadena de texto
print('Mes', fecha[3:5])

# Imprimir el año extrayendo los caracteres desde la posición 6 hasta el final de la cadena de texto
print('Año', fecha[6:])
