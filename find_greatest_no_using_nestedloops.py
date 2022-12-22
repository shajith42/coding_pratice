a=int(input("enter a value="))
b=int(input("enter b value="))
c=int(input("enter c value="))
if a>c:   
    if a>b:
        great=a
else:
    if b>a:
        if b>c:
            great=b
    else:
        if c>a:
            if c>b:
                great=c

print(f"Greatest is {great}") 
