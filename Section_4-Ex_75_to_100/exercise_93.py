# Recursive File Counter
import glob

lst = glob.glob("subdirs/**/*.py", recursive = True)
print(len(lst))
