from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'hard' or 'easy': ")
if choose_difficulty == "easy":
    print("You have 10 attempts!")
    number_of_guess = 10
else:
    number_of_guess = 5
    
game_is_over = False

random_number = random.randrange(1, 101)
while not game_is_over:
    
    user_guess = int(input("Please pick a number between 1 and 100. "))
    
    if user_guess > random_number:
        number_of_guess -= 1
        print("Your number is too high.")
        print(f"Number of guesses left: {number_of_guess}")
    elif user_guess < random_number:
        number_of_guess -= 1
        print(" Your number is too low.")
        print(f"Number of guesses left: {number_of_guess}")
   
    if user_guess == random_number:
        game_is_over = True
        print(f"You guessed the correct number {random_number}, good job, YOU WIN!")

    if number_of_guess == 0:
        game_is_over = True
        print(f"You ran out of guesses. Game Over! the number was {random_number}")