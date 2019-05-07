# DESKTOP GIT PATH  cd /d/projects/programming/projects/python/02_word_guessing_game/main
# LAPTOP GIT PATH   cd c/users/e/projects/programming/projects/python/02_word_guessing_game/main


import random
from words import *


# Initial variable declarations
win = False
main_loop = True
previous_answer = ""


# Visually divides each guess
def print_divider():
    print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")


# Displays array of guessed letters to user
def you_have_tried():
    print("You have tried {}\n".format(guessed_letters))


# Tells user they've already guessed a letter, whether correct or incorrect
def already_guessed():
    print("You already guessed that one! You have {} attempts left.\n".format(attempts))
    you_have_tried()


# Gathers guessed letters into a list and sorts alphabetically
def sort_guesses():
    guessed_letters.append(guess)
    guessed_letters.sort()


# Function that runs at end of game, accessed by changing win conditions
def end_of_game():

    # These variables needs to be global to affect two outer loops
    global main_loop
    global user_continue
    global keep_going
    global previous_answer

    keep_going = input("Would you like to keep going? Y/N\n").lower().replace(" ", "")

    # Checks for "recursion" answer for easter egg ;)
    if answer == "recursion":
        previous_answer = answer

    try:
        if keep_going.isalpha() and (keep_going == "y" or keep_going == "n"):

            try:
                # If they want to continue, loop restarts
                if keep_going == "y":
                    user_continue = True

                # If they don't want to continue, loop breaks, program ends
                elif keep_going == "n":
                    print("Thanks for playing!")
                    user_continue = False
                    main_loop = False

                else:
                    user_continue = False
                    raise ValueError("Oops, please enter either Y or N!\n")

            except ValueError as err:
                print("{}".format(err))

        # If they enter some arbitrary value, error throws
        else:
            user_continue = False
            raise ValueError("Oops, please enter either Y or N!\n")

    except ValueError as err:
        print("{}".format(err))


# Start-up message
print("Hello! Let's play a word game!\n")

# This loop wraps whole program to re-prompt user for input to start/exit in various circumstances
while main_loop == True:

    # Initial input to start the game
    start = input("Please press Y to begin or N to quit, followed by Enter/Return to confirm.\n").lower().replace(" ", "")
    user_continue = True

    try:
        if start.isalpha() and (start == "y" or start == "n"):

            # Loop that controls game after initial start input is received
            while user_continue == True:

                # Sets answer as "recursion" if previous_answer was assigned "recursion"
                if previous_answer == "recursion":
                    answer = "recursion"
                else:
                    answer = random.choice(word_bank)

                # Initial in-game variable declarations
                answer_dashes = "-" * len(answer)
                attempts = 0

                # Conditional to begin game
                if start == "y":

                    # Answer length check to determine user's number of guess attempts
                    if len(answer) <= 5:
                        attempts = 10
                    elif 5 < len(answer) <= 10:
                        attempts = 15
                    elif 10 < len(answer) <= 15:
                        attempts = 20
                    else:
                        attempts = 25

                    print_divider()
                    print("You have {} attempts left.\n".format(attempts))

                    # Nested loop for guessing letters, based on number of remaining attempts
                    win = False
                    temp_answer = answer_dashes
                    guessed_letters = []
                    number_of_tries = 0
                    while attempts > 0 and win == False:

                        try:
                            print(temp_answer)
                            guess = input("\nGuess a letter, or guess the whole word!\n").lower().replace(" ", "")

                            # Ensures guess is comprised of letters
                            if guess.isalpha():

                                try:
                                    # Ensures guess is either a single letter or the length of the answer
                                    if len(guess) == 1 or len(guess) == len(answer):

                                        # If their guess is part of answer but isn't the whole answer, this runs
                                        if guess in answer and guess != answer:

                                            # Ensures following loop iterates through every character in answer
                                            guess_position = -1
                                            i = 0
                                            while i < len(answer):

                                                # Changes temp_answer to list in order to replace characters by index
                                                temp_answer = list(temp_answer)

                                                # This stores the index of every guess in answer as guess_position once per iteration without repeating indeces
                                                guess_position = answer.find(guess, guess_position + 1)

                                                # Replaces any applicable - characters with guess
                                                if guess_position != -1 and guess == answer[guess_position]:
                                                    temp_answer[guess_position] = guess

                                                if guess_position == -1:
                                                    break

                                            # Changes temp_answer back to string for displaying again to user
                                            temp_answer = "".join(temp_answer)

                                            # Once the culmination of their guesses matches answer, they win
                                            if temp_answer == answer:
                                                number_of_tries += 1
                                                win = True
                                                break

                                            # Tells user they've already guessed a correct letter if they try it again
                                            elif guess in guessed_letters:
                                                print_divider()
                                                already_guessed()

                                            # Adds guess to guessed_letters list and continues loop
                                            else:
                                                number_of_tries += 1
                                                print_divider()
                                                print("Nice work, keep going! You have {} attempts left.\n".format(attempts))
                                                sort_guesses()
                                                you_have_tried()

                                        # If their guess is the whole word, immediate win
                                        elif guess == answer:
                                            number_of_tries += 1
                                            win = True
                                            break

                                        # If they have already guessed a letter, it will tell them
                                        elif guess in guessed_letters:
                                            print_divider()
                                            already_guessed()

                                        # If their guess doesn't appear in answer, they lose an attempt
                                        else:

                                            # If their guess is a single character and not in the answer or the guessed_letters list, it is added to the list
                                            if len(guess) == 1 and not len(guess) == len(answer) and guess not in guessed_letters:
                                                sort_guesses()

                                            # Removes an attempt with extra flavor text based on amount of remaining attempts
                                            number_of_tries += 1
                                            attempts -= 1
                                            if attempts > 1:
                                                print_divider()
                                                print("Oops! You have {} attempts left.\n".format(attempts))
                                                you_have_tried()
                                            elif attempts == 1:
                                                print_divider()
                                                print("Careful, you only have {} attempt left!\n".format(attempts))
                                                you_have_tried()
                                            else:
                                                print_divider()
                                                print("Oh no, you're out of attempts!\nThe answer was \"{}\". Please try again!\n".format(answer))
                                                end_of_game()

                                    else:
                                        print_divider()
                                        raise ValueError("Oops, you can only enter a single letter or the exact length of the word!\nThe length of the word is represented by the dashes.\n\nYou have {} attempts left.\n".format(attempts))

                                except ValueError as err:
                                    print("{}\nYou have tried {}\n".format(err, guessed_letters))


                            else:
                                print_divider()
                                raise ValueError("Please enter letters only! You have {} attempts left.\n".format(attempts))

                        except ValueError as err:
                            print("{}\nYou have tried {}\n".format(err, guessed_letters))


                # Exit message if user selected N at very beginning
                elif start == "n":
                    print("Come back soon!")
                    main_loop = False
                    break


                # If win_condition is met, function at top of program is called, prompting replay
                if win == True:
                    print_divider()
                    print("Ding ding ding! The answer was \"{}\"!\nIt took you {} tries to guess the answer.\nCongratulations, you win!\n".format(answer, number_of_tries))
                    end_of_game()

        else:
            raise ValueError("Oops, please enter either Y or N!\n")

    except ValueError as err:
        print("{}".format(err))
