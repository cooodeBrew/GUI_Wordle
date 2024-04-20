# # Name: Tianqing Zou
# # UTEID: tz4654
# # replace <NAME> with your name and delete this line.
# #
# # On my honor, <Tianqing Zou>, this programming assignment is my own work
# # and I have not provided this code to any other student.
# #
# # Explain your added feature here:
# """
# I am bad at wordle and really need some hint while playing, so that's why I added a button for user to gain a hint.
# The function checks if the player has already used their wish by calling the cant_make_wish method of the board object.
# If the wish has been used, a message box is displayed to inform the player.
# Otherwise, the function retrieves the feedback and target word from the board object.
# If there is no feedback yet, a message is displayed to prompt the player to make a guess first.
# The function then iterates through the feedback to find the first letter that has not been correctly
# guessed yet (marked as 'G' for correct guesses). It then displays a hint message indicating the position
# and the correct letter at that position in the target word. Finally, the make_a_wish method of the board object
# is called to decrement the remaining wish count.
# """
#
# import random
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
#
#
# def get_words():
#     """
#     Reads from two files, 'secret_words.txt' and 'other_valid_words.txt',
#     to obtain a collection of secret words and all valid words respectively.
#     Converts all words to uppercase, removes leading and trailing whitespace,
#     and sorts the secret words alphabetically.
#     Returns a tuple containing the sorted secret words and a set of all valid words.
#     """
#     temp_secret_words = []
#     # Read and process secret words file
#     with open('secret_words.txt', 'r') as data_file:
#         all_lines = data_file.readlines()
#         for line in all_lines:
#             temp_secret_words.append(line.strip().upper())
#     temp_secret_words.sort()   # Sort secret words alphabetically
#     secret_words = tuple(temp_secret_words)
#
#     # Read and process other valid words file
#     all_words = set(secret_words)
#     with open('other_valid_words.txt', 'r') as data_file:
#         all_lines = data_file.readlines()
#         for line in all_lines:
#             all_words.add(line.strip().upper())
#     return secret_words, all_words
#
#
# class WordleBoard:
#     def __init__(self):
#         """
#                 Initializes a new WordleBoard object.
#                 - Initializes secret words and all words using the get_words() method.
#                 - Selects a random target word from the secret words.
#                 - Initializes feedback as an empty list.
#                 - Sets game_over to False and num_wish to 1.
#         """
#         self.__secret_words, self.__all_words = get_words()
#         self.__target_word = random.choice(self.__secret_words)
#         print(self.__target_word)
#         self.__feedback = []
#         self.__G_only_feedback = ['-', '-', '-', '-', '-']    # Will contain 'G' from all previous guesses
#         self.__game_over = False
#         self.__num_wish = 1
#
#     def get_target_word(self):
#         """Returns the target word the player needs to guess."""
#         return self.__target_word
#
#     def cant_make_wish(self):
#         """Returns True if the player cannot get another hint False otherwise."""
#         return self.__num_wish == 0
#
#     def make_a_wish(self):
#         self.__num_wish -= 1
#
#     def set_game_over(self):
#         self.__game_over = True
#
#     def get__game_over(self):
#         """Sets the game_over attribute to True, indicating the end of the game."""
#         return self.__game_over
#
#     def get_final_feedback(self):
#         return self.__feedback
#
#     def get_g_only_feedback(self):
#         return self.__G_only_feedback
#
#     def get_feedback(self, guess):
#         """
#                Computes and returns the feedback for a guessed word.
#                - Initializes feedback as a list of dashes ('-').
#                - Compares the guessed word with the target word and marks correct letters with 'G'.
#                - Marks correct letters in the wrong position with 'O'.
#          """
#         self.__feedback = ['-', '-', '-', '-', '-']
#         secret_word_copy = list(self.__target_word)
#         marked_green = []   # Store the index that already marked as 'G'
#         for index in range(len(guess)):
#             tgt = guess[index]
#             if secret_word_copy[index] == tgt:
#                 self.__feedback[index] = 'G'
#                 self.__G_only_feedback[index] = 'G'
#                 secret_word_copy[index] = '*'
#                 marked_green.append(index)
#         for index in range(len(guess)):
#             if index not in marked_green:
#                 tgt = guess[index]
#                 if tgt in secret_word_copy:
#                     self.__feedback[index] = 'O'
#                     id_of_letter = secret_word_copy.index(tgt)
#                     secret_word_copy[id_of_letter] = '*'
#         return self.__feedback
#
#     def valid_word(self, guess):
#         """
#                 Checks if a guessed word is valid (i.e., in the set of all words).
#                 Returns True if the word is valid, False otherwise.
#         """
#         if guess in self.__all_words:
#             return True
#         return False
#
#
# def main():
#     # Set the seed to make grading easier.
#     # Final version turned in must have this line
#     # of code. First three words with this seed
#     # should be AFFIX, PROXY, APING
#     random.seed(3252024)
#
#     root = Tk()
#     root.title("WORDLE")
#     root.resizable(False, False)
#     root.geometry('550x550')
#     guess_num = [1]
#     board = [WordleBoard()]
#     labels = create_labels(root)
#     info_label, info_var = create_control_buttons(root, labels, board, guess_num)
#     root.bind('<KeyPress>', lambda event: input_letter(event.char, labels,  guess_num, board, info_var))
#     root.bind('<BackSpace>', lambda event: undo_last_pick(labels, guess_num, board, info_var))
#     root.bind('<Return>', lambda event: enter_guess(labels, board, info_var, guess_num))
#
#     root.mainloop()
#
#
# def input_letter(letter, labels, guess_num, board, info_var):
#     """
#         Handles the input of a letter by the player.
#     """
#     if board[0].get__game_over():
#         info_var.set("Game over. Please start a new game.")
#         return
#
#     done = 0
#     curr_row = 1
#     let = letter.upper()
#     if let.isalpha():
#         for row in labels:
#             for col in row:
#                 if col.cget("text") == ' ' and done == 0 and guess_num[0] == curr_row:
#                     col.config(text=let, fg='black')
#                     done += 1
#             curr_row += 1
#
#
# def create_labels(root):
#     """
#     Create the frame for the color labels and feedback.
#     The color labels are used to show what colors the user
#     has guessed for the current round of mastermind.
#     The feedback variables shall be used to show the result of
#     black or white when the user enters a guess.
#     :param root: The root window.
#     :return: list of lists of labels.
#     """
#     label_frame = ttk.Frame(root, padding="3 3 3 3")
#     label_frame.grid(row=1, column=2)
#     labels = []
#     for row in range(1, 7):
#         label_row = []
#         for col in range(1, 6):
#             label = Label(label_frame, font='Courier 50 bold', text=' ',
#                           borderwidth=3, relief='solid', background='white')
#             label.grid(row=row, column=col, padx=2, pady=2)
#             label_row.append(label)
#         labels.append(label_row)
#     return labels
#
#
# def create_control_buttons(root, labels, board, guess_num):
#     bottom_frame = ttk.Frame(root)
#     bottom_frame.grid(row=3, column=1, columnspan=3)
#     # To give the user information on errors and inform them when they win.
#     info_var = StringVar()
#
#     new_game_button = Button(bottom_frame, font='Osaka 16 bold', text='New Game', command=lambda: reset_game(labels,
#                                                                                                              board,
#                                                                                                              guess_num,
#                                                                                                              info_var))
#     new_game_button.grid(row=1, column=1, padx=5, pady=5)
#
#     undo_button = Button(bottom_frame, font='Osaka 16 bold',
#                          text='Undo Guess',
#                          command=lambda: undo_last_pick(labels, guess_num, board, info_var))
#     undo_button.grid(row=1, column=2, padx=5, pady=5)
#
#     enter_guess_button = Button(bottom_frame, font='Osaka 16 bold',
#                                 text='Enter Guess',
#                                 command=lambda: enter_guess(labels, board, info_var, guess_num))
#     enter_guess_button.grid(row=1, column=3, padx=5, pady=5)
#     info_var.set("Enter a 5 letter word")
#
#     give_hint_button = Button(bottom_frame, font='Osaka 16 bold',
#                               text='Make a Wish',
#                               command=lambda: give_hint(board, info_var))
#     give_hint_button.grid(row=1, column=4, padx=5, pady=5)
#
#     info_label = ttk.Label(bottom_frame, font='Osaka 18 bold', textvariable=info_var)
#     info_label.grid(row=3, column=1, columnspan=4)
#     return info_label, info_var
#
#
# def give_hint(board, info_var):
#     """
#         Provides a hint to the player by revealing a letter of the target word.
#     """
#     if board[0].cant_make_wish():
#         messagebox.showinfo("Stop", "You already made a wish!")
#         return
#
#     feedback = board[0].get_final_feedback()
#     g_only_feedback = board[0].get_g_only_feedback()
#     answer = board[0].get_target_word()
#     if len(feedback) == 0:
#         info_var.set("You should try first!")
#         return
#     index_of_hint = 0
#     for letter in g_only_feedback:   # Get the first index that user haven't solved
#         if letter == 'G':    # User already get it, don't need any hint
#             index_of_hint += 1
#         else:
#             break   # Found the first mystery letter
#     hint_letter = answer[index_of_hint]
#     hint_message = f"The NO.{index_of_hint+1} letter is {hint_letter}"
#     messagebox.showinfo("Hint from the god of Wordle", hint_message)
#     print(g_only_feedback)
#     print(index_of_hint)
#     board[0].make_a_wish()
#
#
# def enter_guess(labels, board,  info_var, guess_num):
#     """
#        If a row is filled enter the guess into the mastermind board and display
#        the feedback.
#     """
#     if board[0].get__game_over():
#         info_var.set("Game over. Please start a new game.")
#         return
#
#     cur_row = 1
#     for row in labels:
#         if row[4].cget("text") == ' ':
#             info_var.set("Must have 5 letters make guess")
#         if info_var.get() == "I don't know that word":
#             info_var.set("Enter a 5 letter word")   # Delete previous guide message after a valid input
#         if row[4].cget("text") != ' ' and cur_row == guess_num[0]:
#             guess_str = ""
#             for letter in row:
#                 guess_str += letter.cget("text")
#             if board[0].valid_word(guess_str):
#                 feedback = board[0].get_feedback(guess_str)
#                 set_colors(row, feedback)
#                 if feedback == ['G', 'G', 'G', 'G', 'G']:   # WIN
#                     won_game(cur_row, info_var)
#                     board[0].set_game_over()
#                     break
#                 if feedback != ['G', 'G', 'G', 'G', 'G'] and cur_row == 6:    # LOSS
#                     info_var.set("Game over. Secret word was " + board[0].get_target_word())
#                     board[0].set_game_over()
#                     break
#                 else:
#                     guess_num[0] += 1
#             else:
#                 info_var.set("I don't know that word")
#             break
#         cur_row += 1
#
#
# def won_game(num_guesses, info_var):
#     print("rh")
#     if num_guesses == 1:
#         info_var.set("You win. Genius!")
#     elif num_guesses == 2:
#         info_var.set("You win. Magnificent!")
#     elif num_guesses == 3:
#         info_var.set("You win. Impressive!")
#     elif num_guesses == 4:
#         info_var.set("You win. Splendid!")
#     elif num_guesses == 5:
#         info_var.set("You win. Great!")
#     elif num_guesses == 6:
#         info_var.set("You win. Phew!")
#
#
# def set_colors(row, feedback):
#     """
#     Change background color base on feedback
#     """
#     letter_num = len(row)
#     for i in range(letter_num):
#         if feedback[i] == 'G':
#             row[i].configure(bg='green')
#         if feedback[i] == 'O':
#             row[i].configure(bg='orange')
#         if feedback[i] == '-':
#             row[i].configure(bg='light gray')
#
#
# def reset_game(labels, board, guess_num, info_var):
#     for row in labels:
#         for let in row:
#             let.configure(text=' ', background="white")
#
#     board[0] = WordleBoard()
#     guess_num[0] = 1
#     info_var.set(" ")
#
#
# def undo_last_pick(labels, guess_num, board, info_var):
#     if board[0].get__game_over():
#         info_var.set("Game over. Please start a new game.")
#         return
#     current_row = guess_num[0]
#     current_labels = labels[current_row - 1]
#     for label in reversed(current_labels):   # Check from back to front
#         if label.cget("text") != ' ':
#             label.configure(text=' ')
#             break
#
#
# if __name__ == '__main__':
#     main()


























