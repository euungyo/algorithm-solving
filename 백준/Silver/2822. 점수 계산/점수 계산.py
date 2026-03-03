scores=[]

for i in range(8):
    scores.append((int(input()),i+1))

scores.sort(reverse=True)
top5=scores[:5]
total=0

for i in range(5):
    total+=top5[i][0]

num=sorted(index for score,index in top5)

print(total)
print(*num)