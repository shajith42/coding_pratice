# cook your dish here
t = int(input())
for i in range(t):
    n, s = list(map(int, input().split()))
    a = 0
    b = s
    while(not(b <= n)):
        a += 1
        b -= 1
    # print(a, b)
    print(abs(a - b))
    t -= 1