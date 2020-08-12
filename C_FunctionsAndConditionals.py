#Functions 
def mean(myList):
  the_mean = sum(myList) / len(myList)
  return the_mean

print(mean([9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9])) #>> OR

studentGrade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

print(mean(studentGrade))

print(type(mean) , type(sum))

#Function and Conditionals

def meanWithDecision(value):
  if type(value) == dict:  
    #Also can be used isinstance(value , dict)
    the_mean = sum(value.values()) / len(value)
  else:
    the_mean = sum(value) / len(value)

  return the_mean

randomDict = {"Shakeeb":10 , "Zubair":20 , "Nabeel":50 , "Adeel":100}

print(meanWithDecision(randomDict))

#>> AND & OR
x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")

#>> Greater than or less than

if x > 1:
    print("Yes")
elif x < 1:
    print("No")
else:
  print("None")
    

