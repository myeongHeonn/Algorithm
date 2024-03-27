import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp = []

def backt(depth):
    if len(temp) == m:
        print(*temp)
        return

    for i in range(depth, n+1):
        temp.append(i)
        backt(i)
        temp.pop()

backt(1)