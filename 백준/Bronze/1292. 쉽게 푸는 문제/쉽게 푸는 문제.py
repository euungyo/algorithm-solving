li=[]
a,b=map(int,input().split())
count=0

for i in range(1,b+1):
    for j in range(i):
        li.append(i)


for i in range(a-1,b):
    count+=li[i]

print(count)    