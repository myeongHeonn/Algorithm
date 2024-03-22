import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
check = [False] * (n+1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(1, n+1):
        if check[i]:
            continue
        check[i] = True
        s.append(i)
        dfs()
        s.pop()
        check[i] = False

dfs()
