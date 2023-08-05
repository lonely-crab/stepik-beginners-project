import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

yes, no = 'y', 'n'
chars = ''


def is_valid(num: str) -> bool:
    for element in num:
        if not element.isdigit():
            return False
    if 1 <= int(num) <= 100:
        return True
    else:
        return False


def generate_password(ch: str, leng: int) -> str:
    password = ''
    for _ in range(leng):
        password += random.choice(ch)
    return password


greeting = input('Hello it\' a safe password generator! Do you want to create a safe password? (y/n) ')

if yes == greeting.lower():
    flag = True #flag for cycle not to break until allowed
    while flag:
        n = input('How many passwords do you want to generate? ')
        if not is_valid(n):
            print('Your number format is incorrect, please, try again.')
        else:
            length = input('How long should it be? ')
            while not is_valid(length):
                length = input('Your length input is incorrect, please, try again. \n How long should it be? ')
            if input(f'Should it contain digits? ({digits}) ') == yes:
                chars += digits
            if input(f'Should it contain lowercase letters? ({lowercase_letters}) ') == yes:
                chars += lowercase_letters
            if input(f'Should it contain uppercase letters? ({uppercase_letters}) ') == yes:
                chars += uppercase_letters
            if input(f'Should it contain punctuation? ({punctuation}) ') == yes:
                chars += punctuation

            print('List of your safe passwords: ')
            for _ in range(int(n)):
                print(generate_password(chars, int(length)))
            if input('Do you want to create another safe password? (y/n) ') == no:
                flag = False
                print('Thanks for using safe password generator! ' +
                      'Come back whenever you want to generate another safe password!')
