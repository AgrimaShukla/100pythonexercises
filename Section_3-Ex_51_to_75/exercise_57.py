# JSON to Dictionary

import json
from pprint import pprint
with open("company1.json", 'r') as file:
    txt = json.load(file)
    
pprint(txt)