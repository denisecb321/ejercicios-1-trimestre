texto="""Hamas y la "promocion de la democracia" Noam Chomsky

Hamas gano combinando una fuerte resistencia contra la ocupacion militar con la creacion de organizaciones sociales de base y de servicio a los pobres, una plataforma y una practica que probablemente haria ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo politicamente justo. Sin embargo, es útil recordar que en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967. ..

La posición de Washington hacia las elecciones en Palestina ha sido coherente. Las elecciones fueron postergadas hasta la muerte de Yasser Arafat, que fue recibida como una oportunidad para la realización de la "visión" de Bush sobre un eventual Estado palestino democrativo, que es una palido y vago reflejo del consenso internacional sobre una acuerdo de dos entidades estatales en la zona, que Estados Unidos viene bloqueando desde hace 30 años....

El compromiso formal de Hamas de "destruir Israel" lo pone a la par con Estados Unidos e Israel, que prometieron por mucho tiempo que no habria ningun "Estado palestino adicional" (aparte de Jordania", hasta que ambas naciones aflojaron parcialmente su posicion, para aceptar un mini Estado constituido por los fragmentos que queden despues que Israel se apropie de todas las partes de Palestina que desea....

Simplemente como conjetura, imagine el lector una inversion de las circunstancias: que Hamas permitiese a los israelies vivir en cantones desparramados e invariables, virtualmente separados unos de otros, y en alguna pequeña parte de Jerusalen, mientras los palestinos construyen enormes asentamientos y proyectos de infraestructura para apoderarse de las tierras y los recursos de Israel, Y que, ademas Hamas acepte llamar a esos fragmentos "un Estado". Si se hicieran propuestas para esta empobrecida "categoria de Estado", nosotros nos sentiriamos, con razon, horrorizados. Pero con ese tipo de propuestas, la posicion de Hamas seria esencialmente igual a la de Estados Unidos e Israel.

buscar=texto.find("empobrecida")
print(buscar)"""







texto="""También se entiende por comunismo la doctrina y filosofía política inspirada en ese sistema. 
Esta doctrina nació como una crítica al capitalismo y las desigualdades socioeconómicas 
del mercado derivadas de la distribución de la riqueza y la propiedad privada. 
Según los comunistas, todo ello genera una brecha entre clases sociales, frente a la que 
sugieren la abolición de la pzropiedad privada de los medios de producción para eliminar 
la división entre pobres y ricos.

busqueda1=texto.find("comunismo")
busqueda2=texto.find("ricos")

print(busqueda1)
print(busqueda2)"""




texto="""eres el mas fuerte porque eres satoru gojo o eres satoru gojo porque eres el mas fuerte

busqueda=texto.find("gojo")
print(busqueda)"""



texto1="""También se entiende por comunismo la doctrina y filosofía política inspirada en ese sistema. 
Esta doctrina nació como una crítica al capitalismo y las desigualdades socioeconómicas del mercado
 derivadas de la distribución de la riqueza y la propiedad privada."""

texto2="""También se entiende por comunismo la doctrina y filosofía política inspirada en ese sistema.
Esta doctrina nació como una crítica al capitalismo y las desigualdades socioeconómicas del mercado
 derivadas de la distribución de la riqueza y la propiedad privada.


print(texto1==texto2)


equipo=input("ingrese el nombre del equipo de futbol: ")
equipo1=int(input("ingrese los puntos del equipo 1: "))
equipo2=int(input("ingrese los puntos del equipo 2: "))
equipo3=int(input("ingrese los puntos del equipo 3: "))
equipo4=int(input("ingrese los puntos del equipo 4: "))
equipo5=int(input("ingrese los puntos del equipo 5: "))

suma=equipo1+equipo2+equipo3+equipo4+equipo5
promedio=suma/5
print(f"el promedio de los equipos es {promedio}")"""



texto1="Python es "
texto2="un lenguaje "
texto3="de programacion "
texto4="versatil"

print(f"objetivo:{texto1}{texto2}{texto3}{texto4}")