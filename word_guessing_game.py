# DESKTOP GIT PATH  cd /d/projects/programming/projects/python/02_word_guessing_game/main
# LAPTOP GIT PATH   cd c/users/e/projects/programming/projects/python/02_word_guessing_game/main


# TO-DO:

# [x] list of words, one selected at random on program start
# [x] collect user input for letters
# [x] certain number of attempts (less attempts for smaller words?)
# [x] word is shown to user as ------- with correctly guessed letters displayed
# [x] be sure to send every user input to lowercase just in case of auto-caps
# [x] if initial input isn't Y or N, throw an error
# [x] if user guess is correct, display answer_dashes but replace dashes with correct letters guessed
# [x] if guess input is a number, throw an error
# [x] display congratulations message on whole word success, better luck next time on failure
# [x] ask if user would like to play again; if yes, loop, if no, break loop
# [x] test functionality, check for line spacing
# [ ] comment all the things
# [ ] add more words to word_bank


import random


# Initial variable declarations to keep loops in line
user_continue = True
win = False
main_loop = True


# Function that runs at end of game, accessed by changing win conditions
def end_of_game():
    try:

        # This variable needs to be global to affect main user_continue loop
        global user_continue

        keep_going = input("Would you like to keep going? Y/N\n").lower()

        # If they want to continue, loop restarts
        if keep_going == "y":
            user_continue = True

        # If they don't want to continue, loop breaks, program ends
        elif keep_going == "n":
            print("Thanks for playing!")
            user_continue = False
            main_loop = False

        # If they enter some inane value, error throws
        else:
            raise ValueError("Oops, please enter either Y or N!\n")

    except ValueError as err:
        print("{}".format(err))



# Start-up message
print("Hello! Let's play a word game!\n")


while main_loop == True:

    # Initial input to start the game
    start = input("Please press Y to begin or N to quit.\n").lower()

    try:
        if start.isalpha() and (start == "y" or start == "n"):

            while user_continue == True:

                # Initial variable declarations
                word_bank = ["these", "are", "test", "words"]
                answer = random.choice(word_bank)
                answer_dashes = "-" * len(answer)
                attempts = 0


                # Conditional to begin game
                if start == "y":

                    # Answer length check to determine user's number of guess attempts
                    if len(answer) <= 5:
                        attempts = 5
                        print("You have {} attempts left.\n".format(attempts))
                    elif 5 < len(answer) <= 10:
                        attempts = 10
                        print("You have {} attempts left.\n".format(attempts))
                    elif 10 < len(answer) <= 15:
                        attempts = 15
                        print("You have {} attempts left.\n".format(attempts))
                    else:
                        attempts = 20
                        print("You have {} attempts left.\n".format(attempts))

                    # Nested loop for guessing letters, based on number of remaining attempts
                    print(answer_dashes)
                    win = False
                    temp_answer = answer_dashes
                    while attempts > 0 and win == False:

                        try:
                            guess = input("Guess a letter, or guess the whole word!\n").lower()

                            # Ensures guess is comprised of letters
                            if guess.isalpha():

                                try:
                                    # Ensures guess is either a single letter or the length of the answer
                                    if len(guess) == 1 or len(guess) == len(answer):

                                        temp_answer = list(answer_dashes)

                                        # If their guess is part of answer but isn't the whole answer, this runs
                                        if guess in answer and guess != answer:

                                            guess_position = -1
                                            i = 0
                                            while i < len(answer):

                                                temp_answer = list(temp_answer)

                                                # This stores the index of every guess in answer as guess_position once per iteration without repeating indeces
                                                guess_position = answer.find(guess, guess_position + 1)

                                                if guess_position != -1 and guess == answer[guess_position]:
                                                    temp_answer[guess_position] = guess

                                                if guess_position == -1:
                                                    break

                                            temp_answer = "".join(temp_answer)

                                            # Once the culmination of their guesses matches answer, they win
                                            if temp_answer == answer:
                                                win = True
                                                break

                                            else:
                                                print("\nSo far, you have {}.".format(temp_answer))
                                                print("Nice work, keep going!\n")

                                        # If their guess is the whole word, immediate win
                                        elif guess == answer:
                                            win = True
                                            break

                                        # If their guess doesn't appear in answer, they lose an attempt
                                        else:
                                            attempts -= 1
                                            if attempts > 1:
                                                print("Oops! You have {} attempts left.\n".format(attempts))
                                                temp_answer = "".join(temp_answer)
                                                print(temp_answer)
                                            elif attempts == 1:
                                                print("Careful, you only have {} attempt left!\n".format(attempts))
                                                temp_answer = "".join(temp_answer)
                                                print(temp_answer)
                                            else:
                                                print("Oh no, you're out of attempts!\nThe answer was \"{}\". Please try again!\n".format(answer))
                                                end_of_game()

                                    else:
                                        raise ValueError("Oops, you can only enter a single letter or the exact length of the word!\nThe length of the word is represented by the dashes.\n")
                                        temp_answer = "".join(temp_answer)
                                        print(temp_answer)

                                except ValueError as err:
                                    print("{}".format(err))


                            else:
                                raise ValueError("Please enter letters only!\n" + "\n" + temp_answer)

                        except ValueError as err:
                            print("{}".format(err))


                # Exit message if user selected N at very beginning
                elif start == "n":
                    print("Come back soon!")
                    main_loop = False
                    break


                # If win_condition is met, function at top of program is called, prompting replay
                if win == True:
                    print("Ding ding ding! The answer was \"{}\"!\nCongratulations, you win!\n\n".format(answer))
                    end_of_game()

        else:
            raise ValueError("Oops, please enter either Y or N!\n")

    except ValueError as err:
        print("{}".format(err))
