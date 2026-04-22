grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
average = (grade1 + grade2) / 2

if average < 5:
    print("\n\033[1;31mFAILED\033[m\n")

elif average >= 5 and average < 7:
    print("\n\033[1;33mRECOVERY\033[m\n")

else:
    print("\n\033[1;32mAPPROVED\033[m\n")
