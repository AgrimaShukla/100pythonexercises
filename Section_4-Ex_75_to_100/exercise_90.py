# Databse to CSV Converter

import sqlite3
#import pandas as pd
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("SELECT * from countries WHERE area >= ?", (2000000,))
rows = cursor.fetchall()
print(rows)
connection.close()

# df = pd.DataFrame.from_records(rows) # dataframe from list of data like list of dict or list of tuple
# df.columns = ["Rank", "Country", "Area", "Population"]
# df.to_csv("countries_mew.csv", index = False)