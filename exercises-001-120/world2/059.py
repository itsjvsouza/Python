while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    choise = int(input("""
[ 1 ] add
[ 2 ] multiply
[ 3 ] larger
[ 4 ] new numbers
[ 5 ] exit the program

Choose the operation: """))

    if choise == 1:
        print(f"\n{num1} + {num2} = {num1 + num2}")
    elif choise == 2:
        print(f"\n{num1} x {num2} = {num1 * num2}")
    elif choise == 3:
        if num1 > num2:
            print(f"\n{num1} is greater than {num2}")
        else:
            print(f"\n{num2} is greater than {num1}")
    elif choise == 4:
        continue
    elif choise == 5:
        break
    else:
        print("\nInvalid option.")
