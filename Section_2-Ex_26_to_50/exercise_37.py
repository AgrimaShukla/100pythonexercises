# Advanced Word Counter

def func(file_name):
    with open(file_name, 'r') as file:
        txt = file.read()
        new_txt = txt.replace(",", " ")
        new_txt = new_txt.split(" ")
        return len(new_txt)

print(func('words2.txt'))