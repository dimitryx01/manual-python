# dicts (diccionarios)

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

# claves y valores de distintos tipos
my_other_dict = {
    "Nombre": "Geral",
    "Apellido": "Lopez",
    "Edad": 35,
    1: "Python"
}
print(my_other_dict)

# valor que es un set
my_dict = {
    "Nombre": "Geral",
    "Apellido": "Lopez",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
}
print(my_dict)

# len cuenta claves (no elementos internos)
print(len(my_other_dict))
print(len(my_dict))

# acceder por clave
print(my_dict["Nombre"])

# modificar valor
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# agregar nueva clave
my_dict["Calle"] = "Calle nou"
print(my_dict)

# eliminar una clave concreta
del my_dict["Calle"]
print(my_dict)

# in en diccionarios busca en claves, no en valores
print("geral" in my_dict)   # False (no es clave)
print("Nombre" in my_dict)  # True

# metodos
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# fromkeys (crea un dict nuevo)
my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "geraldin")
print(my_new_dict)