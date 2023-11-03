import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
txt = response.text
count = txt.count('a')
print(count)