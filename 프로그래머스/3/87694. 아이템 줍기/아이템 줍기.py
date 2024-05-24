from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # 테두리는 1, 내부는 0
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    queue = deque()
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    queue.append((cx, cy))

    while queue:
        x, y = queue.popleft()

        if x == ix and y == iy:
            return visited[x][y]/2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if visited[nx][ny] != 0:
                continue

            if graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))