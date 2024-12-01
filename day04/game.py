import numpy as np

# Compare guess to hidden number:
def check_guess(guess, hidden_number):
    if guess < hidden_number:
        print("Too small!")
    elif guess > hidden_number:
        print("Too big!")
    else:
        print(f"Correct! The number was {hidden_number}.")

# Process guess
def get_user_input():
    guess = input("Your guess (or enter 'x' to quit, 's' to cheat and see the number, 'n' to start a new game): ")
    
    if guess == "x":
        print("It was nice playing with you. Goodbye!")
        exit()  
    elif guess == "s":
        return 's'  
    elif guess == "n":
        return 'n'  
    
    if not guess.isdigit():
        print("Please enter a valid number")
        return None  
    
    return int(guess)  

# Game handling
def play_game():
    hidden_number = np.random.randint(1, 21)  
    guesses = 0
    print("Welcome to the Guessing Game! Guess the hidden number between 1 and 20")

    while True:
        guess = get_user_input()  

        if guess == 's':
            print(f"The hidden number is {hidden_number}.")
            continue
        elif guess == 'n':
            break

        if guess is None:  
            continue

        guesses += 1
        check_guess(guess, hidden_number)  

        if guess == hidden_number:
            print(f"You guessed the number in {guesses} attempts.")
            break 

# Main function:
def main():
    while True:
        play_game()  # Play the game
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == "no":
            print("Thank you for playing!")
            break
        elif replay == "yes":
            print("Starting a new game")
        else:
            print("Invalid input. Exiting the game")
            break

if __name__ == "__main__":
    main()
