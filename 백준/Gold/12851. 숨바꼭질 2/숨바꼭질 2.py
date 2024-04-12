import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [0 for _ in range(MAX + 1)]
cnt = 0

def bfs():
    global cnt
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            cnt += 1
            continue

        for nx in [x-1, x+1, 2*x]:
            if nx < 0 or nx > 100000:
                continue
            if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                queue.append(nx)
                visited[nx] = visited[x] + 1

bfs()
print(visited[k])
print(cnt)