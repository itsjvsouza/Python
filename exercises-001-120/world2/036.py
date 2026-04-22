value = float(input("Enter the house value: "))
salary = float(input("Enter your salary: "))
years = int(input("In how many years do you intend to pay? "))

installment = value / (years * 12)

if installment > salary * 0.3:
    print("Your loan was denied!")

else:
    print("Your loan was approved!")
