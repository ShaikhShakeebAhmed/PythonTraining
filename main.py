#Importing and printing example
import datetime

mynow = datetime.datetime.now()

print("The Date time is " ,mynow)

#Declaring Variables no need of type declarations as they are declared implicitly 
x = 1 #Number
y = "1" #String
z = 10.1 #float

print(x,y,z) 

print(x + z)

#List data types and examples of range()

listtype = list(range(1,11))

print(listtype)

anotherList = [1,2,3,4,5,6,7,8,9]

print(anotherList)

temperatures = [1 , 2.1 , "1"]

print(temperatures)

rainfall = [1 , 2.1 , "1" , temperatures]

print(rainfall)

#dir() and help() examples
dir(list)
help(list.append)