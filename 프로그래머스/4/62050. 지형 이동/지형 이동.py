import heapq

def solution(land, height):
    n, m = len(land), len(land[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    heap = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    heapq.heappush(heap, (0, 0, 0))
    count = 0
    cost = 0
    while heap:
        v, y, x = heapq.heappop(heap)
        if visited[y][x]:
            continue
        
        visited[y][x] = True
        cost += v
        count += 1

        if count == n * m:
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if abs(land[ny][nx] - land[y][x]) > height:
                    heapq.heappush(heap, (abs(land[ny][nx] - land[y][x]), ny, nx))
                else:
                    heapq.heappush(heap, (0, ny, nx))

    return cost