# Letter Extractor


import string
lst = []
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "r") as file:
        new_lst = file.read()
        list.append(new_lst)
        njedmn