# Advanced password

import re
def pw_number(password):
   regex_exp = '[0-9]+'
   matcher = re.search(regex_exp, password)
   if matcher is not None:
      return True
   else:
      print("Password does not contain number")
      return False
   
def pw_upper(password):
   regex_exp = '[A-Z]+'
   matcher = re.search(regex_exp, password)
   if matcher is not None:
      return True
   else:
      print("Password does not contain uppercase")
      return False
   
def pw_length(password):
   if len(password) >= 5:
      return True
   else:
      print("Password length small")
      return False
   
password = input("Enter password: ")

if pw_number(password) and pw_upper(password) and pw_length(password):
   print("Fine")

else:
   print("Not fine")