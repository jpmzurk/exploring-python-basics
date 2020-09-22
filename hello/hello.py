msg = "Hello World"
print(msg)

msg
msg.capitalize()
msg.split()


myint = 7
print(myint)

someString = 'hello'
print(someString)

someString = "hello"
print(someString)


one = 1
two = 2
three = one + two
print(three)

a, b = 3, 4
print(a,b)


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# creates a empty list 
nums = []  
  
# appending data in list 
nums.append(21) 
nums.append(40.5) 
nums.append("String") 
  
print(nums) 

programming_languages = "Python", "Java", "C++", "C#"

for language in programming_languages:
    print(language)

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for row in game:
    print(row)


x = dict(name="John", age=36)

#display x:
print(x)


def my_function():
      print("Hello from a function")

my_function()


def someFunction (x, y):
    z = x + y
    print(z)

someFunction(4, 6)