# Advanced Translator

d = dict(weather = "clima", earth = "terra", rain = "chuva")
str = input("Enter word: ")
for key, value in d.items():
    if key == str:
        print(value)
        break
else:
    print("That word dosen't exist")

'''
def voc(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter word: ")
print(voc(word))
'''