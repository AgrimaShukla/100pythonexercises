# Advanced File Writer

file = open("file_writer1.txt", "a+")
lst = []
while True:
    inp = input("Enter something: ")
    # lst.append(inp)
    if inp == 'SAVE':
        # lst.remove('SAVE')
        for ele in lst:
            file.write(ele + "\n")
        file.close()
        file = open("file_writer.txt", "a+")
    elif inp == "CLOSE":
        file.close()
        break
    else:
        lst.append(inp)

# while True:
#     line = input("Write something: ")
#     if line == 'SAVE':
#         file.close()
#         file = open("file_writer1.txt", "a+")
#     elif line == 'CLOSE':
#         file.close()
#         break
#     else:
#         file.write(line + "\n")  