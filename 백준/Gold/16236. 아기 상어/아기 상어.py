import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
size = 2
stack = 0
time = 0
flag = True

# 가장 가까운 물고기를 찾아서 잡아먹는 함수
def bfs(ini_x, ini_y):
    global time
    global size
    global flag
    global stack
    queue = deque()
    queue.append((ini_x, ini_y))
    distance[ini_x][ini_y] = 0
    board[ini_x][ini_y] = 0
    fish = []

    while queue:
        x, y = queue.popleft()

        # 상어 이동
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 넘어간 경우 통과
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 방문한 경우 통과
            if distance[nx][ny] != -1:
                continue
            # 물고기 크기가 상어보다 클 경우 통과
            if board[nx][ny] > size:
                continue

            queue.append((nx, ny))
            distance[nx][ny] = distance[x][y] + 1

            if board[nx][ny] != 0 and board[nx][ny] < size:
                fish.append((distance[nx][ny], nx, ny))

    if fish:
        # 거리, 행, 열 순으로 정렬
        fish.sort()
        dist, fx, fy = fish[0]
        time += dist
        stack += 1
        if size == stack:
            size += 1
            stack = 0
        board[fx][fy] = 9
        return

    flag = False

while flag:
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                # 초기 미니 상어 위치 : a, b
                a, b = i, j
                break
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    bfs(a, b)

print(time)