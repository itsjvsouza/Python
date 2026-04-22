import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
option = int(input("""
1 - rock
2 - paper
3 - scissors

What is your choice? """))

if option == 1:
    user_choice = "rock"

elif option == 2:
    user_choice = "paper"

elif option == 3:
    user_choice = "scissors"

else:
    print("Invalid option")

if user_choice == computer_choice:
    print(f"Draw! You both chose {user_choice}")

elif user_choice == "rock" and computer_choice == "paper":
    print(f"You lost! \nYou chose {user_choice} and the computer chose {computer_choice}.")

elif user_choice == "paper" and computer_choice == "scissors":
    print(f"You lost! \nYou chose {user_choice} and the computer chose {computer_choice}.")

elif user_choice == "scissors" and computer_choice == "rock":
    print(f"You lost! \nYou chose {user_choice} and the computer chose {computer_choice}.")

else:
    print(f"You won! \nYou chose {user_choice} and the computer chose {computer_choice}.")
