highest_weight = 0
lowest_weight = 1000

for i in range(5):
    weight = int(input(f"Enter the weight of the {i + 1}st person: "))

    if weight > highest_weight:
        highest_weight = weight

    if weight < lowest_weight:
        lowest_weight = weight

print(f"\nThe highest weight was {highest_weight}kg.")
print(f"The lowest weight was {lowest_weight}kg.")
