my_condition = 5*2 #resultado 10

if my_condition == 11:
        print("se ejecuta la condicion del segundo if")
if my_condition == 10:
        print("se ejecuta la condicion del segundo if")
                

my_string = "mi cadena de texto"




# condicionales

my_condition = True

if my_condition:
    print("Se ejecuta la condicion del if")

print("La ejecucion continua")

# if que no se cumple
my_condition = 5 * 2  # 10
if my_condition == 11:
    print("Se ejecuta la condicion del segundo if")

# if que se cumple
if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

# else
if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")
print("La ejecucion continua")

# and / or
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
print("La ejecucion continua")

# elif
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
print("La ejecucion continua")

# strings vacios en condicionales
my_string = ""
if my_string:
    print("Mi cadena de texto no esta vacia")
else:
    print("Mi cadena de texto esta vacia")

# uso de not con strings
my_string = "Mi cadena de texto"
if not my_string:
    print("Mi cadena de texto esta vacia")
else:
    print("Mi cadena de texto no esta vacia")

# ejemplo not del manual
print(not (3 > 4))