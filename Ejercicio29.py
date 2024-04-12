import os
# Limpiar la pantalla antes de iniciar el programa
os.system('cls' if os.name == 'nt' else 'clear')
# Programa que almacena la cadena de caracteres de la contraseña en una variable
# y pregunta al usuario por la contraseña hasta que introduzca la contraseña correcta.
contrasena_correcta = "UthCampusSB" # Variable que almacena la contraseña correcta
contrasena_usuario = "" # Variable que almacena la contraseña introducida por el usuario

# Bucle que se repite hasta que el usuario introduzca la contraseña correcta
while contrasena_usuario != contrasena_correcta:
    contrasena_usuario = input("Introduce la contraseña: ") # Pide al usuario que introduzca la contraseña

# Si la contraseña es correcta, se imprime un mensaje de confirmación
print("Contraseña correcta")