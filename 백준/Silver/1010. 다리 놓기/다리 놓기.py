t=int(input())

for i in range(t):
    numerator=1 #분자
    denominator=1 #분모

    n,m=map(int,input().split())
    for j in range(1,m+1):
        numerator*=j
    for k in range(1,n+1):
        denominator*=k
    for l in range(1,m-n+1):
        denominator*=l
    print(numerator//denominator)

