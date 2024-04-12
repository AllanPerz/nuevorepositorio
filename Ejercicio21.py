import os
os.system('cls' if os.name == 'nt' else 'clear') # Limpia la pantalla de la consola
# Programa que pregunta al usuario su nombre, edad, dirección y teléfono y lo guarda en un diccionario.
# Después debe mostrar por pantalla el mensaje
# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# Solicitamos al usuario que ingrese su nombre
nombre = input('¿Cómo te llamas? ')
# Solicitamos al usuario que ingrese su edad
edad = input('¿Cuántos años tienes? ')
# Solicitamos al usuario que ingrese su dirección
direccion = input ('¿Cuál es tu direccion? ')
# Solicitamos al usuario que ingrese su número de teléfono
telefono = input('¿Cuál es tu numero de telefono? ')

# Creamos un diccionario con la información proporcionada por el usuario
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

# Imprimimos el mensaje con los datos del usuario
print (persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])