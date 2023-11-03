# Translator

str = input("Enter word: ")
d = dict(weather = "clima", earth = "terra", rain = "chuva")

for key, value in d.items():
    if key == str:
        print(value)