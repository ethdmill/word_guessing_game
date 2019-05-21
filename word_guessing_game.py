# DESKTOP GIT PATH  cd /d/projects/programming/projects/python/02_word_guessing_game/main
# LAPTOP GIT PATH   cd c/users/e/projects/programming/projects/python/02_word_guessing_game/main


import random
# import os (need for clear_screen() below)
from words import *


# Initial variable declarations
win = False
main_loop = True
previous_answer = ""


# Clears prompt upon each guess for cleaner experience
# Commented out for potential future use based on test feedback
# def clear_screen():
#     os.system("cls")


# Visually divides each guess
def print_divider():
    print("\n" + ("|" * 100) + "\n")


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


# Checks for >1 or ==1 attempts remaining in order to display a grammatically correct warning message
def remove_attempt():
    if attempts > 1:
        print("Oops! You have {} attempts left.\n".format(attempts))
        you_have_tried()
    elif attempts == 1:
        print("Careful, you only have {} attempt left!\n".format(attempts))
        you_have_tried()


# Function that runs at end of game, accessed by changing win conditions
def end_of_game():

    # These variables needs to be global to affect two outer loops
    global main_loop
    global user_continue
    global keep_going
    global previous_answer
    end_of_game_loop = True

    while end_of_game_loop == True:

        keep_going = input("Would you like to keep going? Y/N\n").lower().replace(" ", "")

        # Checks for "recursion" answer from previous game iteration for easter egg ;)
        if answer == "recursion":
            previous_answer = answer

        try:
            if keep_going.isalpha() and (keep_going == "y" or keep_going == "n"):

                # If they want to continue, loop restarts
                if keep_going == "y":
                    user_continue = True
                    end_of_game_loop = False

                # If they don't want to continue, loop breaks, program ends
                elif keep_going == "n":
                    print_divider()
                    print("Thanks for playing!")
                    print_divider()
                    user_continue = False
                    main_loop = False
                    end_of_game_loop = False

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
    start = input("Please press S to start, Q to quit, or R to view the rules, followed by Enter/Return to confirm.\n").lower().replace(" ", "")
    user_continue = True

    try:
        if start.isalpha() and (start == "s" or start == "q" or start == "r"):

            # Loop that controls game after initial start input is received
            while user_continue == True:

                # Sets answer as "recursion" if previous_answer was assigned "recursion"
                # If so, this also permanently sets the answer as "recursion" from then on until the user exits the program
                if previous_answer == "recursion":
                    answer = "recursion"
                else:
                    answer = random.choice(word_bank)

                # Initial in-game variable declarations
                answer_dashes = "-" * len(answer)
                attempts = 0

                # Gameplay/Rules section, only displayed if chosen
                if start == "r":
                    print_divider();
                    print("HOW TO PLAY:\n\n"
                    "The rules are simple! A word will be selected at random.\n" +
                    "You will have a set number of attempts to guess the word.\n" +
                    "The word will be displayed, hidden by a corresponding amount of dashes.\n" +
                    "You can guess one letter at a time, or the whole word at once.\n" +
                    "To enter a guess, type in your letter/word and press enter.\n" +
                    "If you guess a letter correctly, you don't lose any attempts.\n" +
                    "However, if you guess wrong, you lose an attempt!\n" +
                    "\nBe careful! If you run out of guesses, it's game over!")
                    print_divider();
                    break

                # Conditional to begin game
                if start == "s":

                    # Answer length check to determine user's number of guess attempts
                    if len(answer) <= 10:
                        attempts = 15
                    else:
                        attempts = 20

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

                                                # Replaces any applicable "-" characters with letter stored in guess
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
                                            print_divider()
                                            if attempts >= 1:
                                                remove_attempt()
                                            else:
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
                elif start == "q":
                    print_divider()
                    print("Come back soon!")
                    print_divider()
                    main_loop = False
                    break


                # If win_condition is met, function at top of program is called, prompting replay
                if win == True:
                    print_divider()
                    print("Ding ding ding! The answer was \"{}\"!\nIt took you {} tries to guess the answer.\nCongratulations, you win!\n".format(answer, number_of_tries))
                    end_of_game()


        else:
            print_divider()
            raise ValueError("Oops, please enter either S, Q, or R!\n")

    except ValueError as err:
        print("{}".format(err))
