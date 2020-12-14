import random

def guess_word():
    list_of_words = ["starwards", "someone", "powerrangers", "marabu", "mypython", "wordinthelist", "neversurrender"]
    random_word = random.choice(list_of_words)
    return random_word

def hangman_game():
    alphabet = 'abcdefghijklmnoprstuvwxyqz'
    word = guess_word()
    lifes = 5
    guesses = []
    print('The word contains {} letters'.format(len(word)))
    game_over = False
    while game_over == False and lifes > 0:
        print('-' * 25)
        print('You have {} tries'.format(lifes))
        print('-' * 25)
        user_word = input('Introduce one letter or entire word: ').lower()
        print('-' * 25)
        if len(user_word) == 1:
            if user_word not in alphabet:
                print('Your input is not correct, must to be alphabetic!')

            elif user_word in guesses:
                print('You have already introduced that letter')

            elif user_word not in word:
                print('Was not the right guess!')
                guesses.append(user_word)
                lifes -= 1

            elif user_word in word:
                print('You got it!')
                guesses.append(user_word)

            else:
                print('Try again...')

        elif len(user_word) == len(word):
            if user_word == word:
                print('Your guessed was ok!')
                game_over = True
            else:
                print('Your guessed was not ok!')
                lifes -= 1

        else:
            print('Your length of input is not ok')

        strcuture_of_word = ''
        for letter in word:
            if letter in guesses:
                strcuture_of_word += letter
            else:
                strcuture_of_word += '_'
        print(strcuture_of_word)

        if strcuture_of_word == word:
            print('Congrat! You won the game!')
            game_over = True
            try_again()
        elif lifes == 0:
            print('You lost the game!!!!!')
            game_over = True
            try_again()


def try_again():
    user_choose = input('Do you want to play again? y/n: ')
    print('-' * 25)
    if user_choose == 'y':
        hangman_game()
    else:
        print('Have a nice day!')
        quit()

if __name__ == '__main__':
    hangman_game()
