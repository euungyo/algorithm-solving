n=int(input())
check=-1
count3=0
count5=0

for i in range(n//5,-1,-1):
    rest=n-5*i

    if(rest%3==0):
        count3=rest//3
        count5=i
        check=1
        break

if(check==-1):
    print(-1)
else:
    print(count3+count5)
