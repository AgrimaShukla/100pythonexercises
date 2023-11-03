# Password checker
import re

def pw_number(password):
   regex_exp = '[0-9]+'
   matcher = re.search(regex_exp, password)
   if matcher is not None:
      return True
   else:
      return False
   
def pw_upper(password):
   regex_exp = '[A-Z]+'
   matcher = re.search(regex_exp, password)
   if matcher is not None:
      return True
   else:
      return False
   

password = input("Enter password: ")
if pw_number(password) and pw_upper(password) and len(password) >= 5:
   print("Fine")

else:
   print("Not fine")