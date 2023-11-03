# File Writer
i = 0
lst = []
while i < 5:
    inp = input("Enter: ")
    lst.append(inp)
    i += 1

with open("file_writer", 'w') as file:
    for ele in lst:
        file.write(ele + "\n")


# file = open("user_data1.txt", "a+")

# while True:
#     line = input("Write a value: ")
#     if line == "CLOSE":
#         file.close()
#         break
#     else:
#         file.write(line + "\n")