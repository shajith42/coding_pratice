def print_rangoli(size):
    # your code goes here
    base = '-'.join([chr(i) for i in range(97,123)])
    patterns = [base[i*2:size*2-1] for i in range(size)]
    patterns = patterns[::-1] + patterns[1:] 
    for p in patterns:
        line = p[1:][::-1] + p
        print(line.center(size*4-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)