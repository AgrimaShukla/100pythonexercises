# Add missing data

checklist = ["Portugal", "Germany", "Spain"]
with open('countries_raw_new.txt', 'r') as file:
    text = file.readlines()

#content = [i.strip for i in text]
name = [i + "\n" for i in checklist]
new_name = sorted(name + text)

with open('countries_raw_new.txt', 'w') as file:
    for i in new_name:
        file.write(i)