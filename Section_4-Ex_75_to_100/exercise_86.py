# Data Checker

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_raw_new.txt", 'r') as file:
     text = file.readlines()
     

content = [txt.strip() for txt in text]
name = [i for i in checklist if i in content]

print(name)