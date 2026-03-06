n=int(input())
li=list(map(int,input().split()))
li.sort()
sum=0

for i in range(n):
    sum+=li[i]*(n-i)
print(sum)