import pandas as pd

data = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = pd.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")
print(pd.concat([data, data2]))
data3 = pd.concat([data, data2])
data3.to_csv("sample3.csv")