from collections import deque


def is_valid_move(y, x, n, board):
    return 0 <= y < n and 0 <= x < n and board[y][x] != 1

def solution(board):
    n = len(board)
    answer = float("inf")

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0, -1, 0))

    while queue:
        y, x, direction, cost = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not is_valid_move(ny, nx, n, board):
                continue

            new_cost = cost + (100 if direction == i or direction == -1 else 600)

            if visited[ny][nx][i] != 0 and visited[ny][nx][i] <= new_cost:
                continue

            visited[ny][nx][i] = new_cost

            if ny == n - 1 and nx == n - 1:
                answer = min(answer, new_cost)
            else:
                queue.append((ny, nx, i, new_cost))

    return answer