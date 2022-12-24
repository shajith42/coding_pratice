# Complete the solve function below.
import os
def solve(s):
    l=s.split(" ")
    for i in range(0,len(l)):
            l[i]=l[i].capitalize()
            s=" ".join(l)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
