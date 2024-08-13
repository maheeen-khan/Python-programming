#Unpacking
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

a = "awesome"

def myfunc1():
  a = "fantastic"
  print("Python is " + a)

myfunc1()

print("Python is " + a)

#To create a global variable inside a function, you can use the global keyword.

def myfunc2():
  global b
  b = "fantastic"

myfunc2()

print("Python is " + b)

#Also, use the global keyword if you want to change a global variable inside a function.

c = "awesome"

def myfunc3():
  global c
  c = "fantastic"

# myfunc3()

print(" f3 : Python is " + c)

#complex data type
d = complex(1j)

#display x:
print(d)

#display the data type of x:
print(type(d)) 