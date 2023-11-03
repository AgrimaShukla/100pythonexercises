# Letters Two by Two

import string
with open('data.txt', 'w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        file.write(letter1 + letter2 + "\n")