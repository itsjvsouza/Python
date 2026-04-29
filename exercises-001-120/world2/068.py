import random

counter = 0

while True:
    user_choise = input("\nEven or odd? ").lower()
    if user_choise == "even":
        computer_choice = "odd"
    elif user_choise == "odd":
        computer_choice = "even"
    else:
        print("Invalid option.")
        continue

    num = int(input("\nEnter an integer number: "))
    random_num = random.randint(0, 10)
    sum = num + random_num

    if sum % 2 == 0 and user_choise == "even" or sum % 2 != 0 and user_choise == "odd":
        print("\033[32mYou won!\033[m")
        counter += 1
    else:
        print(f"\033[31mYou lost after winning {counter} in a row!\033[m")
        break
