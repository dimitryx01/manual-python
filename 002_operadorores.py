# operadores

# operadores aritmeticos
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

# operador modulo (%)
print(3 % 4)
print(10 % 3)

# division entera //
print(10 // 3)

# potenciacion **
print(2 ** 3)

# concatenacion de strings con +
print("hola " + "Python")

# ejemplos de operaciones invalidas con strings (el manual las muestra, pero fallan)
print("hola" + "python")
# print("hola" - "python")  # esto da TypeError
# print("hola" * "python")  # esto da TypeError

print("Hola " + "Python " + "¿Qué tal?")

# no se puede concatenar string con int directamente
# print("Hola " + 5)  # TypeError
print("Hola " + str(5))  # solucion

# repetir strings con *
print("hola" * 5)

# repetir con float falla
# print("hola" * 2.5)  # TypeError

# actividad propuesta: convertir antes a int
my_float = 2.5 * 2
print("Hola" * int(my_float))

# operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# comparaciones entre strings
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Hola")
print("aaaa" > "abaa")                 # ordenacion alfabetica (unicode)
print(len("aaaa") > len("abaa"))       # cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# operadores logicos: and, or
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")

# prioridad de operadores (parentesis, not, and, or)
print(3 < 4 or ("Hola" > "Python" and 4 == 4))

# operador not
print(not (3 > 4))