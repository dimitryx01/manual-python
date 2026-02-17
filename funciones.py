
def my_function():
    print("esto es una funcion")
    
my_function()
my_function()
my_function()


def sum_two_values(first_number, second_number):
    print(first_number+second_number)
    
sum_two_values(5,7)
sum_two_values(54754,71231)
sum_two_values(1.4,5.2) #tipo float


sum_two_values("5","7")
def sum_two_values(first_number:int,second_number:int):
    print(first_number+second_number)
    
sum_two_values("5","7")
    
    
def sum_two_values_with_return(first_value,second_value):
    return first_value+second_value

sum_two_values_with_return(10,5)
    
        
my_result = sum_two_values_with_return(10,5)
print(my_result)        


def print_name(name,surname):
    print(f"{name}{surname}")
    
print_name("lopez","geral")

    
def print_name(name,surname):
    print(f"{name}{surname}")
    
print_name(surname="lopez",name="geral")    


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        