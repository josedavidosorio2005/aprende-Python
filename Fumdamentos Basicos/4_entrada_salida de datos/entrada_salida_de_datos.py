#La función principal para obtener entrada del usuario es input(). Siempre devuelve una cuerda.
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")

#converciones de tipos 
edad = int(input("¿Cuál es tu edad? "))

#converciona float 
altura = float(input("¿Cuál es tu altura? "))
#convertir a vuleanos 
respuestas = bool(input("¿Te gusta la pizza?(True/False) "))


#Salida de DatosFunción print()
#La función print()es la forma más básica de mostrar información:
print("Hola Mundo")

#multiples argumentos 

nombre = "juan "
edad = 50
print("nombre", nombre, "tienes", edad, "años")

#uso  de end para cambiar el final 
print("Hola", end=" ")
print("Mundo")

#uso de sep para cambiar el separador
print("Python", "es", "genial", sep="_")

#formatos de cadena 
nombre = "Juan"
edad = 30

print(f"me llamo {nombre} y tengo {edad} años")

# Con formateo de números
precio = 19.99
print(f"el precio es de{precio:.2f} ")

#metodo .format()
nombre = "María"
edad = 25
print("me llamo {} y tengo {} años".format(nombre, edad))

# Con posiciones específicas
print("{1} tiene {0} años".format(edad, nombre))

# Con nombres
print("{n} tiene {e} años".format(n=nombre, e=edad))

# operador %
nombre = "luna "
edad = 102
print("me llamo %s y tengo %d años"%(nombre,edad))


#manejo de archivos 
# Método 1: with (recomendado)
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()  # Lee todo el archivo

with open('archivo.txt', 'r') as archivo:
    lineas = archivo.readlines() # Lee todas las líneas

# Método 2: lectura línea por línea
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina espacios y saltos de línea

        
# Escribir en un archivo (sobrescribe)
with open('nuevo.txt', 'w') as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Segunda línea")

# Añadir a un archivo (append)
with open('lunapendeja.txt', 'a') as archivo:
    archivo.write("\nTercera línea")


# Manejo básico de errores
try:
    edad = int(input("cuantos años tienes? "))
except ValueError:
    print("Eso no es un número válido")

    

try:
    with open('nuevo.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos para abrir el archivo")

    

def registrar_usuario():
    nombre = input("nombre")
    try:
       edad=int(input("cuantos años tienes? "))
       with open('usuarios.txt', 'a') as archivo:
           archivo.write(f"{nombre} tiene {edad} años\n")
           print("Usuario registrado exitosamente")
    except ValueError:
        print("Eso no es un número válido")


def mostrar_usuarios():
    try:
        with open('usuario.txt', 'r') as archivo:
            for linea in archivo:
                nombre, edad = linea.strip().split(',')
                print(f"Usuario: {nombre}, Edad: {edad}")
    except FileNotFoundError:
        print("El archivo de usuarios no existe")