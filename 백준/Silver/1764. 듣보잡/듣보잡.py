n,m=map(int,input().split())
nohear=set()
nohearandlook=[]

for i in range(n):
    nohear.add(input())
for i in range(m):
    nolook=input()
    if(nolook in nohear):
        nohearandlook.append(nolook)

nohearandlook.sort()
print(len(nohearandlook))
for i in range(len(nohearandlook)):
    print(nohearandlook[i])