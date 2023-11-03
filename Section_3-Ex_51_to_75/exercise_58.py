# Add to JSON

import json
with open('company1.json', 'r+') as file:
    text = json.loads(file.read())
    text["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
    file.seek(0)
    json.dump(text, file, indent = 4)
    