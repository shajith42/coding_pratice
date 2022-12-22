#To display current date and time
from datetime import datetime
now=datetime.now()
date=now.strftime("%d/%m/%y")
time=now.strftime("%H.%M.%S")
print(f"CURRENT DATE :{date}")
print(f"CURRENT TIME :{time}")
