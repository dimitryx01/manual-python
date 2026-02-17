my_tupla=(32,1.80,"jolman","gordillo")

print(my_tupla)
print(type(my_tupla))

print(my_tupla[0])
print(my_tupla[-1])

my_tupla2=[32,1.80,"jolman","gordillo"]
print(type(my_tupla)) #esto no es una tupla porque se cambio de () a []

print(my_tupla.count("jolman"))#cuenta cuantas veces aparece
print(my_tupla.index("jolman"))#para ubicar el indice del elemento en la dupla

#my_tupla[1]=1.90
print(my_tupla)

my_tupla=list(my_tupla)#se puede convertir a list
print(type(my_tupla))



my_tupla3=set(my_tupla)#lo convertimos a set
print(type(my_tupla3))

my_tupla3={"jolman","yobany","gordillo",35,1.80}
print(my_tupla3)
my_tupla3.add("geral")
print(my_tupla3)

my_tupla3.remove("jolman")
print(my_tupla3)