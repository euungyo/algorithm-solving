n=int(input())
li=[]
result=0

for i in range(n):
    li.append(int(input()))

li.sort()

for i in range(n):
    if(li[i]*(n-i)>result):
        result=li[i]*(n-i)

print(result)