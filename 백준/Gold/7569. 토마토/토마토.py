import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
box = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    box.append(temp)

visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
days = 0
tomatos = []
# 처음부터 익어있는 토마토 위치 확인
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                tomatos.append((i, j, k))
                visited[i][j][k] = 0
# bfs
def bfs():
    global days
    queue = deque()
    for tomato in tomatos:
        queue.append(tomato)

    while queue:
        z, x, y = queue.popleft()

        for l in range(6):
            nz = z + dz[l]
            nx = x + dx[l]
            ny = y + dy[l]

            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nz][nx][ny] != -1:
                continue

            if box[nz][nx][ny] == 0:
                visited[nz][nx][ny] = visited[z][x][y] + 1
                box[nz][nx][ny] = 1
                queue.append((nz, nx, ny))
                days = max(days, visited[nz][nx][ny])

# 저장될 때부터 모든 토마토가 익어있는 상태 확인
flag = False
flag2 = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                flag = True

if not flag:
    print(0)
else:
    bfs()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    flag2 = False
    if not flag2:
        print(-1)
    else:
        print(days)