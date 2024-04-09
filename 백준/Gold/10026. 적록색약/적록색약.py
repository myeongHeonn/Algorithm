import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().rstrip())))

visited = [[0] * n for _ in range(n)]

cnt1 = 0
cnt2 = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, color):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny] != 0:
            continue

        if graph[nx][ny] == color:
            dfs(nx, ny, color)

for color in ['R','G','B']:
    for i in range(n):
        for j in range(n):
            # color인 구역
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]

for color in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                cnt2 += 1

print(cnt1, cnt2)