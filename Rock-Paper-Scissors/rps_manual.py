import random

def get_computer_choice():
    options=["rock","paper","scissor"]
    computer_choice = random.choice(options)
    # print("Computer plays:", computer_choice)
    return computer_choice

def get_user_choice():
    user_choice = input("Enter your choice: \n")
    if type(user_choice) is not str:
        raise ValueError("The choice should be a string")
    if (user_choice !="rock" and user_choice!="paper" and 
        user_choice!="scissor"):
        raise ValueError("Invalid choice inputted")
    return user_choice

def get_winner(computer_choice,user_choice):
    if(computer_choice == "rock" and user_choice == "rock"):
        print("Draw")
    elif(computer_choice == "rock" and user_choice == "paper"):
        print("User wins")
    elif(computer_choice == "rock" and user_choice == "scissor"):
        print("Computer wins")
    elif(computer_choice == "paper" and user_choice == "paper"):
        print("Draw")
    elif(computer_choice == "paper" and user_choice == "rock"):
        print("Computer wins")
    elif(computer_choice == "paper" and user_choice == "scissor"):
        print("User wins")
    elif(computer_choice == "scissor" and user_choice == "scissor"):
        print("Draw")
    elif(computer_choice == "scissor" and user_choice == "paper"):
        print("User wins")
    else:
        print("Computer wins")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice,user_choice)

play()

    