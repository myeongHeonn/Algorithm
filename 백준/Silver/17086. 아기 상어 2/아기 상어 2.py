import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[-1 for _ in range(m)] for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
answer = 0

# 한 점에서 상어까지 최단 거리
def bfs(a, b):
    global answer
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 0

    while queue:
        x, y = queue.popleft()

        if board[x][y] == 1:
            answer = max(answer, visited[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != -1:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    for j in range(m):
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        if board[i][j] == 1:
            continue
        bfs(i,j)

print(answer)