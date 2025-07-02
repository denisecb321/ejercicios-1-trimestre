"""persona={
    "nombre":"Denise",
    "edad":"17",
    "l_nacimiento":"Palmira",
}
print(persona)
#-------------------------

auto={
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 2022
}
print(auto)
#--acceder-a-valor---------------
print(auto["modelo"])
#--modificar-valor---------------
auto["año"]=2023
print(auto)
#--añadir-elemento---------------
auto["color"]="rojo"
print(auto)
#--eliminar-valor----------------
del auto["modelo"]
print(auto)
#--.pop-------------------------
auto.pop("año")
print(auto)

#--ejemplo2-.del------------------------------

auto={"marca":"toyota","modelo":"corolla"}
del auto["modelo"]
print(auto)

#--ejemplo3-.pop------------------------------

auto={"marca":"toyota","modelo":"corolla"}
valor=auto.pop("marca")
print(valor)
print(auto)

#------------------------------

color=auto.pop("color","no especifico")
print(color)"""