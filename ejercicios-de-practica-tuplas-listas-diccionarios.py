#----EJERCICIOS-DE-PRACTICA------------------------------------

#---calculadora-de-promedio-------------------

"""calificacion1=int(input("ingrese su primera calificacion: "))
calificacion2=int(input("ingrese su segunda calificacion: "))
calificacion3=int(input("ingrese su tercera calificacion: "))
lista=[calificacion1,calificacion2,calificacion3]
print(lista)
promedio=calificacion1+calificacion2+calificacion3//3
print(f"el promedio del estudiante es:{promedio}")

#---actualiza-precios------------------------

productos={
    "banano": "4000",
    "huevo": "500",
    "leche": "6000",
}
print(productos)
porcentaje=float(input("ingrese el porcentaje de aumento(%): "))
productos["banano"]+=productos["banano"]*(porcentaje/100)
productos["huevo"]+=productos["huevo"]*(porcentaje/100)
productos["leche"]+=productos["leche"]*(porcentaje/100)
print(productos)

#---conversor-de-temperaturas----------------

temp1 = float(input("Ingrese la temperatura del día 1 (°C): "))
temp2 = float(input("Ingrese la temperatura del día 2 (°C): "))
temp3 = float(input("Ingrese la temperatura del día 3 (°C): "))
temp4 = float(input("Ingrese la temperatura del día 2 (°C): "))
temp5 = float(input("Ingrese la temperatura del día 3 (°C): "))

celsius=(temp1,temp2,temp3,temp4,temp5)

f1=temp1*9/5+32
f2=temp2*9/5+32
f3=temp3*9/5+32
f4=temp4*9/5+32
f5=temp5*9/5+32

fahrenheit=(f1,f2,f3,f4,f5)

print("temperaturas en °C:",celsius)
print("temperaturas en °F:",fahrenheit)

#---edad-promedio-con-listas------------------

edades=[int(input("edad 1:")),int(input("edad 2:")),int(input("edad 3:")),int(input("edad 4:")),int(input("edad 5:"))]
promedio=sum(edades)/len(edades)
print(f"mayor:{max(edades)},menor:{min(edades)},promedio:{promedio}")

#---diccionario-de-frutas---------------------

frutas={
    "manzana": 7000,
    "pera": 6000,
    "banano": 8000
}
print(frutas)
pedido=int(input("¿cuantos kilos de manzana quiere?: "))
pedido2=int(input("¿cuantos kilos de pera quiere?: "))
pedido3=int(input("¿cuanros kilos de banano quiere?: "))
 
total_manzana = pedido * frutas["manzana"]
total_pera = pedido2 * frutas["pera"]
total_banano = pedido3 * frutas["banano"]

total_general = total_manzana + total_pera + total_banano

print(f"\nTotal por manzanas: ${total_manzana}")
print(f"Total por peras: ${total_pera}")
print(f"Total por bananos: ${total_banano}")
print(f"\nTotal a pagar: ${total_general}")

#---suma-de-elementos-en-tupla-------------------

numeros=(1,2,3,4,5)
suma=sum(numeros)
print(f"la suma total de los elemtos es:",suma)"""

#---inventario-con-lista-de-diccionarios--------------

nombre1 = input("Nombre del producto 1: ")
cantidad1 = int(input("Cantidad: "))
precio1 = int(input("Precio: "))

nombre2 = input("Nombre del producto 2: ")
cantidad2 = int(input("Cantidad: "))
precio2 = int(input("Precio: "))

nombre3 = input("Nombre del producto 3: ")
cantidad3 = int(input("Cantidad: "))
precio3 = int(input("Precio: "))

total1 = cantidad1 * precio1
print(total1)
total2 = cantidad2 * precio2
total3 = cantidad3 * precio3