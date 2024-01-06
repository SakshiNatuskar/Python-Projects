import random

options = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissor")
        or (player == "paper" and computer == "rock")
        or (player == "scissor" and computer == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("Thanks for playing!")
