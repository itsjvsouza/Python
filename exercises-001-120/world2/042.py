r1 = float(input("Enter the value of the first line of the triangle: "))
r2 = float(input("\nEnter the value of the second line of the triangle: "))
r3 = float(input("\nEnter the value of the third line of the triangle: "))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print("It is not possible to form a triangle with these lines.")

elif r1 != r2 and r1 != r3 and r2 != r3:
    print("The triangle formed is scalene.")

elif r1 == r2 and r2 == r3:
    print("The triangle formed is equilateral.")

else:
    print("The triangle formed is isosceles.")