# Name: Tianqing Zou
# UTEID: tz4654
# replace <NAME> with your name and delete this line.
#
# On my honor, <Tianqing Zou>, this programming assignment is my own work
# and I have not provided this code to any other student.
#
# Explain your added feature here:
"""
I am bad at wordle and really need some hint while playing, so that's why I added a button for user to gain a hint.
The function checks if the player has already used their wish by calling the cant_make_wish method of the board object.
If the wish has been used, a message box is displayed to inform the player.
Otherwise, the function retrieves the feedback and target word from the board object.
If there is no feedback yet, a message is displayed to prompt the player to make a guess first.
The function then iterates through the feedback to find the first letter that has not been correctly
guessed yet (marked as 'G' for correct guesses). It then displays a hint message indicating the position
and the correct letter at that position in the target word. Finally, the make_a_wish method of the board object
is called to decrement the remaining wish count.
"""

"""
Grading:
-5 3.) no error message displayed if less than 5 chars
-5 4.) no error message if not in dictionary
-5 7.) doesnt show secret word if user doesnt solve puzzle
-5 8.) no reminder to start a new game
"""

import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def get_words():
    """
    Reads from two files, 'secret_words.txt' and 'other_valid_words.txt',
    to obtain a collection of secret words and all valid words respectively.
    Converts all words to uppercase, removes leading and trailing whitespace,
    and sorts the secret words alphabetically.
    Returns a tuple containing the sorted secret words and a set of all valid words.
    """
    temp_secret_words = []
    # Read and process secret words file
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()   # Sort secret words alphabetically
    secret_words = tuple(temp_secret_words)

    # Read and process other valid words file
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


