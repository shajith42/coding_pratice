# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
r="-"
c=".|."

# upper design
for i in range(1,(n-1),2):
     print((c*i).center(m,r))
     
#middle line     
print("WELCOME".center(m,r))

# lower design
for i in range((n-2),0,-2):
     print((c*i).center(m,r))