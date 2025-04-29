def solution(storage, requests):
    from collections import deque

    n, m = len(storage), len(storage[0])
    board = [list(row) for row in storage]
    reachable = [[False]*m for _ in range(n)]

    # 초기 접근 가능 위치 표시 (외곽)
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                reachable[i][j] = True

    # 4방향
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def update_reachable():
        q = deque()
        visited = [[False]*m for _ in range(n)]

        # 접근 가능한 칸들에서 시작
        for i in range(n):
            for j in range(m):
                if reachable[i][j] and board[i][j] == '':
                    q.append((i, j))
                    visited[i][j] = True

        while q:
            y, x = q.popleft()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and not reachable[ny][nx] and board[ny][nx] != '':
                        reachable[ny][nx] = True  # 접근 가능해짐
                    elif not visited[ny][nx] and board[ny][nx] == '':
                        visited[ny][nx] = True
                        q.append((ny, nx))

    for req in requests:
        ch = req[0]
        if len(req) == 1:  # 지게차
            for i in range(n):
                for j in range(m):
                    if board[i][j] == ch and reachable[i][j]:
                        board[i][j] = ''
            update_reachable()  # 꺼낸 뒤 접근 가능 영역 다시 계산

        else:  # 크레인
            for i in range(n):
                for j in range(m):
                    if board[i][j] == ch:
                        board[i][j] = ''
            update_reachable()

    # 남은 컨테이너 세기
    return sum(1 for i in range(n) for j in range(m) if board[i][j] != '')
