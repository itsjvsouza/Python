import random

num = random.randint(0, 10)
counter = 0
user_num = -1

while user_num != num:
    user_num = int(input("\nTry to guess which number I chose between 0 and 10: "))
    counter += 1

    if user_num == num:
        print(f"\033[32mYou guessed the number correctly!\033[m \nGuesses needed: {counter}")
    else:
        print("\033[31mTry again!\033[m")
