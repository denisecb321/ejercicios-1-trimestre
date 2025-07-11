
edad=30
if edad >=18:
    print(f"es un adulto porque tiene {edad}")

#------------ejercicios con condicionales y operaciones matematicas--------------

#-verifica si un numero es positivo, negativo o cero.

num1=float(input("ingrese un numero: "))

if num1 > 0:
    print(f"es positivo porque es {num1}")
elif num1 <0:
    print(f"es negativo porque es {num1}")
else:
    print(f"es cero porque es {num1}")

# ejercicio2

num2=float(input("ingrese un numero:"))
num3=float(input("ingrese otro numero:"))

if num2 > num3:
    print(f"el {num2} es mayor que el {num3}")
elif num3 > num2:
    print(f"el {num3} es mayor que el {num2}")


#--ejercicio3

num1=int(input("ingrese un numero:"))
 
if num1 % 2==0:
    print(f"el numero {num1} es par")
else:
    print(f"el numero {num1} es impar")

#--ejercicio4

num2=float(input("ingrese un numero:"))

if 10 <= num2 <=20:
    print(f"el numero {num2} esta entre 10 y 20.")
else:
    print(f"el numero {num2} no esta entre 10 y 20.")


#--ejercicio5

num3=int(input("ingrese un numero:"))
num4=int(input("ingrese otro numero:"))
num5=int(input("ingrese otro numero:"))

if num3 > num4 and num3 > num5:
    print(f"el numero {num3} es mayor que {num4} y {num5} .")

elif num4 > num3 and num4 > num5:
    print(f"el numero {num4} es mayor que {num3} y {num5} .")

elif num5 > num3 and num5 > num4:
    print(f"el numero {num5} es mayor que {num3} y {num4} .")

#---ejercicio6

precio=float(input("ingrese un precio:"))
descuento= precio*0.10
total=precio-descuento
if total >=100:
    print(f"{total} es mayor o igual a $100.")
elif total < 100:
    print(f"{total} no es igual o mayor a $100.")

#---ejercicio7

edad=int(input("ingrese su edad:"))

if edad >= 18:
    print(f"usted tiene {edad} años, es mayor de edad por lo tanto usted puede votar.")
elif edad < 18:
    print(f"usted tiene {edad} años, es menor de edad por lo tanto usted no puede votar")


#--ejercicio8

precio=float(input("ingrese un precio:"))
tipo_cliente=input("que tipo de cliente es usted?(VIP/normal):")
descuento=precio*0.20
total=precio-descuento
if tipo_cliente == "VIP":
    print("si usted es un cliente VIP se le aplicara un 20% de descuento.")
elif tipo_cliente == "normal":
    print("usted es un cliente noraml por lo tanto no se le dara descuento.")



#---desafios logicos en python---

#---ejercicio1---

edad=int(input("ingrese su edad:"))

if edad < 18:
    print("usted es menor de edad")
elif edad >= 18 and edad <= 65:
    print("usted es mayor de edad")
elif edad > 65:
    print("usted es un adulto mayor")

#---ejercicio2---

estatura=float(input("ingrese su estatura en metros :"))

if estatura < 1.5:
    print("usted es considerado de estatura baja")
elif estatura >= 1.5 and estatura <= 1.8:
    print("usted es considerado de estatura media")
elif estatura > 1.8:
    print("usted es considerado de estatura alta")

#---ejercicio3---

num=int(input("ingrese un numero: "))

if num % 2 == 0:
    print("el numero es multiplo de 2")
elif num % 3 == 0:
    print("el numero es multiplo de 3")
else:
    print("el numero no es multiplo de ninguno")


#---ejercicio4---

num1 = input("Ingrese un número decimal: ")

if "." in num1:
    parte_decimal = num1.split(".")[1]
    cantidad_decimales = len(parte_decimal)

    if cantidad_decimales == 1:
        print("El número tiene 1 decimal.")
    elif cantidad_decimales == 2:
        print("El número tiene 2 decimales.")
    else:
        print("El número tiene más de 2 decimales.")
else:
    print("El número no tiene parte decimal.")

#---ejercio5---

paises=("Colombia", "Peru", "Argentina", "Mexico")
pais=input("ingrese el nombre de un pais:")

if pais in paises:
    print("el pais esta en la tupla")
else:
    print("el pais no esta en la tupla")

#---ejercicio6---

