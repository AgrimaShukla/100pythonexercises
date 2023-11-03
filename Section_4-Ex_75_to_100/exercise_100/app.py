from flask import Flask, request, render_template

app = Flask(__name__)

import re

# lsts = []
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


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
      username = request.form.get('username')
      with open("new1.txt", "a+") as file:
         file.seek(0)
         val = file.readlines()
         for item in val:
            if username == item.strip('\n'):
               return render_template("base.html", PROMPT = "Enter another username")
         password = request.form.get('password')
         if pw_number(password) and pw_upper(password) and pw_length(password):
            file.writelines(username)    
         else:
            return 
      with open("pass.txt", "a+") as file:
         file.writelines(password)
    return render_template('base.html')
    


if __name__ == "__main__":
    app.run()