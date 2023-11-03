import requests

response = requests.get("https://pythonhow.com/media/data/universe.txt")

text = response.text
print(text)