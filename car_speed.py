# cook your dish here
import math
for i in range(int(input())):
    u, v, a, s = map(int, input().split())
    if ((u**2) - (2 * a * s)) > v**2:
        print("No")
    else:
        print("Yes")