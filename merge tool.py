from textwrap import wrap

def merge_the_tools(string, k):
    for t in wrap(string, k):
        print(*dict.fromkeys(t), sep="")
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)