compatibilidad={
    "O":["O"],
    "A":["O","A"],
    "B":["O","B"],
    "AB":["O","A","B","AB"]
}
tipo_de_sangre=input("ingrese su tipo de sangre (A/B/AB/O): ").upper()

if tipo_de_sangre in compatibilidad:
    compatibles=compatibilidad[tipo_de_sangre]
    print(f"puedes recibir sangre de :{", ".join(compatibles)}")
else:
    print("tipo de dato no valido")


#---ejercicio7---

temperatura=int(input("ingrese la temperatura en °C: "))

if temperatura < 10:
    print("el clima esta frio")
elif temperatura >= 10 and temperatura <= 25:
    print("el clima esta templado")
else:
    print("el clima esta caliente")


#---ejercicio8---

print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1-4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    resultado = num1 + num2
    print("Resultado: ", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("Resultado: ", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("Resultado: ", resultado)
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado: ", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida.")

#---ejercicio9---

meses={
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

num2=int(input("ingrese un numero entre el 1 y el 12: "))

if 1 <= num2 <= 12:
    print("el mes correspondiente es: ",meses[num2])
else:
    print("numero no valido")

#---ejercicio10---

num3=(input("ingrese un numero de 4 digitos: "))

if num3[0]== "1":
    print("el numero comienza con 1")
elif num3[0]== "2":
    print("el numero comienza con 2")
elif num3[0]== "3":
    print("el numero comienza con 3")
else:
    print("el numero no comienca con 1, 2 o 3")


#---ejercicio11---

palabra=input("ingresa una palabra: ")

if palabra[0] in "aeiou":
   print("la palabra empieza con una letra vocal")
else:
  print("la palabra comienza con una letra consonante")

#---ejercicio12---

frutas={
    "manzana": 100,
    "pera": 200,
    "piña": 120
}

fruta = input("Ingresa una fruta: ").lower()

if fruta in frutas:
    print(f"El precio de la {fruta} es: {frutas[fruta]} pesos.")
else:
    print("La fruta no está disponible.")

#---ejercicio13---

calificacion=int(input("ingrese su calificacion (0 a 5): "))

if calificacion < 3:
    print("reprobado")
elif calificacion >=3 and calificacion <=4:
    print("aprobado")
else:
    print("excelente")

#---ejercicio14---

num4=int(input("ingrese un numero:"))
if num4 % 4 == 0:
    print("el numero es divisible entre 4")
elif num4 % 6 == 0:
    print("el numero es divisible entre 6")
else:
    print("el numero no es divisible entre 4 o 6")

#---ejercicio15---

usuarios={
    "nicolk": 16,
    "sofia": 29,
    "annjely": 1
}

usuario=input("ingrese su usuario: ")
clave=int(input("ingrese su clave:"))

if usuario in usuarios and usuarios[usuario]== clave:
    print("acceso permitido")
else:
    print("acceso denegado")

#---ejercicio16---

edad=int(input("ingrese su edad: "))

if edad >= 0 and edad <= 12:
    print("usted es un/a niño/a")
elif edad >=13 and edad <= 17:
    print ("usted es un/a adolecente")
elif edad >= 18 and edad <= 64:
    print("usted es un/a adulto/a")
else:
    print("usted es un/a adulto/a mayor")

#---ejercicio17---

capitales = ("Madrid", "Buenos Aires", "Lima")

ciudad = input("Ingresa el nombre de una ciudad: ")

if ciudad in capitales:
    print(f"{ciudad} es una capital.")
else:
    print(f"{ciudad} es una ciudad secundaria.")

#---ejercicio18---

valor = float(input("Ingresa el valor de la compra: "))

if valor > 200000:
    descuento = valor * 0.15
elif 100000 <= valor <= 200000:
    descuento = valor * 0.10
else:
    descuento = 0

total = valor - descuento
print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {total}")


#---ejercicio19---

nombre = input("Ingresa tu nombre: ")
horas = float(input("Número de horas trabajadas: "))
tarifa = 10999
salario_base = horas * tarifa
if horas > 40:
    bono = salario_base * 0.20
else:
    bono = 0

salario_total = salario_base + bono
print(f"{nombre}, tu salario total es: {salario_total}")

#---ejercicio20---

puntaje = int(input("Ingresa un puntaje (0-100): "))

if puntaje < 0 or puntaje > 100:
    print("Puntaje inválido.")
elif puntaje < 50:
    print("Insuficiente")
elif puntaje <= 79:
    print("Aceptable")
else:
    print("Sobresaliente")












