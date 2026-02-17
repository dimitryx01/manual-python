#definicion de una clase vacia

class MyEmptyPerson:
    pass

print(MyEmptyPerson)


#el init crea un objeto cada que se llama la clase
class Person:
    def __init__(self,name,surname):
            pass

#cuando eliminamos el pass y usamos el self estamos trabajando directamente con la instancia del objeto, self hace referencia al propio objeto
        
  
class Person2:
     def __init__(self,name,surname):
         self.name=name
         self.surname = surname

my_person = Person("Geral","jolman")


class Person:
    def __init__(self,name,surname):
         self.full_name=f"{name}{surname}"
    def walk(self):
        print(f"{self.full_name} esta caminando" )      
                 
       #crear un objeto
    
my_person = Person("Geral", "Lopez")     
       #mostras el atributo
print(my_person.full_name)   

#ejecutar el metodo
my_person.walk()   
                 
                 
                 
                 
#crear un objeto
      
my_person2 = Person("Geral", "Lopez")                  

#acceder al atributo
print(my_person2.full_name)

#ejecutar el metodo
my_person2.walk()   

#modificar directamente el atributo
my_person2.full_name="Andres (el loco de los gatos)"

#volver a mostrar el atributo
print(my_person2.full_name)

