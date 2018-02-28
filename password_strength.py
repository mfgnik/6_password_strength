import sys
import re


def count_upper_letters(password):
    amount_of_upper_letters = 0
    eng_upper_letters = set(chr(index) for index in range(65, 91))
    rus_upper_letters = set(chr(index) for index in range(1040, 1072)) | {'Ё'}
    upper_letters = eng_upper_letters | rus_upper_letters
    for letter in password:
        if letter in upper_letters:
            amount_of_upper_letters += 1
    return amount_of_upper_letters


def count_lower_letters(password):
    amount_of_lower_letters = 0
    eng_lower_letters = set(chr(index) for index in range(97, 123))
    rus_lower_letters = set(chr(index) for index in range(1072, 1104)) | {'ё'}
    lower_letters = eng_lower_letters | rus_lower_letters
    for letter in password:
        if letter in lower_letters:
            amount_of_lower_letters += 1
    return amount_of_lower_letters


def count_numbers(password):
    amount_of_numbers = 0
    numbers = set(chr(index) for index in range(48, 58))
    for letter in password:
        if letter in numbers:
            amount_of_numbers += 1
    return amount_of_numbers


def count_symbols(password):
    amount_of_symbols = 0
    first_group_of_symbols = set(chr(index) for index in range(33, 48))
    second_group_of_symbols = set(chr(index) for index in range(58, 65))
    symbols = first_group_of_symbols | second_group_of_symbols
    for letter in password:
        if letter in symbols:
            amount_of_symbols += 1
    return amount_of_symbols


def count_repeats_of_letters(password):
    sum_of_repeats = 0
    max_repeat = 0
    for repeat in re.finditer(r'(.)\1+', password):
        start, end = repeat.span()
        length_of_repeat = end - start
        sum_of_repeats += length_of_repeat
        if length_of_repeat > max_repeat:
            max_repeat = length_of_repeat
    return sum_of_repeats * 2 + max_repeat * 3


def additions(password):
    number_of_characters = len(password) * 4
    upper_letters = (len(password) - count_upper_letters(password)) * 2
    lower_letters = (len(password) - count_lower_letters(password)) * 2
    numbers = count_numbers(password) * 4
    symbols = count_symbols(password) * 6
    type_criteria = upper_letters + lower_letters + numbers + symbols
    all_types = upper_letters * lower_letters * numbers * symbols > 0
    requirements = (number_of_characters >= 8 and all_types) * 10
    return number_of_characters + type_criteria + requirements


def deductions(password):
    numbers_only = (password.isdigit())
    upper_only = (password.isupper() and password.isalpha())
    lower_only = (password.islower() and password.isalpha())
    only_criteria = numbers_only * 10 + (upper_only + lower_only) * 7
    not_numbers = (not count_numbers(password)) * 9
    not_upper = (not count_upper_letters(password)) * 7
    not_lower = (not count_lower_letters(password)) * 7
    not_symbols = (not count_symbols(password)) * 5
    not_criteria = not_numbers + not_upper + not_lower + not_symbols
    repeats_of_letters = count_repeats_of_letters(password)
    return only_criteria * len(password) + not_criteria + repeats_of_letters


def get_password_strength(password):
    criteria = additions(password) - deductions(password)
    if criteria < 20:
        return 1
    if criteria > 99:
        return 10
    else:
        return criteria // 10


if __name__ == '__main__':
    password = sys.argv[1]
    print(get_password_strength(password))
