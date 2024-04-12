
# Programa que pide la edad del usuario y determina si es mayor o menor de edad

# Solicita la edad al usuario y la convierte a un número entero
edad = int(input("¿Cual es tu edad?"))

# Compara la edad ingresada con el límite de 18 años
if edad < 18:
    # Si la edad es menor a 18, imprime que es menor de edad
    print ("Eres menor de edad.")
else:
    # Si la edad es mayor o igual a 18, imprime que es mayor de edad
    print ("Eres mayor de edad.")   