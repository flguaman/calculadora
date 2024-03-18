# Definición de funciones para realizar operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:  # Verifica si el divisor no es cero para evitar una división por cero
        return a / b
    else:
        return "Error: División por cero"

# Muestra las opciones disponibles al usuario
print("Selecciona la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa tu opción (1/2/3/4): ")

# Solicita al usuario que ingrese los dos números para realizar la operación
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realiza la operación seleccionada según la opción ingresada por el usuario y muestra el resultado
if opcion == '1':
    print("Resultado:", suma(num1, num2))
elif opcion == '2':
    print("Resultado:", resta(num1, num2))
elif opcion == '3':
    print("Resultado:", multiplicacion(num1, num2))
elif opcion == '4':
    print("Resultado:", division(num1, num2))
else:
    print("Opción no válida")  # Muestra un mensaje de error si la opción ingresada no es válida
