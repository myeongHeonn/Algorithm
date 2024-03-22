import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [0] * (MAX + 1)

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        # k에 도달 시
        if x == k:
            return visited[x]
        # 이동 경우
        for nx in (x-1, x+1, 2*x):
            # 범위 벗어날 경우 패스
            if nx < 0 or nx > MAX:
                continue
            # 방문한 경우 패스
            if visited[nx] != 0:
                continue
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(bfs())