print('''1.celsius to fahrenheit
2.fahrenheit to celsius''')
ch=input("for celsius=(1,c,celsius)\nfor fahrenheit=(2,f,fahrenheit) select any one from bracket= ")
if ch== "1" and "celsius" and "c":
    c=float(input("Enter the celsuis:")) 
    f=(c*9/5)+32
    print(f"fahrenheit is {f}")
elif ch== "2" and "fahrenheit" and "f":
    f=float(input("Enter the fahrenheit:"))
    c=(f-32)*5/9
    print(f"celsius is {c}")
else:
    print("wrong choice")