import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

running = True

while  running:
    while player not in options:
        player = input("enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it's a tie")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win! ")
    else:
        print("you lose.")
    break


