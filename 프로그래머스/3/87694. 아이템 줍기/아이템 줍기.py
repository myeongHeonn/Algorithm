from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 102
    board = [[0 for _ in range(MAX)] for _ in range(MAX)]

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] = 1

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[False for _ in range(MAX)] for _ in range(MAX)]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    queue = deque()
    queue.append((characterX, characterY, 0))
    
    while queue:
        x, y, distance = queue.popleft()
        if x == itemX and y == itemY:
            return distance // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < MAX and 0 <= ny < MAX and
                not visited[nx][ny] and
                board[nx][ny] == 1):
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True