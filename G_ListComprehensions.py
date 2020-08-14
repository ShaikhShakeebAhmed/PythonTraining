#List comprehension
studentGradeget = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

grade = [temp / 10 for temp in studentGradeget]

print(grade)

#>> with If Conditional

grade2 = [temp / 10 for temp in studentGradeget if temp != 10.0]

print(grade2)

#>> with Else Conditional

grade3 = [temp / 10  if temp != 10.0 else 0 for temp in studentGradeget ]

print(grade3)

