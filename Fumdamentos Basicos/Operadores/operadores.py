#operadores aridmeticos 

#suma (+)
suma = 5 + 3 #resultado 8

#resta (-)
resta = 10-4 #resultado 6

 #multiplicación (*)
multiplicacion = 5 * 2 #resultado 10

#división (/)
division = 10 / 2 #resultado 5
 
 #divicion entera (//)
division_entera = 17 // 3 #resultado 5

#residuo (%)
residuo = 10 % 3 # resultado 1

#potencia (**)
potencia = 2 ** 3 # resultado 


#operadores de cmparacion 
#igual que (==)
5 == 5 #resultado True
5 == 3 #resultado False

#distinto que (!=)
5 != 3 # resultado True
5 != 5 # resultado False

#mayor que (>)
5 > 3 # resultado True
5 > 8 # resultado False

#menor que (<)
5 < 8 # resultado True
5 < 6 # resultado False

#mayor o igual que (>=)

5 >= 5 # resultado True
5 >= 3 # resultado True
5 >= 8 # resultado False

#menor o igual que (<=)
5 <= 5 # resultado True
5 <= 3 # resultado False
5 <= 6 # resultado True

#operadores logicos
#and - ambas direcicnes 
edad = 18
tiene_licencia = True
puede_conducior = edad >= 18 and tiene_licencia # resultado True

#or - cualquiera de las direcciones
edad = 18
tiene_licencia = False

puede_conducir = edad >= 18 or tiene_licencia # resultado True

#not - negacion

tiene_licencia = True
tiene_licencia_negada = not tiene_licencia # resultado False

#operadores de atribucion
#asignacion (=)
x = 5

#suma y asignacion (+=)
x += 3 # resultado 8

#resta y asignacion (-=)
x -= 2 # resultado 6

#multiplicacion y asignacion (*=)

x *= 2 # resultado 12

#division y asignacion (/=) 

x /= 2 # resultado 6

#ejemplo paractiico 
"calculadora simple "
n1 = 10 
n2 = 3

#operacion basicas 
suma = n1 + n2

resta = n1 - n2

multiplicacion = n1 * n2

division = n1 / n2

print(f"suma: {suma}")

print(f"resta: {resta}")

print(f"multiplicacion: {multiplicacion}")

print(f"division: {division}")

# comparacion  
es_mayor = n1 > n2

es_menor = n1 < n2

es_igual = n1 == n2

print(f"es mayor: {es_mayor}")  

print(f"es menor: {es_menor}")

print(f"es igual: {es_igual}")

# Programa para calcular el descuento de una compra
precio = 100
tiene_cupon = True
es_cliente_vip = True

if tiene_cupon and es_cliente_vip:
    descuento = 0.30 * precio
elif tiene_cupon or es_cliente_vip:
    descuento = 0.15 * precio
else:
    descuento = 0

precio_final = precio - descuento

print(f"El precio final es: {precio_final}")