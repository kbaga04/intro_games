import random
import string

Special_Characters = ['@', '%', '+', '-', '/', '\ ', '!',
                      "'", '$', '^', '?', ';', ':', ',', ')', '(', '*']

randomStuff = random.choice(string.ascii_lowercase)
randStuff = random.choice(string.ascii_uppercase)
rand = random.choice(string.digits)
ra = random.choice(string.punctuation)
print(randomStuff)
print(randStuff)
print(rand)
print(ra)


def pass_gen():
    password = ''
    how_str_digits = 0
    how_str_low = random.randint(3, 5)
    how_str_high = random.randint(3, 5)
    how_str_special_chars = random.randint(1, 3)
    how_str_digits = 15 - (how_str_low + how_str_high + how_str_digits)

    for i in range(how_str_low):
        password += random.choice(string.ascii_lowercase)
    for x in range(how_str_high):
        password += random.choice(string.ascii_uppercase)
    y = 0
    while y < how_str_special_chars:
        char = random.choice(string.punctuation)
        if not (char == '<' or char == '>'):
            password += char
        else:
            y -= 1
        y += 1
    for k in range(how_str_digits):
        password += random.choice(string.digits)

    l = list(password)
    random.shuffle(l)
    password = ''.join(l)

    return password


print(pass_gen())
