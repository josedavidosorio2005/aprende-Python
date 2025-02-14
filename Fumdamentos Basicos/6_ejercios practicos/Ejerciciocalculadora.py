#Calculadora simple
# Crear una calculadora que:
# - Pida dos números al usuario
# - Permita elegir entre suma, resta, multiplicación y división
# - Muestre el resultado
# - Maneje errores (división por cero)
def calculadora():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        print("\n1. Suma\n2. Resta\n3. Multiplicación\n4. División")
        opcion = int(input("Seleccione una opción (1-4): "))
        
        if opcion == 1:
            print(f"Resultado: {num1 + num2}")
        elif opcion == 2:
            print(f"Resultado: {num1 - num2}")
        elif opcion == 3:
            print(f"Resultado: {num1 * num2}")
        elif opcion == 4:
            if num2 == 0:
                print("No se puede dividir por cero")
            else:
                print(f"Resultado: {num1 / num2}")
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: Ingrese números válidos")

if __name__ == "__main__":
    calculadora()