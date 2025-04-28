def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    x, y = 0, 0
    direction = 0
    
    for num in range(1, n * (n + 1) // 2 + 1):
        triangle[x][y] = num
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 0 <= nx < n and 0 <= ny <= nx and triangle[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 3
            x += dx[direction]
            y += dy[direction]
            
    answer = []
    for row in triangle:
        answer += row
    return answer