my_string = "My String"
my_othher_string = "Mi otro String"

print(len(my_string))
print(len(my_othher_string))

print(my_string + my_othher_string)

print(my_string + " - " + my_othher_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_new_line_string = "\\tEste es un String\\ncon salto de linea"
print(my_new_line_string)

name, surname, age = "Jolman   ", "Gordillo", 25
print("Mi nombres es" + name + " " + surname  + " y mi edad es " + str(age))

# s = String
# f = Float
# d = entero

# Esta es la version con %
print("Mi nombre es %s %s y mi edad es %s, prueba %d" % (name, surname, age,(2000 - 2025)))

# Esta es la version con {}
print("Mi nombre es {} {} y mi edad es {}, prueba {}".format(name, surname, age, (2000 - 2025)))

numero =  432.43214234321423
print(f"Mi nombre es {name} {surname} y mi edad es {type(numero)}")

language = "Python"

a,b,c,d,e,f = language

print(a)
print(e)

print('Division')



print(language.capitalize())
# 1. Primera letra en mayúscula
print(language.upper())
# 2. Todo en mayúsculas
print(language.count("t"))
# 3. Cuenta cuántas veces aparece "t
print(language.isnumeric())
# 4. Verifica si todos los caracteres son numéricos
print("1".isnumeric())
# 5. Ejemplo: True porque "1" es un número
print(language.lower())
# 6. Todo en minúsculas
print(language.upper().isupper()) 
# 7. Comprueba si está en mayúsculas 
print(language.startswith("py")) 
# 8. Este método verifica si la cadena 
# almacenada en la variable language no empieza con el texto "py"




# Almacenar una palabra en la variable language
language = "python"

# 1. La palabra con la primera letra en mayúscula
print("1. Primera letra en mayúscula:", language.capitalize())

# 2. La palabra completamente en mayúsculas
print("2. Completamente en mayúsculas:", language.upper())

# 3. Cuántas veces aparece la letra 'p' en la palabra
print("3. Veces que aparece 'p':", language.count('p'))

# 4. Si la palabra está formada únicamente por números
print("4. ¿Es numérica?:", language.isnumeric())

# 5. Comprobación numérica usando el texto "1"
print("5. ¿'1' es numérico?:", "1".isnumeric())

# 6. La palabra en minúsculas
print("6. En minúsculas:", language.lower())

# 7. Si la palabra está completamente en mayúsculas
print("7. ¿Está en mayúsculas?:", language.isupper())

# 8. Si la palabra comienza con "py"
print("8. ¿Comienza con 'py'?:", language.startswith("py"))