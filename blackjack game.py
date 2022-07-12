import random
num = random.randint(1,100)
guess = []
guess_count = 0
out_of_guesses = False
print("Welcome to the Number Guessing Game!")
print("\nI am thinking of a number between 1 and 100, can you guess it?")
difficulty = input("\nChoose a difficulty, Type 'easy' or 'hard': ")
if difficulty.lower() == "easy":
    guess_limit = 10
    print("\nYou have 10 attempts to guess the number between 1 and 100")
    while guess != num and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = int(input("Enter your guess: "))
            guess_count += 1
            if guess > num + 10:
                print("Your number is too high\n")
            elif guess > num:
                print("Your number is high\n")
            elif guess < num - 10:
                print("Your number is too low\n")
            elif guess < num:
                print("Your number is low\n")
        else:
            out_of_guesses = True
    if out_of_guesses:
        print(f"Sorry, your are out of guesses, the number was {num}")
    else:
        print("Congratulations, You WON!!!")
elif difficulty.lower() == "hard":
    guess_limit = 5
    print("\nYou have 5 attempts to guess the number between 1 and 100")
    while guess != num and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = int(input("Enter your guess: "))
            guess_count += 1
            if guess > num + 10:
                print("Your number is too high\n")
            elif guess > num:
                print("Your number is high\n")
            elif guess < num - 10:
                print("Your number is too low\n")
            elif guess < num:
                print("Your number is low\n")
        else:
            out_of_guesses = True
    if out_of_guesses:
        print(f"Sorry, your are out of guesses, the number was {num}.")
    else:
        print("Congratulations, You WON!!!")
else:
    print("Invalid Command")
