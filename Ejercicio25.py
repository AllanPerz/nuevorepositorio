import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que crea un diccionario vacío y lo va llenando con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) Cada vez que se añada un nuevo dato debe 
#imprimirse el contenido del diccionario.
info_persona = {} # Diccionario para almacenar información de la persona
continuar_ingreso = True # Bandera para controlar el ciclo de ingreso de datos
while continuar_ingreso:
    dato = input('¿Qué dato quieres introducir? ') # Solicita al usuario el tipo de dato a ingresar
    valor_dato = input(dato + ': ') # Solicita al usuario el valor del dato a ingresar
    info_persona[dato] = valor_dato # Agrega el dato al diccionario
    print(info_persona) # Imprime el contenido del diccionario
    # Pregunta al usuario si desea continuar añadiendo información
    continuar_ingreso = input('¿Quieres añadir más información (Si/No)? ') == "Si"