class WordleBoard:
    def __init__(self):
        """
                Initializes a new WordleBoard object.
                - Initializes secret words and all words using the get_words() method.
                - Selects a random target word from the secret words.
                - Initializes feedback as an empty list.
                - Sets game_over to False and num_wish to 1.
        """
        self.__secret_words, self.__all_words = get_words()
        self.__target_word = random.choice(self.__secret_words)
        print(self.__target_word)
        self.__feedback = []
        self.__G_only_feedback = ['-', '-', '-', '-', '-']    # Will contain 'G' from all previous guesses
        self.__game_over = False
        self.__num_wish = 1

    def get_target_word(self):
        """Returns the target word the player needs to guess."""
        return self.__target_word

    def cant_make_wish(self):
        """Returns True if the player cannot get another hint False otherwise."""
        return self.__num_wish == 0

    def make_a_wish(self):
        self.__num_wish -= 1

    def set_game_over(self):
        self.__game_over = True

    def get__game_over(self):
        """Sets the game_over attribute to True, indicating the end of the game."""
        return self.__game_over

    def get_final_feedback(self):
        return self.__feedback

    def get_g_only_feedback(self):
        return self.__G_only_feedback

    def get_feedback(self, guess):
        """
               Computes and returns the feedback for a guessed word.
               - Initializes feedback as a list of dashes ('-').
               - Compares the guessed word with the target word and marks correct letters with 'G'.
               - Marks correct letters in the wrong position with 'O'.
         """
        self.__feedback = ['-', '-', '-', '-', '-']
        secret_word_copy = list(self.__target_word)
        marked_green = []   # Store the index that already marked as 'G'
        for index in range(len(guess)):
            tgt = guess[index]
            if secret_word_copy[index] == tgt:
                self.__feedback[index] = 'G'
                self.__G_only_feedback[index] = 'G'
                secret_word_copy[index] = '*'
                marked_green.append(index)
        for index in range(len(guess)):
            if index not in marked_green:
                tgt = guess[index]
                if tgt in secret_word_copy:
                    self.__feedback[index] = 'O'
                    id_of_letter = secret_word_copy.index(tgt)
                    secret_word_copy[id_of_letter] = '*'
        return self.__feedback

    def valid_word(self, guess):
        """
                Checks if a guessed word is valid (i.e., in the set of all words).
                Returns True if the word is valid, False otherwise.
        """
        if guess in self.__all_words:
            return True
        return False


