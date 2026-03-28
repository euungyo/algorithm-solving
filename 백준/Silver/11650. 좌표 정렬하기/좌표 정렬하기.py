n=int(input())
points=[]

for i in range(n):
    xy=list(map(int, input().split()))
    points.append(xy)

points.sort()

for x,y in points:
    print(x,y)