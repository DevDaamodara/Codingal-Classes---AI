import random

string_list = ["rock", "paper", "scissors"]


while True:
    user_input = input("Please choose a option from rock, paper, scissors.").lower()

    if user_input == "quit":
        print("Game over!, thank you for playing.")
    if user_input not in string_list:
        print("Sorry, invalid option!")
        continue
    choice = random.choice(string_list)
    print(f"Computer chose {choice}")

    if user_input == choice:
        print("It's a tie!")

    elif (user_input == "rock" and choice == "scissors") or (user_input == "paper" and choice == "rock") or (user_input == "scissors" and choice == "paper"):
        print("You Win!!!")
    else:
        print("You lose, try again next time!")