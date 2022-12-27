def swapList(list):
     
    start, *middle, end = list
    list = [end, *middle, start]
     
    return list
     

NL=[]
for i in range(5):
    element=input("enter the element in the list:")
    NL.append(element)
 

print(swapList(NL))