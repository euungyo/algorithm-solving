a=list(input())
for i in range(len(a),15):
    a.append('')
b=list(input())
for i in range(len(b),15):
    b.append('')
c=list(input())
for i in range(len(c),15):
    c.append('')
d=list(input())
for i in range(len(d),15):
    d.append('')
e=list(input())
for i in range(len(e),15):
    e.append('')
ans=[]

for i in range(15):
    if(a[i]=='' and b[i]=='' and 
       c[i]=='' and d[i]=='' and e[i]==''):
        break

    if(a[i]!=''):
        ans.append(a[i])    
    if(b[i]!=''):
        ans.append(b[i])    
    if(c[i]!=''):
        ans.append(c[i])    
    if(d[i]!=''):
        ans.append(d[i])    
    if(e[i]!=''):
        ans.append(e[i])

print(''.join(ans))
