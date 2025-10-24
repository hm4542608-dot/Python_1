#1. Write a Python function show_message() that defines a local variable msg = "Hello, Bilal!" and prints it.Then, try to print msg outside the function and observe what happens

def show_message():
   
   msg = "Hello, Bilal!"
   print(msg)

show_message()  
  
#2.Create a global variable count = 5.
#Define a function update_count() that increases the value of count by 10 using the global keyword.
#After calling the function, print count outside the function to confirm it has been updated.

count = 5
def update_count():
    global count
    count = 10
update_count()
print(count)    


#5.Create a function add_numbers(a, b) that prints the sum of two numbers.
#Call it with at least three different pairs of numbers.

def add_numbers(a,b):
    print(a + b)
add_numbers(5,10)

#6.Write a function display_info(name, age) that prints something like:
#"Name: Bilal, Age: 23"
#Call the function using keyword arguments, for example:

#display_info(age=23, name="Bilal")

def display_info(name, age):
    print("Name:" + name )
    print("Age:" + str(age) )
display_info(age=23, name="Bilal")   


#7. Create a function country_name(country="Pakistan") that prints:
#"I live in <country>".
#Call it once with an argument and once without to see the default value in action.

def country_name(country="Pakistan"):
    print("I live in "+ country) 
country_name("India")    
