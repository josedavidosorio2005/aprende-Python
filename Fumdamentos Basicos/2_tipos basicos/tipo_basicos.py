#numeros decimales 
edad = 25
temperatura = -5
catidad_de_estudiantes = 30

print(type(temperatura,))

#flotantes numero decimales 
altura = 1.75
peso = 68.5
temperatura = 36.6

print(type(altura))

# texo o cadenas (strings)

nombre = "Juan"

apellido = 'Pérez'
direccion ="calle principal #123"
mensaje = """este mesaje 
ocupa 
tres lineas """
print(type(nombre))

# booleanos (bool)

es_estudiante = True
tiene_mascota = False

print(type(es_estudiante))

#convertir entre difernetes  tipos 
edad_texto = "25"
edad_num = int(edad_texto)

precio =99.99
precio_entero = int(precio)

numero = 42 
numero_texto = str(numero )

print(type(edad_num))

print(type(precio_entero))

print(type(numero_texto))


# Programa de registro de estudiante
nombre = "ana"
edad = 20
altura =1.65
es_activo = True

print("Información del Estudiante:")
print(f"Nombre: {nombre} ({type(nombre)})")

print(f"Edad: {edad} ({type(edad)})")

print(f"Altura: {altura} ({type(altura)})")

print(f"Es activo: {es_activo} ({type(es_activo)})")

#caracteristicas especiles 
varible = None
print(type(varible))

num = 24 
texto = "hola"

print(isinstance(num, int))

print(isinstance(texto, str))

print(isinstance(num, (float)))


# Crear un programa que maneje diferentes tipos de datos

nombre = input("pon tu nombre ")
edad = int(input("pon tu edad "))
altura = float(input("pon tu altura  en metros "))
tine_mascota = input("tines mascota ? (si/no) ").lower() == "si"

# Mostramos un resumen
print("\nResumen de datos:")
print(f"Nombre: {nombre} ({type(nombre)})")

print(f"Edad: {edad} ({type(edad)})")

print(f"Altura: {altura} ({type(altura)})")

print(f"Tine mascota: {tine_mascota} ({type(tine_mascota)})")

