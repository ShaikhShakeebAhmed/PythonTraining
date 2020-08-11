#Indexing a list

print(help(list.index))

studentGrade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

#>> search for 10.0 after index 3
print(studentGrade.index(10.0 , 3))

#>> Remove from the list
studentGrade.remove(10.0)
print(studentGrade)

#>> __getitem__ method on a list
studentGradeget = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(studentGradeget[3])

#>> Get and append item

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])

print(workdays)


