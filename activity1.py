from random import choice
word = choice(('apple', 'oracle', 'amazon'))
clue = word[0] + word[::-1][0]
word_guess = ''
store_letter = ''
count = 0
limit = 5
print('select from the following 1.apple 2.oracle 3.amazon')
print('Welcome to "Guess the Word Game!')
print('You have 5 attempts at guessing letters in a word')
print("Let's begin!")
print('\n')
while count < limit:
    letter_guess = input('Guess a letter: ')
    count += 1
    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
    else:
        print('no!')
    if count == 2:
        print('\n')
        clue_request = input('Would you like a clue? [y / n] ')
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        elif clue_request == 'n':
            # Changed to elif
            print("You're very brave!")
print('\n')
print('You have guessed', len(store_letter), 'letters correctly.')
print('These letters are: ', store_letter)
word_guess = input('Guess the whole word: ')
if word_guess.lower() == word:
    print('Congrats!')
else:
    # You don't have to write out a whole
    # elif condition, just use else-
    print('Unlucky! The answer was,', word)
print('\n')
input('Press Enter to leave the program ')
