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


#---16

# Creamos una tupla con los valores dados
tupla = (15, 8, 12, 20)

# Comprobamos si el primer valor es menor que el último
if tupla[0] < tupla[-1]:
    print("orden ascendente")  # Si el primer valor es menor, mostramos "orden ascendente"
else:
    print("orden descendente")  # Si no, mostramos "orden descendente"""

#---17






