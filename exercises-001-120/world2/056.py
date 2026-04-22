total_sum = 0
women_under_20 = 0
oldest_age = 0
oldest_name = ""

for i in range(4):
    name = input(f"Enter the name of the {i + 1}st person: ")
    gender = input(f"Enter the gender of the {i + 1}st person (M/F): ").lower()
    age = int(input(f"Enter the age of the {i + 1}st person: "))

    total_sum += age

    if gender == "f" and age < 20:
        women_under_20 += 1

    if gender == "m" and age > oldest_age:
        oldest_age = age
        oldest_name = name

average = total_sum / 4

print(f"\nThe average age of the group is: {average:.0f}")
print(f"The oldest man in the group is: {oldest_name}")
print(f"Quantity of women under 20 years old: {women_under_20}")
