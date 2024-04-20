# Name: Tianqing Zou
# UTEID: tz4654
#
# On my honor, <Tianqing Zou>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random


def main():
    """ Plays a text based version of Wordle.
        1. Read in the words that can be choices for the secret word
        and all the valid words. The secret words are a subset of
        the valid words.
        2. Explain the rules to the player.
        3. Get the random seed from the player if they want one.
        4. Play rounds until the player wants to quit.
    """
    secret_words, all_words = get_words()
    welcome_and_instructions()
    continue_playing = True
    while continue_playing:
        guesses = 6
        secret_word = get_secret_word(secret_words)
        output = ''
        feedback = ''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while guesses > 0 and feedback != 'GGGGG':

            # print('!!!SECRET word is: ' + secret_word)

            result_tuple = play_round(secret_word, all_words, alphabet)
            output += result_tuple[0]
            feedback = result_tuple[1]
            print('\n' + output)
            guesses -= 1
            alphabet = result_tuple[2]
            print('Unused letters:' + alphabet)
        if feedback == 'GGGGG' and guesses == 0:
            print('\nYou win. Phew!')
        elif feedback == 'GGGGG' and guesses == 1:
            print('\nYou win. Great!')
        elif feedback == 'GGGGG' and guesses == 2:
            print('\nYou win. Splendid!')
        elif feedback == 'GGGGG' and guesses == 3:
            print('\nYou win. Impressive!')
        elif feedback == 'GGGGG' and guesses == 4:
            print('\nYou win. Magnificent!')
        elif feedback == 'GGGGG':
            print('\nYou win. Genius!')
        else:
            print('\nNot quite. The secret word was ' + secret_word + '.')
        continue_playing = input('\nDo you want to play again? Type Y for yes: ').upper() == 'Y'


def welcome_and_instructions():
    """
    Print the instructions and set the initial seed for the random
    number generator based on user input.
    """
    print('Welcome to Wordle.')
    instructions = input('\nEnter y for instructions, anything else to skip: ')
    if instructions == 'y':
        print('\nYou have 6 chances to guess the secret 5 letter word.')
        print('Enter a valid 5 letter word.')
        print('Feedback is given for each letter.')
        print('G indicates the letter is in the word and in the correct spot.')
        print('O indicates the letter is in the word but not that spot.')
        print('- indicates the letter is not in the word.')
    set_seed = input(
        '\nEnter y to set the random seed, anything else to skip: ')
    if set_seed == 'y':
        random.seed(int(input('\nEnter number for initial seed: ')))


def get_words():
    """ Read the words from the dictionary files.
        We assume the two required files are in the current working directory.
        The file with the words that may be picked as the secret words is
        assumed to be names secret_words.txt. The file with the rest of the
        words that are valid user input but will not be picked as the secret
        word are assumed to be in a file named other_valid_words.txt.
        Returns a sorted tuple with the words that can be
        chosen as the secret word and a set with ALL the words,
        including both the ones that can be chosen as the secret word
        combined with other words that are valid user guesses.
    """
    temp_secret_words = []
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()
    secret_words = tuple(temp_secret_words)
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


def get_secret_word(secret_words):
    """ return a random secret word form word tuple
    """
    return random.choice(secret_words)


def play_round(secret_word, all_words, alphabet):
    invalid = True
    guess = ''
    while invalid:
        guess = input('\nEnter your guess. A 5 letter word: ').upper()
        if check_valid_guess(guess, all_words):
            invalid = False
        else:
            print('\n' + guess + ' is not a valid word. Please try again.')

    feedback = get_feedback(secret_word.upper(), guess)
    output = feedback + '\n' + guess + '\n'
    alphabet = update_alphabet(guess, alphabet)
    return output, feedback, alphabet


def get_feedback(secret_word, guess):
    feedback = ['-', '-', '-', '-', '-']
    secret_word_copy = list(secret_word)
    marked_green = []

    for index in range(len(guess)):
        tgt = guess[index]
        if secret_word_copy[index] == tgt:
            feedback[index] = 'G'
            secret_word_copy[index] = '*'
            marked_green.append(index)
    for index in range(len(guess)):
        if index not in marked_green:
            tgt = guess[index]
            if tgt in secret_word_copy:
                feedback[index] = 'O'
                id_of_letter = secret_word_copy.index(tgt)
                secret_word_copy[id_of_letter] = '*'
    return ''.join(feedback)


def check_valid_guess(guess, all_words):
    if len(guess) != 5:
        return False
    if not guess.isalpha():
        return False
    if guess in all_words:
        return True
    return False

def update_alphabet(guess_word, alphabet):
    result = ''
    alphabet = alphabet.replace(' ', '')
    for letter in alphabet:
        if letter not in guess_word:
            result += ' ' + letter
    return result

if __name__ == '__main__':
    main()
