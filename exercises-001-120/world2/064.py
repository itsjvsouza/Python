num = 0
sum = 0
counter = 0

while num != 999:
    num = int(input("Enter an integer number: "))
    sum += num
    counter += 1

print(f"\nThe sum of the {counter} numbers given is: {sum - 999}")
