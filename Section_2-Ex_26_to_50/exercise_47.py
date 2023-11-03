# Conditioned Letter Extractor
import glob
file_list = glob.iglob("letters/*.txt")
str = "python"
lst = []
for name in file_list:
    with open(name, "r") as file:
        txt = file.read().strip("\n")
    if txt in str:
        lst.append(txt)

print(lst)