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
print(f"la suma total de los elemtos es:",suma)

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

producto1 = {
    "nombre": nombre1, 
    "cantidad": cantidad1, 
    "precio": precio1
    }

producto2 = {
    "nombre": nombre2, 
    "cantidad": cantidad2, 
    "precio": precio2
    }

producto3 = {
    "nombre": nombre3, 
    "cantidad": cantidad3, 
    "precio": precio3
    }

inventario=[producto1,producto2,producto3]
total = sum(producto["cantidad"] * producto["precio"] for producto in inventario)
print("\nInventario:")
for producto in inventario:
    print(producto)

#---modificar-una-lista-de-precios-------------------------------

precio1 = int(input("Precio del producto 1: "))
precio2 = int(input("Precio del producto 2: "))
precio3 = int(input("Precio del producto 3: "))
precio4 = int(input("Precio del producto 4: "))
precio5 = int(input("Precio del producto 5: "))

precios=[precio1,precio2,precio3,precio4,precio5]
descuento=float(input("ingrese el porcentaje de descuento(%): "))

precio1_desc = precio1 * (1 - descuento / 100)
precio2_desc = precio2 * (1 - descuento / 100)
precio3_desc = precio3 * (1 - descuento / 100)
precio4_desc = precio4 * (1 - descuento / 100)
precio5_desc = precio5 * (1 - descuento / 100)

precios_con_descuento = [precio1_desc, precio2_desc, precio3_desc, precio4_desc, precio5_desc]

print("Precios con descuento:", precios_con_descuento)


#---notas-con-tuplas-------------------------------------------

nota1=float(input("nota1:"))
nota2=float(input("nota2:"))
nota3=float(input("nota3:"))
nota4=float(input("nota4:"))

notas=(nota1,nota2,nota3,nota4)
print("nota mas alta:",max(notas))
print("nota mas baja:",min(notas))

#---diccionario-de-conversiones----------------------------------

equivalencias={
    "km": 1000,
    "m": 1,
    "cm": 0.01
}
cantidad=float(input("ingrese una cantidad: "))
unidad=input("ingrese la unidad(km, m, cm): ")
metros = cantidad * equivalencias.get(unidad, 0)
print(metros, "metros")

#---lista-de-productos-mas-IVA--------------------------------------

precio1=float(input("Precio 1: "))
precio2= float(input("Precio 2: "))
precio3= float(input("Precio 3: "))

precios=[precio1,precio2,precio3]
precio_con_IVA=[precio1*1.19,precio2*1.19,precio3*1.19]

print("precios", precios)
print("precios con IVA", precio_con_IVA)

#---tupla-de-operaciones-matematicas------------------------------

num=int(input("ingrese un numero:"))
num2=int(input("ingrese otro numero:"))

operaciones=(num+num2, num-num2, num*num2, num/num2)
print("resultados de la suma, resta, multiplicaion y division entre ambos numeros:",operaciones)

#---diccionario-de-estudiantes-------------------------------------

valores={
    "sofia": 3.0,
    "nicolk": 4.9,
    "annjely": 4.0
}

print(sum(valores.values()) / len(valores))

#---lista-de-salarios---------------------------------------------------

salario1=float(input("ingrese el salario:"))
salario2=float(input("ingrese el salario:"))
salario3=float(input("ingrese el salario:"))
salario4=float(input("ingrese el salario:"))
salario5=float(input("ingrese el salario:"))

salarios_nuevos=[salario1*1.1, salario2*1.1, salario3*1.1, salario4*1.1, salario5*1.1]
print(salarios_nuevos)

#---diccionario-de-impuestos--------------------------------------------

productos = {
    'manzana': 100,
    'pan': 50,
    'leche': 80
}

impuesto = float(input("Porcentaje de impuesto (%): "))

for producto, precio in productos.items():
    precio_final = precio * (1 + impuesto / 100)
    print(f"{producto}: {precio_final:.2f}")

#---analisis-de-lista-de-edades---------------------------------------

edad1=int(input("ingrese una edad: "))
edad2=int(input("ingrese una edad: "))
edad3=int(input("ingrese una edad: "))

mayores = (edad1 >= 18) + (edad2 >= 18) + (edad3 >= 18)
menores = 3 - mayores

print("Mayores de edad:", mayores)
print("Menores de edad:", menores)

#---tupla-de-conversiones-de-monedas---------------------------------

dolares = float(input("Cantidad en dólares: "))

euros = dolares * 0.85
pesos = dolares * 17.0
yenes = dolares * 110.0

conversiones = (euros, pesos, yenes)

print("Esa cantidad en euros, pesos, yenes es:", conversiones)

#---diccionario-de-ventas--------------------------------------------

productos={
    "leche": 3,
    "pan": 5,
    "queso": 3
}
total = sum(productos.values())
print("Total de unidades vendidas de los tres productos es:", total)

#---lista-de-temperaturas-extremas-------------------------------------

temperaturas=[5,9,18,20,25,30,35,40,45,47]

arriba = [t for t in temperaturas if t > 30]
abajo = [t for t in temperaturas if t < 10]

print("Temperaturas arriba de 30°:", arriba)
print("Temperaturas de 10° o menos:", abajo)

#---actualizar-precios-con-metodos-de-listas----------------------------

precios=[100,200,1000,5000,2500]
print(precios)

eliminar = int(input("Precio a eliminar: "))
precios.remove(eliminar)

agregar = int(input("Precio a agregar: "))
precios.append(agregar)

precios.sort()
print("Lista ordenada:", precios)"""

