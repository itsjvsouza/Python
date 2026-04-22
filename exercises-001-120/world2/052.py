num = int(input("Enter an integer: "))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        print(f"\nThe number {num} is not prime.")
        is_prime = False
        break

if is_prime == True:
    print(f"\nThe number {num} is prime.")
