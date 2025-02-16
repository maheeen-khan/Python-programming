arr = [2,3,4,5]
sq = lambda x : x * x
cube = lambda x : x * x * x

print("Cube: ",list(map(cube, arr)))
print("Square: ",list(map(sq, arr)))

# 2 : a Python program to find if a given string starts with a given character using Lambda. 
string = input("Enter a string: ")
char = input("Enter a character: ")

check = lambda x,y : True if x[0] == y else False

print(check(string,char))

#III. Python program to extract year, month, date and time using Lambda. 
import datetime

now = datetime.datetime.now()

year = lambda x : x.year
month = lambda x : x.month
day = lambda x : x.day
time = lambda x : x.time()

print("Year: ",year(now))
print("Month: ",month(now))
print("Day: ",day(now))
print("Time: ",time(now))