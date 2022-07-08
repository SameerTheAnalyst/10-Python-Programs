import random
num = random.randint(1,100)
guess = []
guess_count = 0
guess_limit = 10
out_of_guesses = False

print("Welcome!")
print("This is a guessing game where you will have to guess a random number between 1 and 100")
print("You will be given a hint after each guess, and you will have 1 tries to guess the number")
print("GOOD LUCK!!!\n")

while guess != num and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("Enter your guess: "))
        guess_count += 1
        if guess > num:
            print("Hint: The number is less then your current guess!\n")
        if guess < num:
            print("Hint: The number is greater then your current guess!\n")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Sorry, your are out of guesses, try again next time!")
else:
    print("Congratulations, You WON!!!")