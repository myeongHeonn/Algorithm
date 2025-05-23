from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0, 1)) # (y, x, 이동 횟수)
    
    while queue:
        y, x, move_cnt = queue.popleft()
        if y == n - 1 and x == m - 1:
            return move_cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < n and 0 <= nx < m 
                    and not visited[ny][nx] 
                    and maps[ny][nx] == 1):
                visited[ny][nx] = True
                queue.append((ny, nx, move_cnt + 1))
    
    return answer