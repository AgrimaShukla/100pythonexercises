# Data cleaner

with open('countries_raw.txt', 'r')as file:
    data = file.readlines()

data = [i.strip("\n") for i in data if "\n" in i]
data = [i for i in data if i != "Top of Page"]
data = [i for i in data if len(i) != 1]
data = [i for i in data if i != ""]
with open('countries_raw_new.txt', 'w') as file:
    for i in data:
        file.write(i+"\n")