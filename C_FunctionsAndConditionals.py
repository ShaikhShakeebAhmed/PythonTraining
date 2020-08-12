#Functions and Conditionals
def mean(myList):
  the_mean = sum(myList) / len(myList)
  return the_mean

print(mean([9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9])) #>> OR

studentGrade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

print(mean(studentGrade))

print(type(mean) , type(sum))
