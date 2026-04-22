year = int(input("What year were you born? "))
age = 2026 - year

if age == 18:
    print("\nYou must enlist this year.")

elif age < 18:
    
    if 18 - age == 1:
        print("\nThere is 1 year left for you to enlist.")
    
    else:
        print(f"\nThere are {18 - age} years left for you to enlist.")

else:

    if age - 18 == 1:
        print("\nYou are 1 year late!")
    
    else:
        print(f"\nYou are {age - 18} years late!")
