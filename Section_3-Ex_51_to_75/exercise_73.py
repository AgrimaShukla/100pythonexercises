# Data Multiplier

import pandas as pd

data = pd.read_csv("ex.txt")
print(data)

data_new = data * 2
data_new.to_csv("sample_new.csv")
print(data_new)
