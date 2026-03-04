import sys
input = sys.stdin.readline
stack=[]

def push(x):
    stack.append(x)

def pop():

    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop())



def size():
    print(len(stack))

def empty():
    if(len(stack)==0):
        print(1)
    else:
        print(0)

def top():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack[-1])

def main():
    n=int(input())

    for i in range(n):
        cmd=input().split()
        
        if cmd[0]=='push':
            push(int(cmd[1]))
        elif cmd[0]=='top':
            top()
        elif cmd[0]=='size':
            size()
        elif cmd[0]=='empty':
            empty()
        elif cmd[0]=='pop':
            pop()

main()