import os
os.system('cls' if os.name == 'nt' else 'clear') 
# Ejercicio2.py 
# Es un programa que almacena una contraseña y le pide al usuario ingresar otra

# Se define la contraseña correcta y se almacena en la variable 'key'
key = "holacompañeros"

# Se solicita al usuario que ingrese una contraseña y se almacena en la variable 'password'
password = input("Introduce la contraseña: ")

# Se compara la contraseña ingresada por el usuario con la contraseña correcta
# Se utiliza el método .lower() para convertir la contraseña ingresada a minúsculas
# y así evitar problemas de mayúsculas y minúsculas al momento de comparar
if key == password.lower():
    # Si las contraseñas coinciden, se imprime un mensaje de éxito
    print("La contraseña coincide")
else:
    # Si las contraseñas no coinciden, se imprime un mensaje de error
    print("La contraseña no coincide")
