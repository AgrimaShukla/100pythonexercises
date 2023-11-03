# Enumerator

a = [1, 2, 3]
index = enumerate(a)
index = list(index)

for i, j in index:
    print(f"Item {j} has index {i}")
