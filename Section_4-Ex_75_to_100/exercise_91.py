import sqlite3
import pandas as pd
lst = []

with open("ten_more_countries.txt", 'r') as file:
    txt = file.readlines()

with open("ten_more_countries", 'a') as file:
    for i in txt:
        lst.append(i.strip())

lst = lst[1:]
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
for i in lst:
    new_lst = i.split(',')
    print(new_lst)
    # cursor.execute("INSERT INTO COUNTRIES VALUES (?, ?, ?, NULL)", (new_lst[0], new_lst[1], new_lst[2]) )

connection.commit()


# using pandas
# data = pd.read_csv("ten_more_countries.txt")

# conn = sqlite3.connect('database.db')
# cursor = cursor.connection
# for index, row in data.iterrows(): #iterrows() generates an iterator object of the DataFrame, allowing us to iterate each row in the DataFrame
#     print(row["Country"], row["Area"])
#     cursor.execute("INSERT INTO countries VALUES (NULL, ?, ?, NULL)", (row['Country'], row['Area']))

# connection.commit()
# connection.close()