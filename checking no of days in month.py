print('''List of months:
 January, February, March, April, May,
  June, July, August, September, October, November, December''')
month_name = input("Input the name of Month: ")
month=month_name.capitalize() # to change first letter captial and other to small

if month == "February":
	print("No. of days: 28/29 days")
elif month in ("April", "June", "September", "November"):
    print(f"{month} having 30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print(f"{month} having 31 days")
else:
	print("Wrong month name") 
	