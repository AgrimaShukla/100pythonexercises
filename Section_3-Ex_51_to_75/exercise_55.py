# Adding to Multilevel Dictionaries

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
      "owners": [{"firstName": "Jack", "lastName": "Peter"},
                 {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"].append({"firstName": "Albert", "lastName": "Bert"})
print(d)