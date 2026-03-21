from collections import deque

t=int(input())

for i in range(t):
    iserror=0
    isreverse=0

    fun=list(input())
    n=int(input())
    arr=input()
    arr=arr[1:-1]

    if(arr==''):
        nums=deque([])
    else:
        nums=deque(map(int,arr.split(',')))

    for j in range(len(fun)):
        if(fun[j]=='R'):
            isreverse+=1
        
        elif(fun[j]=='D'):
            if(len(nums)==0):
                iserror=1
                break
            else:
                if(isreverse%2==0):
                    nums.popleft()
                else:
                    nums.pop()

    if(iserror==0):
        if(isreverse%2==0):
            print('[' + ','.join(map(str, nums)) + ']')
        else:
            nums.reverse()
            print('[' + ','.join(map(str, nums)) + ']')
    else:
        print("error")