import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
distance = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    distance[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if distance[nx][ny] != -1:
                continue

            if graph[nx][ny] == 0:
                distance[nx][ny] = distance[x][y]
                queue.appendleft((nx, ny))
            else:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

bfs()
print(distance[n-1][m-1])