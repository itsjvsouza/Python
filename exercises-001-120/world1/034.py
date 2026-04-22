salary = float(input("Enter your salary: "))

if salary <= 1250:
    print(f"Your salary of ${salary} becomes ${salary + (salary * 0.15)}")

else:
    print(f"Your salary of ${salary} becomes ${salary + (salary * 0.1)}")
