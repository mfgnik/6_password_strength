import sys


def count_upper_letters(password):
    amount_of_upper_letters = 0
    upper_letters = set(chr(index) for index in range(65, 91)) | set(chr(index) for index in range(1040, 1072)) | {'Ё'}
    for letter in password:
        if letter in upper_letters:
            amount_of_upper_letters += 1
    return amount_of_upper_letters


def count_lower_letters(password):
    amount_of_lower_letters = 0
    lower_letters = set(chr(index) for index in range(97, 123)) | set(chr(index) for index in range(1072, 1104)) | {'ё'}
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
    symbols = set(chr(index) for index in range(33, 48)) | set(chr(index) for index in range(58, 65))
    for letter in password:
        if letter in symbols:
            amount_of_symbols += 1
    return amount_of_symbols


def count_repeats_of_letters(password):
    sum_of_repeats = 0
    max_repeat = 0
    repeat_now = 0
    number_of_letter = 0
    while number_of_letter < len(password) - 1:
        if password[number_of_letter] == password[number_of_letter + 1]:
            repeat_now = 1
            while number_of_letter < len(password) - 1 and password[number_of_letter] == password[number_of_letter + 1]:
                repeat_now += 1
                number_of_letter += 1
            sum_of_repeats += repeat_now
            if max_repeat < repeat_now:
                max_repeat = repeat_now
        number_of_letter += 1
    return sum_of_repeats * 2 + max_repeat * 3


def additions(password):
    number_of_characters = len(password) * 4
    upper_letters = (len(password) - count_upper_letters(password)) * 2
    lower_letter =  (len(password) - count_lower_letters(password)) * 2
    numbers = count_numbers(password) * 4
    symbols = count_symbols(password) * 6
    requirements = (len(password) >= 8 and upper_letters > 0 and lower_letter > 0 and numbers > 0 and symbols > 0) * 10
    return number_of_characters + upper_letters + numbers + symbols + requirements


def deductions(password):
    numbers_only = (password.isdigit()) * len(password) * 10
    upper_only = (password.isupper() and password.isalpha()) * len(password) * 6
    lower_only = (password.islower() and password.isalpha()) * len(password) * 6
    letters_only = (password.isalpha()) * len(password) * 2
    only_criteria = numbers_only + upper_only + lower_only + letters_only
    not_numbers = (not count_numbers(password)) * 9
    not_upper = (not count_upper_letters(password)) * 7
    not_lower = (not count_lower_letters(password)) * 7
    not_symbols = (not count_symbols(password)) * 5
    not_criteria = not_numbers + not_upper + not_lower + not_symbols
    repeats_of_letters = count_repeats_of_letters(password)
    return only_criteria + not_criteria + repeats_of_letters


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
