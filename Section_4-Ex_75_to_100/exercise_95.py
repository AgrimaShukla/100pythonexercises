# Comma Separated Input

user_input = input("Enter something: ")
lst = []
user_input = user_input.split(',')
for ele in user_input:
    lst.append(ele)

print(lst)
with open("comma.txt", 'w') as file:
    for ele in lst:
        file.write(ele + "\n")