def main():
    # Set the seed to make grading easier.
    # Final version turned in must have this line
    # of code. First three words with this seed
    # should be AFFIX, PROXY, APING
    random.seed(3252024)

    root = Tk()
    root.title("WORDLE")
    root.resizable(False, False)
    root.geometry('550x550')
    guess_num = [1]
    board = [WordleBoard()]
    labels = create_labels(root)
    info_label, info_var = create_control_buttons(root, labels, board, guess_num)
    root.bind('<KeyPress>', lambda event: input_letter(event.char, labels,  guess_num, board, info_var))
    root.bind('<BackSpace>', lambda event: undo_last_pick(labels, guess_num, board, info_var))
    root.bind('<Return>', lambda event: enter_guess(labels, board, info_var, guess_num))

    root.mainloop()


def input_letter(letter, labels, guess_num, board, info_var):
    """
        Handles the input of a letter by the player.
    """
    if board[0].get__game_over():
        info_var.set("Game over. Please start a new game.")
        return

    done = 0
    curr_row = 1
    let = letter.upper()
    if let.isalpha():
        for row in labels:
            for col in row:
                if col.cget("text") == ' ' and done == 0 and guess_num[0] == curr_row:
                    col.config(text=let, fg='black')
                    done += 1
            curr_row += 1


