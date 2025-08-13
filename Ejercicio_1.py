"""
Sistema de calculadora

Este programa permite:
1. SUMAR.
2. RESTAR.
3. DIVIDIR.
6. MULTIPLICAR.
5. Salir del sistema.

Autor: Eduardo Baños
Fecha: 13/08/2025
"""
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "5":
            print("Adiós!")
            break
        elif opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Ingrese números válidos.")
            continue

        if opcion == "1":
            print(f"{num1} + {num2} = {suma(num1, num2)}")
        elif opcion == "2":
            print(f"{num1} - {num2} = {resta(num1, num2)}")
        elif opcion == "3":
            print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"{num1} / {num2} = {division(num1, num2)}")

if __name__ == "__main__":
    calculadora()
