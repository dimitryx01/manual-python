alumnos = {}
#Cada alumno se guardará así:
alumnos["Jolman"] = {
    "edad": 32,
    "curso": "DAM2",
    "lenguajes": {"Python", "Java"},
    "nota": 7.5
}
alumnos["Ana"] = {
    "edad": 31,
    "curso": "DAM2",
    "lenguajes": {"PHP", "Java"},
    "nota": 8.5
}
alumnos["Sebastian"] = {
    "edad": 25,
    "curso": "DAM2",
    "lenguajes": {"Python", "Java","PHP","JavaScript"},
    "nota": 9.5
}

alumnos["pepito"] = {
    "edad": 19,
    "curso": "DAM2",
    "lenguajes": {"Python", "Java"},
    "nota": 7.5
}

alumnos["luis"] = {
    "edad": 22,
    "curso": "DAW1",
    "lenguajes": {"JavaScript", "HTML"},
    "nota": 4.5
}

alumnos["marta"] = {
    "edad": 18,
    "curso": "DAM1",
    "lenguajes": {"C++"},
    "nota": 9.2
}

while True:
    print("\n1. Mostrar alumnos")
    print("2. Buscar alumno")
    print("3. Añadir alumno")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for nombre, datos in alumnos.items():
            nota = datos["nota"]
            estado = ""

            if nota < 5:
                estado = "Suspenso"
            elif nota >= 5 and nota < 7:
                estado = "Aprobado"
            elif nota >= 7 and nota < 9:
                estado = "Notable"
            elif nota >= 9:
                estado = "Sobresaliente"

            print("---")
            print("Alumno:", nombre)
            print("Edad:", datos["edad"])
            print("Curso:", datos["curso"])
            print("Lenguajes:", datos["lenguajes"])
            print("Nota:", nota, "-", estado)

        print("\n--- ALUMNOS DESTACADOS (>18 años y nota >= 7) ---")
        for nombre, datos in alumnos.items():
            if datos["edad"] > 18 and datos["nota"] >= 7:
                print(nombre)

    elif opcion == "2":
        nombre_buscar = input("Dime el nombre: ")
        
        if nombre_buscar in alumnos:
            datos = alumnos[nombre_buscar]
            print("Encontrado:", datos)
        else:
            print("No existe ese alumno.")

    elif opcion == "3":
        nombre = input("Nombre nuevo: ")
        
        if nombre == "salir":
            continue

        edad = int(input("Edad: "))
        curso = input("Curso: ")
        texto_lenguajes = input("Lenguajes (separados por coma): ")
        nota = float(input("Nota: "))

        lista_lenguajes = texto_lenguajes.split(",")
        conjunto_lenguajes = set(lista_lenguajes)

        alumnos[nombre] = {
            "edad": edad,
            "curso": curso,
            "lenguajes": conjunto_lenguajes,
            "nota": nota
        }
        print("Alumno guardado.")

    elif opcion == "4":
        suma = 0
        cantidad = 0
        
        for datos in alumnos.values():
            suma = suma + datos["nota"]
            cantidad = cantidad + 1
        
        if cantidad > 0:
            print("La media de toda la clase es:", suma / cantidad)
        
        print("Adiós")
        break
    
    else:
        print("Opción incorrecta")