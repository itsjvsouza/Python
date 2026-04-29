over_18 = 0
mens = 0
women_under_20 = 0

while True:
    age = int(input("\nEnter the age of the person: "))
    gender = input("Enter the gender of the person (M/F): ").lower()

    if age > 18:
        over_18 += 1

    if gender == "m":
        mens += 1

    if gender == "f" and age < 20:
        women_under_20 += 1
    
    choise = input("\nDo you want to continue? (Y/N): ").lower()

    if choise == "n":
        break

print(f"\nQuantity of people over 18 years old: {over_18}")
print(f"Quantity of men: {mens}")
print(f"Quantity of women under 20 years old: {women_under_20}")
