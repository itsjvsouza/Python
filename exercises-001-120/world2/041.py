year = int(input("What year were you born? "))
age = 2026 - year

if age >= 0 and age <= 9:
    print("LITTLE")

elif age > 9 and age <= 14:
    print("INFANTILE")

elif age > 14 and age <= 19:
    print("JUNIOR")

elif age > 19 and age <= 25:
    print("SENIOR")

elif age > 25:
    print("MASTER")

else:
    print("INVALID DATE")
