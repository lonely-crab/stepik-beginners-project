import random
from most_used_functions import is_valid


"""Generation of a random number"""
random_number = random.randrange(1, 101)
print("Welcome to number guesser! Please, input your guess:", end='')


"""counter of attempts"""
counter = 0


"""cycle for input"""
while True:
    x = input()
    if not is_valid(x):
        print('Your guess format is incorrect, please, try again.')
        continue
    else:
        if int(x) == random_number:
            print('You are right, great job!')
            print(f'The number of attempts: {counter+1}')
            break
        elif int(x) < random_number:
            print('Your number is too small, please, try again!')
            counter += 1
        else:
            print('Your number is too big, please, try again!')
            counter += 1
