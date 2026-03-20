n=int(input())
times=[]

for i in range(n):
    times.append(list(map(int,input().split())))

times.sort(key=lambda x:(x[1],x[0]))

count=1
temp=0
for i in range(n-1):
    if(times[temp][1]<=times[i+1][0]):
        count+=1
        temp=i+1

print(count)