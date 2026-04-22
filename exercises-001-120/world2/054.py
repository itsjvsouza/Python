qty_of_age = 0
qty_under_age = 0

for i in range(7):
    year = int(input(f"Enter the birth year of the {i + 1}st person: "))
    if year <= 2007:
        qty_of_age += 1
    else:
        qty_under_age += 1

print(f"\n{qty_of_age} people are over 18 years old.")
print(f"{qty_under_age} people are under 18 years old.")
