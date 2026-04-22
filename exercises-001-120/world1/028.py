import random

num = random.randint(0, 5)

user_num = int(input("Try to guess which number I chose between 0 and 5: "))

if user_num == num:
    print("You guessed the number correctly!")

else:
    print("You guessed the wrong number!")
