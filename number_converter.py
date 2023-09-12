from most_used_functions import is_valid
from typing import Union

def number_converter(sys1: str, sys2: str, num: str) -> Union[int, str]:
    """
    :type num: str
    :type sys1: str
    :type sys2: str
    """
    if sys1 == sys2:
        return num
    dict_of_hex_numbers = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
    }
    num = list(num)
    if sys1 == 'hexadecimal':
        for i in range(len(num)):
            if num[i] in dict_of_hex_numbers.keys():
                num[i] = dict_of_hex_numbers[num[i]]
        base = 16
    elif sys1 == 'decimal':
        num = int(''.join(num))
    elif sys1 == 'octal':
        base = 8
    elif sys1 == 'binary':
        base = 2

    if type(num) != int:
        num = num[::-1]
        decimal_num = [int(e)*base**i for i,e in enumerate(num)]
        decimal_num = sum(decimal_num)
        if sys2 == 'decimal':
            return decimal_num
    else:
        decimal_num = int(num)
    if sys2 == 'hexadecimal':
        return hex(decimal_num)[2:].upper()
    elif sys2 == 'octal':
        return oct(decimal_num)[2:]
    elif sys2 == 'binary':
        return bin(decimal_num)[2:]


print('Hello! This program purpose is to convert numbers from one numerical system to another \n' +
      'It supports systems like binary, octal, hexadecimal, and decimal.')

system1 = input('Please, enter initial system: ')

number = input(f'Please, enter a number of {system1} system to transform: ')

system2 = input('Please, enter final system: ')

print(number_converter(system1, system2, number))