def create_labels(root):
    """
    Create the frame for the color labels and feedback.
    The color labels are used to show what colors the user
    has guessed for the current round of mastermind.
    The feedback variables shall be used to show the result of
    black or white when the user enters a guess.
    :param root: The root window.
    :return: list of lists of labels.
    """
    label_frame = ttk.Frame(root, padding="3 3 3 3")
    label_frame.grid(row=1, column=2)
    labels = []
    for row in range(1, 7):
        label_row = []
        for col in range(1, 6):
            label = Label(label_frame, font='Courier 50 bold', text=' ',
                          borderwidth=3, relief='solid', background='white')
            label.grid(row=row, column=col, padx=2, pady=2)
            label_row.append(label)
        labels.append(label_row)
    return labels


def create_control_buttons(root, labels, board, guess_num):
    bottom_frame = ttk.Frame(root)
    bottom_frame.grid(row=3, column=1, columnspan=3)
    # To give the user information on errors and inform them when they win.
    info_var = StringVar()

    new_game_button = Button(bottom_frame, font='Osaka 16 bold', text='New Game', command=lambda: reset_game(labels,
                                                                                                             board,
                                                                                                             guess_num,
                                                                                                             info_var))
    new_game_button.grid(row=1, column=1, padx=5, pady=5)

    undo_button = Button(bottom_frame, font='Osaka 16 bold',
                         text='Undo Guess',
                         command=lambda: undo_last_pick(labels, guess_num, board, info_var))
    undo_button.grid(row=1, column=2, padx=5, pady=5)

    enter_guess_button = Button(bottom_frame, font='Osaka 16 bold',
                                text='Enter Guess',
                                command=lambda: enter_guess(labels, board, info_var, guess_num))
    enter_guess_button.grid(row=1, column=3, padx=5, pady=5)
    info_var.set("Enter a 5 letter word")

    give_hint_button = Button(bottom_frame, font='Osaka 16 bold',
                              text='Make a Wish',
                              command=lambda: give_hint(board, info_var))
    give_hint_button.grid(row=1, column=4, padx=5, pady=5)

    info_label = ttk.Label(bottom_frame, font='Osaka 18 bold', textvariable=info_var)
    info_label.grid(row=3, column=1, columnspan=4)
    return info_label, info_var


