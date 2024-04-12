import os
# Limpiar la pantalla de la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Diccionario con los nombres de los meses
nombres_meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

# Solicitar al usuario que ingrese una fecha en formato dd/mm/aaaa
fecha_ingresada = input('Introduce una fecha en formato dd/mm/aaaa: ')

# Dividir la fecha ingresada en día, mes y año
fecha_dividida = fecha_ingresada.split('/')

# Imprimir la fecha en el formato deseado
print(fecha_dividida[0], 'de', nombres_meses[int(fecha_dividida[1])], 'de', fecha_dividida[2])
