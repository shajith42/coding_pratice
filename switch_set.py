for i in range(int(input())):
    a,b,a1,b1,a2,b2=map(int,input().split())
    s=set((a,b))
    s1=set((a1,b1))
    s2=set((a2,b2))
    if s==s1:
        print(1)
    elif s==s2:
        print(2)
    else:
        print(0)