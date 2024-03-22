import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 방문 여부 체크
visited = [False] * (n + 1)
temp = []

def backt(depth):
    if len(temp) == m:
        print(*temp)
        return

    for i in range(depth, n+1):
        # 방문한 적이 있으면 패스
        if visited[i]:
            continue
        visited[i] = True
        temp.append(i)
        backt(i+1)
        visited[i] = False
        temp.pop()

backt(1)