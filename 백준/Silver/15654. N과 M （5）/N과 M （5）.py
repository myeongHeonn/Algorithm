import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num=list(map(int,input().split()))
num=sorted(num)
s=[]
visited=[False]*n

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i]=True
        s.append(num[i])
        dfs()
        s.pop()
        visited[i]=False

dfs()