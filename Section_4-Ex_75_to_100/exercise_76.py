# Date and Time Generator
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime("Today is %A, %B%d, %Y"))

