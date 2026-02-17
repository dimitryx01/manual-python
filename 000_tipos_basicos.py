# tipos basicos (resumen del inicio del manual)

# numeros
print(1)          # int
print(3.6)        # float
print(-5j)        # complex

# strings
print("hola python")
print("Hola Python")
print('Hola Python')

# booleanos
print(True)
print(False)

# lista, tupla, set, dict
mi_lista = [1, "hola", True, 3.5, [2, 4]]
mi_tupla = (1, "hola", True, 3.5)
mi_conjunto = {1, 2, 3, 3, 4}
mi_dict = {1: "1", 2: "2"}

print(mi_lista)
print(mi_tupla)
print(mi_conjunto)  # esperado: {1, 2, 3, 4}
print(mi_dict)

# type() para comprobar tipos
print(type("texto"))     # str
print(type(10))          # int
print(type(2.2))         # float
print(type(True))        # bool
print(type(1 + 2j))      # complex