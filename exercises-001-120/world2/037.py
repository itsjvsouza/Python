num = int(input("Enter an integer number: "))
base = int(input("""
1 - Binary
2 - Octal
3 - Hexadecimal
                 
Choose the conversion base: """))

if base == 1:
    print(f"\n{num} converted to binary is: {bin(num)}")

elif base == 2:
    print(f"\n{num} converted to octal is: {oct(num)}")

elif base == 3:
    print(f"\n{num} converted to hexadecimal is: {hex(num)}")

else:
    print("\nInvalid option.")
