#Conversor de temperatura
# Crear un programa que:
# - Convierta entre Celsius y Fahrenheit
# - Permita elegir la dirección de la conversión
# - Valide la entrada
def limpiar_consola():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def conversor_temperatura():
    while True:
        limpiar_consola()
        print("\n=== CONVERSOR DE TEMPERATURA ===")
        print("\n1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Salir")
        
        try:
            opcion = input("\nSeleccione una opción (1-3): ")
            
            if opcion == "3":
                print("\n¡Gracias por usar el conversor!")
                break
                
            if opcion not in ["1", "2"]:
                print("\nOpción no válida. Por favor, seleccione 1, 2 o 3.")
                input("\nPresione Enter para continuar...")
                continue
                
            temp = float(input("\nIngrese la temperatura: "))
            
            if opcion == "1":
                resultado = (temp * 9/5) + 32
                print(f"\n{temp}°C = {resultado:.2f}°F")
            else:
                resultado = (temp - 32) * 5/9
                print(f"\n{temp}°F = {resultado:.2f}°C")
                
            input("\nPresione Enter para continuar...")
            
        except ValueError:
            print("\nError: Por favor, ingrese un número válido")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    conversor_temperatura()