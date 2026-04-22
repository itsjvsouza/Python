value = float(input("Enter the product value: "))
method = int(input("""
1 - Cash money/check
2 - Cash on card
3 - 2x on card
4 - 3x or more on card
What is the payment method? """))

if method == 1:
    print(f"Amount to pay: {value - (value * 0.1)}")

elif method == 2:
    print(f"Amount to pay: {value - (value * 0.05)}")

elif method == 3:
    print(f"Amount to pay: {value}")

elif method == 4:
    print(f"Amount to pay: {value + (value * 0.2)}")

else:
    print("Invalid option.")
