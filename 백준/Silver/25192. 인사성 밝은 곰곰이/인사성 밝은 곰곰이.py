n=int(input())
name=set()
count=0

for i in range(n):
    chat=input()
    if(chat=='ENTER'):
        name.clear()

    elif(chat not in name):
        name.add(chat)
        count+=1

print(count)    
