import sys
input=sys.stdin.readline

n=int(input())
total=0
numbers={}
nums=[]

for i in range(n):
    num=int(input())
    nums.append(num)

    total+=num
    if num in numbers:
        numbers[num]+=1
    else:
        numbers[num]=1 

nums.sort()
result=sorted(numbers.items(), key=lambda x:(-x[1], x[0]))

if(len(nums)==1):
    for i in range(3):
        print(nums[0])
    print(0)

else:
    ave=round(total/n)
    cen=nums[n//2]
    ran=nums[-1]-nums[0]

    print(ave)
    print(cen)

    if len(result) > 1 and result[0][1] == result[1][1]:
        print(result[1][0])
    else:
        print(result[0][0])


    print(ran)