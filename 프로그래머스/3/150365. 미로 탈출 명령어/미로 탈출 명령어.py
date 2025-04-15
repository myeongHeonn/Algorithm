import sys
sys.setrecursionlimit(3000)

def solution(n, m, x, y, r, c, k):
    answer = []

    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

    def can_reach(cx, cy, steps_left):
        dist = abs(cx - r) + abs(cy - c)
        return dist <= steps_left and (steps_left - dist) % 2 == 0

    def dfs(cx, cy, path, steps_left):
        if answer:
            return  # 이미 정답 찾음 (사전순 가장 빠른 경로)
        if steps_left == 0:
            if (cx, cy) == (r, c):
                answer.append(path)
            return

        for d, dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                if can_reach(nx, ny, steps_left - 1):
                    dfs(nx, ny, path + d, steps_left - 1)

    if not can_reach(x, y, k):
        return "impossible"

    dfs(x, y, "", k)

    return answer[0] if answer else "impossible"