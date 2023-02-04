import random

print("Welcome to the guessing game!")
print("Guess a number between 1 and 10.")

random_number = random.randint(1, 10)
guessed = False

while not guessed:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You got it! The number was", random_number)
        guessed = True
    elif guess < random_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

print("Thanks for playing!")
