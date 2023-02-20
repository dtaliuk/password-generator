from string import digits as dig, ascii_lowercase as low, ascii_uppercase as up
from random import sample

symbols = [symb for symb in low + up + dig if symb not in ' lI1oO0']


def generate_password(length):
    while True:
        res = sample(symbols, length)
        if all([any([i in low for i in res]),
                any([j in up for j in res]),
                any([k in dig for k in res])]):
            return ''.join(res)


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


generate_passwords(int(input()), int(input()))
