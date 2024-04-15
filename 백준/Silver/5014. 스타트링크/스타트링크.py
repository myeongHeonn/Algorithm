import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f+1)]

def bfs():
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.popleft()

        if x == g:
            return visited[g] - 1

        for nx in [x + u, x - d]:
            if nx < 1 or nx > f:
                continue
            if visited[nx] != 0:
                continue

            queue.append(nx)
            visited[nx] = visited[x] + 1

    return "use the stairs"

print(bfs())