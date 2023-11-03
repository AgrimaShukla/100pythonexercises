# Year of Birth Calculator

from datetime import datetime
age = int(input("Enter your age: "))
year = datetime.now().year - age
print(f"We think you were born back in {year}")