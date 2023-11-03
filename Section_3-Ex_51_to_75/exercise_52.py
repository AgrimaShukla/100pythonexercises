# String Formatting

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
# Aprint("Your first name is %s and your second name is %s" % firstname,  secondname) # TypeError - not enough arguments for format string
print("Your first name is %s and your second name is %s" % (firstname,  secondname))