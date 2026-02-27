strings=list(input() for i in range(5))
ans=[]

for i in range(15):
    for j in strings:
        if(i<len(j)):
            ans.append(j[i])

print(''.join(ans))