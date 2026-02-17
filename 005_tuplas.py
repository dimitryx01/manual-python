# tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.60, "Geral", "Lopez")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

# index error (ejemplos, no ejecutar)
# print(my_tuple[4])
# print(my_tuple[-6])

# nota: si usas [] creas una lista, no una tupla
my_tuple = [35, 1.77, "Geral", "Lopez"]
print(type(my_tuple))

# volvemos a tupla para seguir con el tema
my_tuple = (35, 1.60, "Geral", "Lopez")

print(my_tuple.count("Geral"))
print(my_tuple.index("Geral"))
print(my_tuple.index("Lopez"))

# las tuplas son inmutables (ejemplo que falla)
# my_tuple[1] = 1.80  # TypeError

# concatenacion de tuplas
my_other_tuple = ("Python", "Developer")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# convertir tupla a lista para modificar
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "Ilerna"      # reemplazo
my_tuple.insert(1, "Azul")  # insercion
print(my_tuple)

# volver a convertir a tupla
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del en tuplas: borra la variable completa
del my_tuple
# print(my_tuple)  # NameError si lo descomentas