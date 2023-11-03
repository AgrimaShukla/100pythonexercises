# User friendly Translator

d = dict(weather = "clima", earth = "terra", rain = "chuva")

str =  input("Enter word: ")
for key, value in d.items():
     if str.lower() == key:
          print(value)
          break
else:
     print("We couldn't find the word!")