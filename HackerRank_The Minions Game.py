def minion_game(string):
    s=len(string)
    vowels=0
    consonant=0
    
    for i in range(s):
        if string[i] in 'AEIOU':
            vowels+=(s-i)
        else:
            consonant+=(s-i)
    if vowels < consonant:
        print(f"Stuart {consonant}")
    elif vowels > consonant:
        print(f"Kevin {vowels}")
    else:
        print("Draw")    
if __name__ == '__main__':
    s = input()
    minion_game(s)