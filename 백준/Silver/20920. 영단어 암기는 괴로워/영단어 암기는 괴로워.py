import sys
input = sys.stdin.readline

n,m=map(int,input().split())
words={}

for i in range(n):
    word=input().strip()

    if(len(word)>=m):
        if word in words:
            words[word]+=1
        else:
            words[word]=1

ans=sorted(words.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))

for word,count in ans:
    print(word)