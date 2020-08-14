#Basic for loop
studentGradeget = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

for grade in studentGradeget:
  print(round(grade))

for strings in "Shakeeb":
  print(strings)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for x in colors:
    if x > 50:
        print (x)


for x in colors:
    if type(x) == int and x > 50:
        print (x)

#For loop on dictionaries
phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}

for items in phone_numbers.items():
  print(items)

#>> Loop on Keys

for items in phone_numbers.keys():
  print(items)

#>> Loop on values 

for items in phone_numbers.values():
  print(items)