import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[-1] * n for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs():
    queue = deque()
    queue.append((r1, c1))
    visited[r1][c1] = 0

    while queue:
        x, y = queue.popleft()

        if (x,y) == (r2,c2):
            return visited[x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] != -1:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return -1

print(bfs())