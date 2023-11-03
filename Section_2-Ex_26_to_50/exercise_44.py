# Ltters Three by Three

import string
with open("data.txt", "w") as file:
    for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[3::3]):
        file.write(letter1 + letter2 + letter3 + "\n")