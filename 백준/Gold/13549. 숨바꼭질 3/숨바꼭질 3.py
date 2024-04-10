import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [False] * (MAX + 1)
distance = [0] * (MAX + 1)

def bfs():
    queue = deque()
    queue.append(n)

    while True:
        x = queue.popleft()

        if x == k:
            print(distance[x])
            break

        for nx in [2*x, x-1, x+1]:
            if nx < 0 or nx > MAX:
                continue
            if visited[nx]:
                continue

            if nx == 2*x:
                distance[nx] = distance[x]
            else:
                distance[nx] = distance[x] + 1

            visited[nx] = True
            queue.append(nx)

bfs()