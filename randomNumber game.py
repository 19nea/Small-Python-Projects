import random  # for taking random number

# welcome message
welcome = input(
    'Welcome to a simple guessing game! Are you ready to play? Y/N: ').lower()

# dificulties
EASY = 100
MEDIUM = 10
HARD = 5


# the game
def play():
    if welcome != 'y':
        print("Maybe next time!")
        quit()
    # asking user what dificulty he would like
    difficulty = input(
        'Great! Please select a difficulty: Easy(e) - 100 tries, Medium(m) - 10 tries, Hard(h) - 5 tries: ').lower()

    if difficulty == 'e':
        TRIES = EASY
    elif difficulty == 'm':
        TRIES = MEDIUM
    elif difficulty == 'h':
        TRIES = HARD
    else:
        print("Invalid difficulty. Try again next time! ")
        quit()

    # defining maximum number
    max_number = int(
        input("Alright! What is the maximum number you would like to guess? "))
    secret_number = random.randint(1, max_number)

    # actual game
    while TRIES > 0:
        guess = int(
            input(f"You have {TRIES} tries left. What is your guess? "))
        TRIES -= 1
        # winning message
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        else:
            print("Wrong guess.")

    # fail message
    if TRIES == 0 and guess != secret_number:
        fail = input(
            f"Sorry! You've used all your tries. The number was {secret_number}. Would you like to try again? Y/N: ").lower()
        if fail == 'y':
            play()
        else:
            print('thank you for playing')


# play the game
play()
