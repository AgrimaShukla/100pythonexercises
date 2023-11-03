# Word Counter

def func(file_name):
    with open(file_name, 'r') as file:
        file = file.read()
        txt = file.split(" ")
        return len(txt)
    
print(func('word.txt'))