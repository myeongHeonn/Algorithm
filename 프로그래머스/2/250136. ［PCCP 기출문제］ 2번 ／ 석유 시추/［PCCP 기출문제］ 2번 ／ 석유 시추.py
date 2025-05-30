from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[False for _ in range(m)] for _ in range(n)]
    label_map = [[-1 for _ in range(m)] for _ in range(n)]
    label_volume = dict()
    label = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                label_map[i][j] = label
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                volume = 0

                while queue:
                    volume += 1
                    y, x = queue.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and land[ny][nx] == 1:
                            queue.append((ny, nx))
                            label_map[ny][nx] = label
                            visited[ny][nx] = True

                label_volume[label] = volume
                label += 1

    total_volume = 0
    for j in range(m):
        column = set()
        column_volume = 0
        for i in range(n):
            if label_map[i][j] != -1:
                column.add(label_map[i][j])

        if column:
            for v in column:
                column_volume += label_volume[v]

        total_volume = max(total_volume, column_volume)

    return total_volume