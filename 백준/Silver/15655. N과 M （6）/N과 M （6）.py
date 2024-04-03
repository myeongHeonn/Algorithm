import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
temp = []

def backt(start):
    if len(temp) == m:
        print(*temp)
        return

    for i in range(start, n):
        temp.append(s[i])
        backt(i+1)
        temp.pop()

backt(0)