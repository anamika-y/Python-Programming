import random
choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
round_number = 1

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' to quit the game.\n")

while True:
    print(f"\nRound {round_number}")
    user_choice = input("Your choice: ").lower()

    if user_choice == 'exit':
        print("\nThanks for playing!")
        print(f"Final Score — You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in choices:
        print("❗ Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        result = "You win this round!"
        user_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    print(f"Result: {result}")
    print(f"Score — You: {user_score} | Computer: {computer_score}")
    round_number += 1