def give_hint(board, info_var):
    """
        Provides a hint to the player by revealing a letter of the target word.
    """
    if board[0].cant_make_wish():
        messagebox.showinfo("Stop", "You already made a wish!")
        return

    feedback = board[0].get_final_feedback()
    g_only_feedback = board[0].get_g_only_feedback()
    answer = board[0].get_target_word()
    if len(feedback) == 0:
        info_var.set("You should try first!")
        return
    index_of_hint = 0
    for letter in g_only_feedback:   # Get the first index that user haven't solved
        if letter == 'G':    # User already get it, don't need any hint
            index_of_hint += 1
        else:
            break   # Found the first mystery letter
    hint_letter = answer[index_of_hint]
    hint_message = f"The NO.{index_of_hint+1} letter is {hint_letter}"
    messagebox.showinfo("Hint from the god of Wordle", hint_message)
    print(g_only_feedback)
    print(index_of_hint)
    board[0].make_a_wish()


def enter_guess(labels, board,  info_var, guess_num):
    """
       If a row is filled enter the guess into the mastermind board and display
       the feedback.
    """
    if board[0].get__game_over():
        info_var.set("Game over. Please start a new game.")
        return

    cur_row = 1
    for row in labels:
        if row[4].cget("text") == ' ':
            info_var.set("Must have 5 letters make guess")
        if info_var.get() == "I don't know that word":
            info_var.set("Enter a 5 letter word")   # Delete previous guide message after a valid input
        if row[4].cget("text") != ' ' and cur_row == guess_num[0]:
            guess_str = ""
            for letter in row:
                guess_str += letter.cget("text")
            if board[0].valid_word(guess_str):
                feedback = board[0].get_feedback(guess_str)
                set_colors(row, feedback)
                if feedback == ['G', 'G', 'G', 'G', 'G']:   # WIN
                    won_game(cur_row, info_var)
                    board[0].set_game_over()
                    break
                if feedback != ['G', 'G', 'G', 'G', 'G'] and cur_row == 6:    # LOSS
                    info_var.set("Game over. Secret word was " + board[0].get_target_word())
                    board[0].set_game_over()
                    break
                else:
                    guess_num[0] += 1
            else:
                info_var.set("I don't know that word")
            break
        cur_row += 1


def won_game(num_guesses, info_var):
    print("rh")
    if num_guesses == 1:
        info_var.set("You win. Genius!")
    elif num_guesses == 2:
        info_var.set("You win. Magnificent!")
    elif num_guesses == 3:
        info_var.set("You win. Impressive!")
    elif num_guesses == 4:
        info_var.set("You win. Splendid!")
    elif num_guesses == 5:
        info_var.set("You win. Great!")
    elif num_guesses == 6:
        info_var.set("You win. Phew!")


def set_colors(row, feedback):
    """
    Change background color base on feedback
    """
    letter_num = len(row)
    for i in range(letter_num):
        if feedback[i] == 'G':
            row[i].configure(bg='green')
        if feedback[i] == 'O':
            row[i].configure(bg='orange')
        if feedback[i] == '-':
            row[i].configure(bg='light gray')


def reset_game(labels, board, guess_num, info_var):
    for row in labels:
        for let in row:
            let.configure(text=' ', background="white")

    board[0] = WordleBoard()
    guess_num[0] = 1
    info_var.set(" ")


def undo_last_pick(labels, guess_num, board, info_var):
    if board[0].get__game_over():
        info_var.set("Game over. Please start a new game.")
        return
    current_row = guess_num[0]
    current_labels = labels[current_row - 1]
    for label in reversed(current_labels):   # Check from back to front
        if label.cget("text") != ' ':
            label.configure(text=' ')
            break


if __name__ == '__main__':
    main()
