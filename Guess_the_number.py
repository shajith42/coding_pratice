import random
num=random.randrange(1,50)
guesscheck="Wrong"
print("welcome to GAME")

while guesscheck=="Wrong":
    Ask=int(input("enter number between 1 to 50:"))
    try:
        val=int(Ask)
    except ValueError:
        print("Try to input number.\n Try Again!")
        continue
    val=int(Ask)
    if val<num:
        print("lower than guess number\n Try Again")
    elif val>num:
        print("greater than guess number\nTry Again!")
    else:
        print("this is correct number:",val)
        guesscheck="correct"        

print("thank you for playing")