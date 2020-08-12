#if you do not have anu IDE for python use https://repl.it/

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

print(dir(list))
help(str.upper)
print("shakeeb".upper())
print("SHAKEEB".lower())
print("shakeeb".title())

#getting a list of builtin functions and types everything available in your environment

print(dir(__builtins__))

#calculating avarage step by step

studentGrade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

print(help(len))

totalNumberofItems = len(studentGrade)

sumofStudentsGrades = sum(studentGrade)

print(totalNumberofItems)
print(sumofStudentsGrades)

mean= sumofStudentsGrades/totalNumberofItems

print(mean)

#getting max and count of a specific value

maximum = max(studentGrade)

print(maximum)

countOfCertainValue = studentGrade.count(10.0)

print(countOfCertainValue)

#Dictionary type getting mean of student Grades

studentGradeDictionary = {"Shakeeb":10 , "Zubair":20 , "Nabeel":50 , "Adeel":100}


totalNumberofItems = len(studentGradeDictionary)

sumofStudentsGrades = sum(studentGradeDictionary.values())

print(totalNumberofItems)
print(sumofStudentsGrades)

mean= sumofStudentsGrades/totalNumberofItems

print(mean , " For Students" , studentGradeDictionary.keys())

#Tuple like a list but cannot be edited

color_codes = ((1,2) , (3,4) , (5,6))

print(color_codes)

#Complex dictionary

day_temperatures = {'morning': [10.1,11.1,12.3] , 'noon': (11.1,22.2,33.3) , 'evening': (44.4,55.5,66.6)}

print(day_temperatures)