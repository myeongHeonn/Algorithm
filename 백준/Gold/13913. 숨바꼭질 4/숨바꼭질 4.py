import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 10 ** 5 + 1
distance = [0] * MAX
# 자식 노드가 부모 노드를 알기 위한 정보
check = [0] * MAX

def move(x):
    data = []
    temp = x
    for _ in range(distance[x] + 1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str, data[::-1])))

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(distance[x])
            move(x)
            break
        for nx in (x-1, x+1, x*2):
            if nx < 0 or nx >= MAX:
                continue
            # 처음 방문한것만 처리
            # 가장 빠른 시간만 구하면 되기 때문
            if not distance[nx]:
                distance[nx] = distance[x] + 1
                queue.append(nx)
                # 수빈이가 지나온 위치를 알기위해 다음 이동위치에 현재 이동위치를 기록
                check[nx] = x

bfs()