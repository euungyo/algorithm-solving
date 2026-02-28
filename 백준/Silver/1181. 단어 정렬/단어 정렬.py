n=int(input())
li=[]

for i in range(n):
    word=input()
    if word not in li:
        li.append(word)    

li.sort(key=lambda x: (len(x), x))

for i in range(len(li)):
    print(li[i])

