import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dic={}

for i in range(n):
    site,password=input().split()
    dic[site]=password

for i in range(m):
    url=input().strip()
    print(dic[url])
    