"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(length):
    # TODO : complete this
    my_length = length
    if length < 12:
        my_length = 12

    password = [LOWER_LETTERS[random.randint(0, 25)], UPPER_LETTERS[random.randint(0, 25)],
                NUMBERS[random.randint(0, 9)], SPECIAL[random.randint(0, 12)]]

    while len(password) < my_length:
        password.append(ALL_CHARS[random.randint(0,74)])

    random.shuffle(password)
    return ''.join(password)