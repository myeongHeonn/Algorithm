from collections import deque

def solution(maps):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])

    dist = [[-1] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 1

    while queue:
        y, x = queue.popleft()

        if y == n-1 and x == m-1:
            return dist[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if  maps[ny][nx] == 0:
                continue

            if dist[ny][nx] == -1:
                queue.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1

    return -1