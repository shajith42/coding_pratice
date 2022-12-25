result=[]
scorelst=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result+=[[name,score]]
        scorelst+=[score]
    b=sorted(list(set(scorelst)))[1]

    for a,c in sorted(result):
        if c==b:
            print(a)