def dfs(node, visited, computers):
    visited[node] = True
    for next_node in range(len(computers)):
        if computers[node][next_node] and not visited[next_node]:
            dfs(next_node, visited, computers)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i]:
            continue
        dfs(i, visited, computers)
        answer += 1

    return answer