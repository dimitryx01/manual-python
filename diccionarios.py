my_dict = dict ()


my_other_dict = {
    "Nombre": "Geral",
    "Apellido": "Lopez",
    "Edad": 35,
    1: "Python"
}
my_dict = {
    "Nombre": "Geral",
    "Apellido": "Lopez",
    "Edad": 35,
    "'Lenguajes": {"Python", "Swift", "Kotlin"},
    "1": "algún vpython"
}
print (my_other_dict)
print (my_dict)

my_dict['calle']="calle nou"
print(my_dict)

del my_dict["calle"]#eliminar el elemento dentro del diccionario

#del my_dict  borra todo el diccionario

print("geral" in my_dict) #busca la clave geral pero como no la encuentra retorna false

my_new_dict = my_other_dict.fromkeys (("Nombre", 1)) #crea un nuevo diccionario con esas claves y valor None
print (my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,"geraldin")
print (my_new_dict)
