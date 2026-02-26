n=int(input())
ans=list(input())

for i in range(n-1):
    str=input()

    for i in range(len(str)):
        if(ans[i]!=str[i]):
            ans[i]='?'

print(''.join(ans))