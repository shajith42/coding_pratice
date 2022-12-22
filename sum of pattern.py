n=int(input("enter the num:"))
'''
for i in range(n+1):
  for j in range(i+1):
    print(i,end="")
  print("")
'''

for i in range(n+1):
    print(str(i) * i)
