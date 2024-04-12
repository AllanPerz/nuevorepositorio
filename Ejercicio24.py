import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que guarda un diccionario con diferentes divisas y sus símbolos
diccionario_monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

#Se solicita al usuario que ingrese una divisa para buscar su símbolo
divisa_usuario = input("Introduce una divisa: ")

#Se busca el símbolo de la divisa en el diccionario y se muestra al usuario.
#Si la divisa no existe, se muestra un mensaje de aviso.
print(diccionario_monedas.get(divisa_usuario.title(), "La divisa no está en el diccionario."))
