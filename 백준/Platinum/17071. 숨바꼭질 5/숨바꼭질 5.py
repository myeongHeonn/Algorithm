import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MAX = 500000
# 방문한 짝수 최소시간과 홀수 최소시간 저장
visited = [[-1 for _ in range(MAX + 1)] for _ in range(2)]

def bfs():
    queue = deque()
    queue.append((n, 0))
    visited[0][n] = 0

    while queue:
        x, cnt = queue.popleft()
        flag = cnt % 2

        for nx in [x-1, x+1, 2*x]:
            if nx < 0 or nx > MAX:
                continue
            if visited[1-flag][nx] != -1:
                continue

            visited[1-flag][nx] = cnt + 1
            queue.append((nx, cnt + 1))

bfs()

t = 0
flag = 0
result = -1
while k <= 500000:
    if visited[flag][k] != -1:
        if visited[flag][k] <= t:
            result = t
            break
    flag = 1 - flag
    t += 1
    k += t

print(result)