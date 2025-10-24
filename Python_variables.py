#variable name
age = 17
name = 'Hassaan'
#valid characters
# A-Z, a-z, 0-9, _
#Finding type
x = 10
y = 20.8
z = 'Hassan'
print(type(x))
print(type(y))
print(type(z))
#Casting
print(int(60.76))
print(float(92))
print(str(90))
#Case sensitive
name = "Hassan"
Name = "Mahmood"
#Variable names
#Camle case
myName = 'Hassaan'
#Pascal case
MyName = 'Hassan'
#Snake case
my_name = 'Hassan'
#Assign multiple value in single line
#Multiple value for multiple variables
a , b ,c = "Hassaan" , "Mahmood" , "Ahmad"
print(a)
print(b)
print(c)
#One value for multiple variables
p = q = r = "Pakistan"
#Global function
#By using def[myfunc]
x = "hassaan"

def myfunc():
    print("My name is " + x)

myfunc()
#---------------------------
x = "one"

def myfunc():
    x = "friend"
    print("You are my " + x)

myfunc()

print("Allah is " + x)
#Global keyword
def myfunc():
    global x
    x = "country"

myfunc()

print("I love my " + x)