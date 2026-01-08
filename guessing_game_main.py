from art import logo
import random
def play_game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("\nI'm thinking of a number between 1 to 100.")

    """choose random number"""
    def choose_number():
        return random.randrange(1,101)

    hidden_number = choose_number()
    #print(hidden_number) """computer's guess"""

    """difficulty setting"""
    level= {"easy" : 10,"medium" : 8, "hard" : 5}
    while True:
        user_choice = input("Choose the difficulty level! type easy / medium / hard! ").lower()
        if user_choice in ["easy" , "medium" , "hard"]:
            break
        else:
            print("❌ Invalid input. Please type valid level.")

    """difficulty validation"""
    def difficulty():
        if user_choice in level:
            print(f"you have {level[user_choice]} attempts left for guessing the right number.")
            return level[user_choice]
        else:
            print("invalid difficulty")
            return 0

    attempts = difficulty()

    game_over = False
    previous_guess = []

    print("\n--------GAME STARTED--------")

    """game logic"""

    while not game_over and attempts > 0:
        while True:
            try:
                user_guess = int(input("Guess the number... "))
                break
            except ValueError:
                print("❌ Please enter a valid number. Without any symbol or latter.")

        if user_guess in previous_guess:
            print(f"⚠️ You've already guessed that number : {user_guess}, 'Guess another one'.")
            continue

        if user_guess > 100 or user_guess <= 0:
            print("You went over!, please guess between 1 to 100.")
            continue

        difference = abs(user_guess - hidden_number)
        if user_guess < hidden_number:
            if difference <= 5:
                print("🔥 Very close!")
            elif difference <= 10:
                print("Close")
            else:
                print("Too low")
            attempts -= 1
            previous_guess.append(user_guess)
            print(f"Attempts left: {attempts}")

        elif user_guess > hidden_number:
            if difference <= 5:
                print("🔥 Very close!")
            elif difference <= 10:
                print("Close")
            else:
                print("Too high")
            attempts -= 1
            previous_guess.append(user_guess)
            print(f"Attempts left: {attempts}")

        elif user_guess == hidden_number:
            print("------------You did it!------------")
            print(f"The correct number was {hidden_number}")
            print("You got the right number, Game over.")
            game_over = True

        print(f"Previous guesses: {previous_guess}")


    if attempts == 0:
        game_over = True
        print("you run out of attempts.\n -------Game over-------")
        print(f"The correct number was {hidden_number}")

while True:
    play_game()
    user_mind = input("do you want to play again? type y or n ").lower()

    if user_mind != "y":
        print("thanks for playing, goodbye!")
        break
