n=int(input())
dance={"ChongChong"}

for i in range(n):
    a,b=input().split()
    
    if(a in dance or b in dance):
        if(a not in dance):
            dance.add(a)
        elif(b not in dance):
            dance.add(b)

print(len(dance))
