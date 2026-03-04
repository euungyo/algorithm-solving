n=input()

if(int(n)<100):
    print(int(n))

else:
    count=99
    for i in range(100,int(n)+1):
        correct=0
        num=str(i)
        term=int(num[0])-int(num[1])
        for j in range(1,len(num)-1): 
            if(term!=int(num[j])-int(num[j+1])):
                correct=1
                break

        if(correct==0):
            count+=1

    print(count)