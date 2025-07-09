
edad=30
if edad >=18:
    print(f"es un adulto porque tiene {edad}")

#------------ejercicios con condicionales y operaciones matematicas--------------

#-verifica si un numero es positivo, negativo o cero.

"""num1=float(input("ingrese un numero: "))

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
    print(f"usted tiene {edad} años, es menor de edad por lo tanto usted no puede votar")"""


#--ejercicio8

precio=float(input("ingrese un precio:"))
tipo_cliente=input("que tipo de cliente es usted?(VIP/normal):")
descuento=precio*0.20
total=precio-descuento
if tipo_cliente == "VIP":
    print("si usted es un cliente VIP se le aplicara un 20% de descuento.")
elif tipo_cliente == "normal":
    print("usted es un cliente noraml por lo tanto no se le dara descuento.")

