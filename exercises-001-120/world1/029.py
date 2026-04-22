v = int(input("What is the car's speed? "))

if v > 80:
    print("\nYou have been fined!")
    print(f"\nYou will pay ${(v - 80) * 7} in fines.")

else:
    print("You are within the speed limit!")
    