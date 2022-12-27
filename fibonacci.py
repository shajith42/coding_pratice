c=int(input("enter number of terms:"))
n1=-1
n2=1
i=0
while i<=c:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    i+=1
    