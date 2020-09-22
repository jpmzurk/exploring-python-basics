
INSTALL PYTHON:

in terminal run this command:
 brew install python

 making a variable is: 

x = "Hello World"	str	
x = 20	            int	
x = 20.5            float

type does not need to be declared but can be

x = str("Hello World")	
x = int(20)	
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)	
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))

an example of writing to the console might be: 

myint = 7
print(myint)


**DATA STRUCTURES 

an array looks like:

programming_languages = "Python", "Java", "C++", "C#"

for such an example a for loop printing each string to console might look like:

for language in programming_languages:
    print(language)

* note the indentation on the second line. it must be present


an object in python is dictionary. an object must be declared as "dict()":

x = dict( name="John", age= 37)

print(x)

print(type(x)) 
A
** FUNCTIONS

def someFunction (x, y):
    z = x + y
    print(z)

someFunction(4, 6)

output will give you 10# exploring-python-basics
