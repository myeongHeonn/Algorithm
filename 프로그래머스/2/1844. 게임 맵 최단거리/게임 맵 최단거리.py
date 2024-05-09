from collections import deque

def solution(maps):
    answer = -1

    n = len(maps)
    m = len(maps[0])

    visited = [[-1 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            answer = visited[x][y]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != -1:
                continue
            if maps[nx][ny] == 0:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

    return answer