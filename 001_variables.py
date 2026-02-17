# variables en python (segun el manual)

my_string_variable = "my string variable"
print(my_string_variable)

# variables incorrectas (ejemplos, no ejecutar)
# first-name
# first@name
# first$sname
# num-1
# 1num

# hagamos algunas variables
Myvariable = "My string variabel "
print(Myvariable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# print con varios valores
print(my_string_variable, my_int_variable, my_bool_variable)

# funcion str y type
my_int_variable = 5
print(my_int_variable)

# variables y conversion de tipos en python
my_int_to_str_variable = str(my_int_variable)  # transformamos el entero a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

print(my_string_variable, str(my_int_variable), my_bool_variable)

# funcion len
print(len(my_string_variable))

# variables en una sola linea (el manual dice que se puede, pero no es buena practica)
name, surname, alias, age = "Geraldin", "Lopez", "Geral", 35
print("Mi nombre es:", name, surname, "mi alias es:", alias, "y mi edad es:", age)

# funcion input() (comentado para que no bloquee al ejecutar)
"""
first_name = input("Cual es tu nombre: ")
age = input("Cuantos anos tienes: ")
print(first_name)
print(age)
"""

# cambio de tipo de dato (tipado dinamico)
# cambiamos su tipo
name = 34
age = "geral"
print(name)
print(age)

# podemos "forzar" el tipo (en realidad python es dinamico, aqui solo reasignamos)
# forzamos el tipo
addres = str("Mi direccion")
addres = 32
addres = True
addres = 2.2
print(type(addres))