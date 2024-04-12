# Limpiamos la consola antes de ejecutar el programa
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programa que pide al usuario su correo electrónico
# y muestra en pantalla otro correo con el mismo nombre de usuario pero con dominio de gmail
email = input("Introduce tu correo electrónico: ")
# Usamos el método find() para localizar la posición de la arroba (@) y extraemos la parte delantera
# Luego concatenamos '@gmail.com' para formar el nuevo correo
print(email[:email.find('@')] + '@gmail.com')