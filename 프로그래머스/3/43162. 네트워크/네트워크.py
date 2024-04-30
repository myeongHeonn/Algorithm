def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0

    for computer in range(n):
        if not visited[computer]:
            dfs(n, computers, computer, visited)
            # dfs로 컴퓨터들을 최대한 방문 -> 연결된 하나의 네트워크
            answer += 1

    return answer

def dfs(n, computers, computer, visited):
    visited[computer] = True
    for con in range(n):
        # 컴퓨터가 연결되어 있으면 dfs
        if not visited[con] and computers[computer][con]:
            dfs(n, computers, con, visited)