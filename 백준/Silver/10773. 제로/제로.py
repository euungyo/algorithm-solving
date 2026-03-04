n=int(input())
li=[]
sum=0

for i in range(n):
    num=int(input())
    li.append(num)
    if(num==0):
        del li[-1]
        del li[-1]

for i in range(len(li)):
    sum+=li[i]
print(sum)   