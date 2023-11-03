# Data Plotter

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
lst_x = []
lst_y = []
for index, rows in data.iterrows():
    lst_x.append(rows["x"])
    lst_y.append(rows["y"])

plt.plot(lst_x, lst_y)
plt.show()