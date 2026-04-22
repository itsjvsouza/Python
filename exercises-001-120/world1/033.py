n1 = float(input("Enter the first number: "))
n2 = float(input("\nEnter the second number: "))
n3 = float(input("\nEnter the third number: "))

if n1 > n2 and n1 > n3:
    
    if n2 < n3:
        print(f"The largest is {n1} and the smallest is {n2}.")
    
    else:
        print(f"The largest is {n1} and the smallest is {n3}.")

elif n2 > n1 and n2 > n3:

    if n1 < n3:
        print(f"The largest is {n2} and the smallest is {n1}.")

    else:
        print(f"The largest is {n2} and the smallest is {n3}.")

else:

    if n1 < n2:
        print(f"The largest is {n3} and the smallest is {n1}.")

    else:
        print(f"The largest is {n3} and the smallest is {n2}.")
