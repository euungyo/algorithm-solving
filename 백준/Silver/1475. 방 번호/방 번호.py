room=input()
if(room.find('6')!=-1):
    room=room.replace('6','9')

set=1

for i in range(len(room)):
    num=room.count(room[i])
    if(room[i]=='9'):
        if(num%2==0):
            num=num//2
        else:
            num=num//2+1    

    if(num>set):
        set=num
        
print(set)        