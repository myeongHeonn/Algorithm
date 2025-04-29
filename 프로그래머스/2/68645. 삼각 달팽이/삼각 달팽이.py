def solution(n):
    answer = []
    triangle = [[0] * (i + 1) for i in range(n)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    direction = 0
    x, y = 0, 0

    for i in range(1, (n * (n + 1)) // 2 + 1):
        triangle[x][y] = i

        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < n and 0 <= ny <= nx and triangle[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 3
            x = x + dx[direction]
            y = y + dy[direction]

    for row in triangle:
        answer += row
    return answer