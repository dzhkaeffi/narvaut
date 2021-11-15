name = input("Enter first name: ")
grades = input("Enter grades: ")
a = 0
b = 0
for char in grades:
    if char.lower() == "a":
        a += 1
    if char.lower() == "b":
        b += 1
print('Hello {}, your grades are {}'.format(name.title(), grades.upper()))
print('You have {} grades'.format(len(grades)))
print('Your grade for the second course is {}'.format(grades[1].upper()))
print('The number of A`s and B`s is {}'.format(a + b))
