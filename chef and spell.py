# cook your dish here
for i in range(int(input())):
    spell =list(map(int,input().split()))
    spell.sort()
    print(spell[-1]+spell[-2])