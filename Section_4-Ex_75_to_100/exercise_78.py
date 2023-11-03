# Random password generator

import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
data = random.sample(characters, 10)
password = "".join(data)
print(password)