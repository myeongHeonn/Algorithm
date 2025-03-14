import heapq

def solution(board):
    n = len(board)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    # 최소 비용을 저장하는 3차원 배열 (방향에 따라 비용이 다름)
    cost = [[[float("INF")] * 4 for _ in range(n)] for _ in range(n)]
    # (비용, y, x, 방향)
    heap = []
    # 초기 위치 (0,0)에서 시작하며, 두 방향(하, 우)으로 시작할 수 있음
    for i in range(4):
        heapq.heappush(heap, (0, 0, 0, i))
        cost[0][0][i] = 0

    while heap:
        cur_cost, y, x, dir = heapq.heappop(heap)

        if y == n - 1 and x == n - 1:
            return cur_cost

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                # 새로운 방향이 기존 방향과 다르면 코너 비용 추가
                new_cost = cur_cost + (100 if i == dir else 600)
                # 더 적은 비용으로 방문할 수 있는 경우만 큐에 추가
                if new_cost < cost[ny][nx][i]:
                    cost[ny][nx][i] = new_cost
                    heapq.heappush(heap, (new_cost, ny, nx, i))

    return