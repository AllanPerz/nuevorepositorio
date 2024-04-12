# Limpiamos la pantalla de la terminal antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitamos al usuario que introduzca el nombre del producto
producto = input('Introduce el nombre del producto: ')
# Solicitamos al usuario que introduzca el precio unitario del producto y lo convertimos a float
precio = float(input('Introduce el precio unitario: '))
# Solicitamos al usuario que introduzca el número de unidades del producto y lo convertimos a int
unidades = int(input('Introduce el número de unidades: '))

# Imprimimos en pantalla la información del producto en un formato específico
# Utilizamos el método format para insertar las variables en la cadena de texto
# Se especifica el formato de los números con :3d para unidades (3 dígitos enteros)
# y :9.2f para precio y total (números flotantes con 2 decimales)
print('{producto}: {unidades:3d} unidades x {precio:9.2f}Lps = {total:11.2f}Lps'.format(
    producto = producto,
    unidades = unidades,
    precio = precio,
    total = unidades * precio
))
