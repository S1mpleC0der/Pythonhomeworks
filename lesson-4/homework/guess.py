import random

def guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10
        print("Number between 1 and 100. You have 10 attempts!")

        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("You guessed it right!")
                break
        else:
            print("You lost. Want to play again?")
        
        replay = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ").strip().lower()
        if replay not in ['y', 'yes', 'ok']:
            print("Thanks for playing!")
            break


guessing_game()
