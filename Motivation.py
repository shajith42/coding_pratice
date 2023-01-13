# cook your dish here
t=int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = []
    for i in range(n):
        j = list(map(int,input().split()))
        a.append(j)
    m = 0
    for i in a:
        if i[0] <= x:
            m = max(m,i[1])
    print(m)