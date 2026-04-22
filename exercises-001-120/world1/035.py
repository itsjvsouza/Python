r1 = float(input("Enter the value of the first line: "))
r2 = float(input("\nEnter the value of the second line: "))
r3 = float(input("\nEnter the value of the third line: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("It is possible to form a triangle with these lines.")

else:
    print("It is not possible to form a triangle with these lines.")
