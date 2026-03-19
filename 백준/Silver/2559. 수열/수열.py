
n,k=map(int,input().split())
nums=list(map(int,input().split()))

prefix=[0]*(n+1)

for i in range(n):
    prefix[i+1]=prefix[i]+nums[i]

result=[]
for i in range(n+1-k):
    result.append(prefix[k+i]-prefix[i])

print(max(result))