my_list=[]
my_other_list=[2,3,4,5,53,2,5,4,4,3,2,]

print(my_other_list[0]) #muestra 
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])

print(my_other_list[-1])#acceder al ultimo elemento
print(my_other_list[-2])#acceder al penultimo elemento

print(my_other_list[4])


print(my_other_list.count("Geral"))
print(my_list.count(30))

age, height,name,surname= my_other_list

name,height,age,surname = my_other_list[2],my_other_list[1]

print(age)
print(name)

#concatenar listas

print(my_list+my_other_list)

my_list="hola python"

print(my_list)
print(type(my_list))


my_other_list.append("ilerna")

print(my_other_list)

# append
my_other_list.append("Ilerna")
print(my_other_list)

# insert y modificar por indice
my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

# remove (elimina la primera coincidencia)
my_list.remove(30)
print(my_list)

# pop
print(my_list.pop())     # ultimo elemento
print(my_list)
print(my_list.pop(2))    # elemento en posicion 2
print(my_list)

# del por indice
del my_list[2]
print(my_list)

# clear
my_list.clear()
print(my_list)

# copy + clear (mantener copia independiente)
my_list = [1, 2, 3, 4]
my_new_list = my_list.copy()
my_list.clear()
print("original:", my_list)
print("copia:", my_new_list)

# reverse y sort
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 