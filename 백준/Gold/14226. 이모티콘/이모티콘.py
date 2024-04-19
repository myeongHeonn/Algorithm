import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
distance = [[-1] * (n + 1) for _ in range(n+1)]
distance[1][0] = 0

def bfs():
    queue = deque()
    # 화면 이모티콘 개수, 클립보드 이모티콘 개수
    queue.append((1,0))

    while queue:
        s, c = queue.popleft()
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
        if distance[s][s] == -1:
            distance[s][s] = distance[s][c] + 1
            queue.append((s,s))
        # 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if s+c <= n and distance[s+c][c] == -1:
            distance[s+c][c] = distance[s][c] + 1
            queue.append((s+c, c))
        # 화면에 있는 이모티콘 중 하나를 삭제
        if s-1 >= 0 and distance[s-1][c] == -1:
            distance[s-1][c] = distance[s][c] + 1
            queue.append((s-1, c))

    answer = -1
    for i in range(n+1):
        if distance[n][i] != -1:
            if answer == -1 or answer > distance[n][i]:
                answer = distance[n][i]

    return answer

print(bfs())