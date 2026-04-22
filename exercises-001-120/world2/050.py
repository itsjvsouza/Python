total_sum = 0

for i in range(0, 6):
    num = int(input("Enter the number: "))
    
    if num % 2 == 0:
        total_sum += num

print(f"\nThe sum of the even numbers is: {total_sum}")
