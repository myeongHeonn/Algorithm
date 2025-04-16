import sys
sys.setrecursionlimit(3000)

def is_move(n, m, x, y):
    return 1 <= x <= n and 1 <= y <= m

def can_reach(x, y, r, c, left_distance):
    distance = abs(x - r) + abs(y - c)
    return distance <= left_distance and (left_distance - distance) % 2 == 0


def solution(n, m, x, y, r, c, k):
    answer = []
    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

    def dfs(cx, cy, path, left_distance):
        if answer:
            return
        
        if left_distance == 0:
            if cx == r and cy == c:
                answer.append(path)
            return

        for d, dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_move(n, m, nx, ny) and can_reach(nx, ny, r, c, left_distance - 1):
                dfs(nx, ny, path + d, left_distance - 1)
                
    if not can_reach(x, y, r, c, k):
        return "impossible"

    dfs(x, y, '', k)

    return answer[0] if answer else 'impossible'
