total=0
for i in range(5):
    score=int(input())
    if score<40:
        score=40
    total=total+score

result=total//5
print(result)