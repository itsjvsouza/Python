import random

s1 = str(input("Enter the name of the first student: "))
s2 = str(input("Enter the name of the second student: "))
s3 = str(input("Enter the name of the third student: "))
s4 = str(input("Enter the name of the last student: "))

students_list = [s1, s2, s3, s4]

random.shuffle(students_list)

print(f"The order of the students is: {students_list}")
