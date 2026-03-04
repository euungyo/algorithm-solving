n=int(input())
li=[]
sum=0

for i in range(n):
    num=int(input())
    if(num==0):
        sum-=li[-1]
        li.pop()
    else:
        li.append(num)
        sum+=num
    
print(sum)   