# DESKTOP GIT PATH  cd /d/projects/programming/projects/python/02_word_guessing_game/main
# LAPTOP GIT PATH   cd c/users/e/projects/programming/projects/python/02_word_guessing_game/main


# TO-DO:

# [x] list of words, one selected at random on program start
# [x] collect user input for letters
# [x] certain number of attempts (less attempts for smaller words?)
# [x] word is shown to user as ------- with correctly guessed letters displayed
# [x] be sure to send every user input to lowercase just in case of auto-caps
# [x] if initial input isn't Y or N, throw an error
# [ ] if user guess is correct, display answer_dashes but replace dashes with correct letters guessed
# [ ] if guess input is a number, throw an error
# [x] display congratulations message on whole word success, better luck next time on failure
# [x] ask if user would like to play again; if yes, loop, if no, break loop
# [ ] add more words to word_bank
# [ ] test functionality, check for line spacing
# [ ] comment all the things


import random


# Start-up message
print("Hello! Let's play a word game!\n")

user_continue = True

while user_continue == True:

    # Initial variable declarations
    word_bank = ["vociferous"]
    answer = random.choice(word_bank)
    answer_dashes = "-" * len(answer)
    attempts = 0

    # Initial input to start game
    try:
        start = input("Please press Y to begin or N to quit.\n").lower()

        # Conditional to begin game
        if start == "y":

            # Answer length check to determine user's number of guess attempts
            if len(answer) <= 5:
                attempts = 5
                print("You have {} attempts left.".format(attempts))
            elif 5 < len(answer) <= 10:
                attempts = 10
                print("You have {} attempts left.".format(attempts))
            elif 10 < len(answer) <= 15:
                attempts = 15
                print("You have {} attempts left.".format(attempts))
            else:
                attempts = 20
                print("You have {} attempts left.".format(attempts))

            # Nested loop for guessing letters, based on number of remaining attempts
            win = False
            win_condition = False
            temp_answer = answer_dashes
            while attempts > 0 and win == False:

                try:
                    guess = input("Guess a letter, or guess the whole word!\n").lower()

                    if guess.isalpha():

                        if guess in answer and guess != answer:

                            # code to go here:

                            # guess is checked against answer
                            # temp_answer turns into some combination of answer_dashes and answer_dashes

                            if temp_answer == answer:
                                win_condition = True
                                break

                            else:
                                print("So far, you have {}.\n".format(temp_answer))
                                print("Nice work, keep going!")


                        elif guess == answer:
                            win_condition = True
                            break

                        else:
                            attempts -= 1
                            if attempts > 1:
                                print("Oops! You have {} attempts left.\n".format(attempts))
                            elif attempts == 1:
                                print("Careful, you only have {} attempt left!\n".format(attempts))
                            else:
                                print("Oh no, you're out of attempts! Please try again!\n")

                    else: raise ValueError("Please enter letters only!\n")

                except ValueError as err:
                    print("{}".format(err))


        # Exit message if user selected N at very beginning
        elif start.lower() == "n":
            print("Come back soon!")
            break

        # Error in case user enters some other random letter/number/whatever
        else:
            raise ValueError("Oops, please enter either Y or N!\n")

    except ValueError as err:
        print("{}".format(err))


    # If win_condition is met, function at top of program is called, prompting replay
    if win_condition == True:
        
        print("Ding ding ding! The answer was {}!\nCongratulations, you win!\n\n".format(answer))

        try:
            keep_going = input("Would you like to keep going? Y/N\n").lower()
            if keep_going == "y":
                win = True
            elif keep_going == "n":
                print("Thanks for playing!")
                user_continue = False
                break
            else:
                raise ValueError("Oops, please enter either Y or N!\n")

        except ValueError as err:
            print("{}".format(err))
