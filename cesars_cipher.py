def coder_decoder(s: str, lang: str, step: int) -> str:
    new_str = ''
    if lang.lower() in 'russianрусский':
        ord_upper = 1040
        ord_lower = 1072
        power = 32
    else:
        ord_upper = 65
        ord_lower = 97
        power = 26
    for e in s:
        if not e.isalpha():
            new_str += e
            continue
        else:
            if e.isupper():
                new_str += chr(ord_upper + (ord(e) - ord_upper + step) % power)
            else:
                new_str += chr(ord_lower + (ord(e) - ord_lower + step) % power)
    return new_str


def is_valid(num: str) -> bool:
    for element in num:
        if not element.isdigit():
            return False
    if 1 <= int(num) <= 100:
        return True
    else:
        return False


print('Hello! This program purpose is to code or decode with Cesar\'s cipher.')

process = input('Do you want to code or to decode your sentence? (code/decode) ').lower()
while process not in ['code', 'decode']:
    print('Your input is incorrect, please, try again.')
    process = input('Do you want to code or to decode your sentence? (code/decode) ').lower()
else:
    string = input('Please, enter your text to process: ')
    language = input('Please, enter your text language: ')
    cipher_step = input('Please, enter cipher step: ')
    while not is_valid(cipher_step):
        print('Your cipher step input is incorrect. Please, enter a valid number')
        cipher_step = input('Please, enter cipher step: ')
if process == 'code':
    cipher_step = int(cipher_step)
else:
    cipher_step = -int(cipher_step)
