n=int(input())

for i in range(n):
    total=0
    num=0
    score=list(map(int,input().split()))
    for j in range(score[0]):
        total+=score[j+1]
    average=round(total/score[0],3)

    for k in range(score[0]):
        if(score[k+1]>average):
            num+=1
    ans=num/score[0]*100      
    print(f"{ans:.3f}%")