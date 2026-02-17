# sets

my_set = set()       # conjunto vacio
my_other_set = {}    # dict vacio (importante)

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Geral", "Lopez", 35}
print(type(my_other_set))

print(len(my_other_set))

# add
my_other_set.add("Geral")
print(my_other_set)

# duplicados: solo guarda valores unicos
my_other_set = {"Geral", "Lopez", 35, "Geral"}
print(my_other_set)

# in
print("Geral" in my_other_set)
print("Lopez" in my_other_set)

# remove
my_other_set = {"Python", "Geral", "Developer"}
my_other_set.remove("Geral")
print(my_other_set)

# clear
my_other_set.clear()
print(my_other_set)

# del borra la variable completa
my_other_set = {"Python", "Geral", "Developer"}
del my_other_set
# print(my_other_set)  # NameError si lo descomentas

# convertir set a list (para usar indices)
my_set = {"Geraldin", "Sanchez", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

# union
my_other_set = {"java", "php", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# difference e intersection
print("Diferencia:", my_new_set.difference(my_set))
print("Interseccion:", my_set.intersection(my_other_set))
print("my_other_set:", my_other_set)