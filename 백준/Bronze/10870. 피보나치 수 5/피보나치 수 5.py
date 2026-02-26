f=[0,1]
n=int(input())

for i in range(n-1):
    new=f[i]+f[i+1]
    f.append(new)
print(f[n])