"""letra=input("ingrese una letra:")

if letra ==("a"):
    print("la a en mayuscula es A")
elif letra ==("e"):
    print("la e en mayuscula es E")
elif letra ==("i"):
    print("la i en mayuscula es I")
elif letra ==("o"):
    print("la o en mayuscula es O")
elif letra ==("u"):
    print("la u en mayuscula es U")
else:
    print("la letra no es valida")

#ejemplo2---

comando="SALIR"
if comando=="ENTRAR":
    print("bienvenido al sistema")
elif comando=="SALUDO":
    print("hola, como estas?")
elif comando=="SALIR":
    print("saliendo del sistema")
else:
    print("no se reconoce el comando")


#--------------------EJERCICIOS-CONDICIONALES-OPERACIONES-MATEMATICAS------------

#---1

# Solicita al usuario que ingrese un número
num=int(input("ingresa un numero: "))

# Verifica si el número es mayor que 0
if num > 0:
    print(f"el numero {num} es positivo")
# Si no es mayor que 0, verifica si es menor que 0  
elif num < 0:
    print(f"el numero {num} es negativo")
# Si no es mayor ni menor que 0, entonces debe ser igual a 0    
elif num == 0:
    print("el numero es igual a 0")
else:
    print("error")

#---2

# Pide al usuario que ingrese el primer número
num1=int(input("ingrese un primer numero: "))
# Pide al usuario que ingrese el segundo número
num2=int(input("ingrese un segundo numero: "))

# Compara si el primer número es mayor que el segundo
if num1 > num2:
    print(f"el numero {num1} es mayor que el numero {num2}")
# Si no, verifica si el primer número es menor que el segundo   
elif num1 < num2:
    print(f"el numero {num1} es menor que el numero {num2}")
# Si no es mayor ni menor, entonces son iguales
else:
    print("los numeros son iguales")

#---3

# Pide al usuario que ingrese un número
num3=int(input("ingrese un numero: "))

# Verifica si el número es divisible por 2 (es par)
if num3 % 2 == 0:
    print(f"el numero {num3} es par")
# Si no es divisible por 2, entonces es impar   
elif num3 % 2 !=0:
    print(f"el numero ingresado es impar")
else:
    print("fin")

#---4

# Pide al usuario que ingrese un número
num4=int(input("ingrese un numero: "))

# Verifica si el número está en el rango de 10 a 20, incluyendo ambos extremos
if num4 >= 10 and num4 <=20:
    print(f"el numero {num4} esta entre 10 y 20")
# Se ejecuta si el número está fuera del rango
else:
    print("fin")

#---5

# Se ingresan tres números
num5=int(input("ingrese un numero: "))
num6=int(input("ingrese un numero: "))
num7=int(input("ingrese un numero: "))

# Verifica si num5 es mayor que los otros dos
if num5 > num6 and num5 > num7:
    print(f"el {num5} es mayor que {num6} y {num7}")
# Verifica si num6 es el mayor
elif num6 > num5 and num6 > num7:
    print(f"el {num6} es mayor que {num5} y {num7}")
# Verifica si num7 es el mayor
elif num7 > num5 and num7 > num6:
    print(f"el {num7} es mayor que {num5} y {num6}")
else:
    print("fin")

#---6

# Solicita al usuario que ingrese el total de la compra
total = float(input("Ingresa el total de la compra: "))

# Verifica si el total es mayor a 100 para aplicar un descuento
if total > 100:
    # Calcula el 10% de descuento
    descuento = total * 0.10
    #  Resta el descuento al total original
    precio_final = total - descuento
    # Muestra el total a pagar con descuento
    print(f"Se aplicó un 10% de descuento. Total a pagar: ${precio_final:.2f}")
else:
    # Si el total no supera 100, no hay descuento
    print(f"No hay descuento. Total a pagar: ${total:.2f}")

#---7

# Solicita al usuario que ingrese su edad
edad=int(input("ingrese su edad: "))

# Verifica si la edad es menor a 18
if edad < 18:
    print("usted es menor de edad, NO puede votar")
# Si no es menor, verifica si es mayor o igual a 18
elif edad >= 18:
    print("usted es mayor de edad, Si puede votar")
else:
    print("fin")

#---8

# Solicita el precio del producto
precio = float(input("Ingresa el precio del producto: "))
# Solicita el tipo de cliente y convierte la entrada a minúsculas para facilitar la comparación
tipo_cliente = input("Ingresa el tipo de cliente (vip o normal): ").lower()

# Verifica si el cliente es VIP para aplicar el descuento
if tipo_cliente == "vip":
    # Calcula el 20% de descuento
    descuento = precio * 0.20
    # Aplica el descuento al precio
    precio_final = precio - descuento
    print(f"Cliente VIP: se aplicó un 20% de descuento. Total a pagar: ${precio_final:.2f}")
# Si el cliente es normal, no hay descuento
elif tipo_cliente == "normal":
    print(f"su total a pagar es de {precio}")
else:
    print("fin")

#---9

# Pide al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verifica si el número es divisible por 3 y por 5 al mismo tiempo
if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} es múltiplo de 3 y de 5 al mismo tiempo.")
else:
    print(f"{numero} NO es múltiplo de 3 y de 5 al mismo tiempo.")

#---10

# Pide al usuario que ingrese un número y dos divisores
numero = int(input("Ingresa un número: "))
divisor1 = int(input("Ingresa el primer divisor: "))
divisor2 = int(input("Ingresa el segundo divisor: "))

# Verifica si el número es divisible por ambos divisores usando el operador módulo
if numero % divisor1 == 0 and numero % divisor2 == 0:
    print(f"{numero} es divisible entre {divisor1} y {divisor2}.")
else: print(f"{numero} NO es divisible entre {divisor1} y {divisor2}.")

#--------------------EJERCICIOS-CON-LISTAS--------------------------------------

#---11

# Creamos una lista con 5 números
numeros = [4, 7, 12, 9, 3]

# Verificamos si el tercer número (posición 2) es mayor que 10
if numeros[2] > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")

#---12

# Creamos una lista con los números 3, 5, 7 y 9
lista = [3, 5, 7, 9]

# Verificamos si el número 7 está dentro de la lista usando 'in'
if 7 in lista:
    # Si 7 está en la lista, mostramos este mensaje
    print("Está en la lista")
else:
    # Si 7 no está en la lista, mostramos este otro mensaje
    print("No está en la lista")

#---13

# Definimos la lista con los números dados
lista = [4, 6, 2, 8]
# Sumamos los dos primeros elementos (índices 0 y 1)
suma = lista[0] + lista[1]

# Verificamos si la suma es mayor a 10
if suma > 10:
    print("Suma alta")
else:
    print("Suma baja")

#---14

# Se crea una lista con cuatro nombres
nombres = ["ana", "luis", "pedro", "marta"]
# Se obtiene el último elemento de la lista usando índice negativo (-1)
ultimo_nombre = nombres[-1]
# Se verifica si el último nombre es igual a "marta"
if ultimo_nombre == "marta":
    # Si la condición es verdadera, se muestra este mensaje
    print("nombre correcto")
else:
    # Si la condición es falsa, se muestra este mensaje
    print("nombre diferente")

#---15

# Se crea una lista con tres colores
colores = ["rojo", "azul", "verde"]
# Se verifica si el segundo color (índice 1) es igual a "azul"
if colores[1] == "azul":
    # Si la condición es verdadera, se cambia el segundo color por "amarillo"
    colores[1] = "amarillo"
# Se muestra la lista actualizada
print(colores)

#---16

# Creamos una tupla con los valores dados
tupla = (15, 8, 12, 20)

# Comprobamos si el primer valor es menor que el último
if tupla[0] < tupla[-1]:
    print("orden ascendente")  # Si el primer valor es menor, mostramos "orden ascendente"
else:
    print("orden descendente")  # Si no, mostramos "orden descendente

#---17

# Se define una tupla llamada 'edades' que contiene tres valores enteros
# Cada posición representa una edad distinta
edades = (25, 32, 28)

# Se evalúa si el segundo valor de la tupla (índice 1) es mayor que 30
if edades[1] > 30:
    # Si la condición es verdadera, se muestra este mensaje en pantalla
    print("edad mayor a 30")
else:
    # Si la condición es falsa, se muestra este mensaje
    print("edad menor o igual a 30")

#---18

# Se define una tupla con los valores 1, 2 y 3
numeros = (1, 2, 3)
# Se convierte la tupla en una lista para poder modificar sus elementos
lista_numeros = list(numeros)
# Se verifica si el segundo valor (índice 1) es igual a 2
if lista_numeros[1] == 2:
    # Si la condición es verdadera, se cambia el segundo valor a 10
    lista_numeros[1] = 10
# Se convierte nuevamente la lista en una tupla
numeros_actualizados = tuple(lista_numeros)

# Se muestra la tupla resultante
print(numeros_actualizados)

#---19

# Se define una tupla con dos valores
coordenadas = (4, 9)
# Se accede al segundo valor de la tupla (índice 1)
segundo_valor = coordenadas[1]
# Se verifica si el segundo valor es mayor que 5
if segundo_valor > 5:
    # Si es mayor que 5, se muestra el mensaje correspondiente
    print("coordenada alta")
else:
    # Si no es mayor que 5, se muestra el mensaje correspondiente
    print("coordenada baja")

#---20

# Se define la primera tupla con los valores 3 y 4
tupla1 = (3, 4)
# Se define la segunda tupla con los valores 3 y 5
tupla2 = (3, 5)
# Se compara si las dos tuplas son exactamente iguales
if tupla1 == tupla2:
    # Si son iguales, se muestra este mensaje
    print("tuplas iguales")
else:
    # Si son diferentes, se muestra este mensaje
    print("tuplas diferentes")

#---21

# Se crea un diccionario con dos claves: 'nombre' y 'edad'
persona = {
    "nombre": "juan",
    "edad": 17
}
# Se accede al valor asociado a la clave 'edad' y se verifica si es mayor o igual a 18
if persona["edad"] >= 18:
    # Si la edad es mayor o igual a 18, se muestra este mensaje
    print("adulto")
else:
    # Si la edad es menor a 18, se muestra este mensaje
    print("menor de edad")

#---22

# Crear un diccionario con las claves 'nombre' y 'edad'
persona = {
    "nombre": "lucia",
    "edad": 20
}
# Verificar si la edad es mayor a 18
if persona["edad"] > 18:
    # Si es mayor a 18, cambiar el valor de 'edad' a 21
    persona["edad"] = 21
# Mostrar el diccionario actualizado
print(persona)

#---23

# Crear un diccionario con la clave 'nombre'
persona = {
    "nombre": "carlos"
}
# Verificar si la clave 'ciudad' no existe en el diccionario
if "ciudad" not in persona:
    # Si no existe, agregar la clave 'ciudad' con el valor 'bogota'
    persona["ciudad"] = "bogota"
# Mostrar el diccionario actualizado
print(persona)

#---24

# Crear un diccionario con las claves 'producto' y 'precio'
producto = {
    "producto": "pan",
    "precio": 1200
}
# Verificar si la clave 'precio' existe en el diccionario
if "precio" in producto:
    # Si existe, mostrar su valor
    print(f"El precio es: {producto['precio']}")
else:
    # Si no existe, mostrar un mensaje indicando que no hay precio
    print("No hay precio")

#---25

# Crear un diccionario con productos y sus precios
productos = {
    "pan": 1200,
    "leche": 2000
}
# Verificar si el producto 'pan' está en el diccionario
if "pan" in productos:
    # Si está, mostrar su precio
    print(f"El precio del pan es: {productos['pan']}")
else:
    # Si no está, mostrar un mensaje indicando que el producto no está disponible
    print("Producto no disponible")"""






