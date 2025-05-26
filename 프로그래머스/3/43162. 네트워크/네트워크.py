def solution(n, computers):
    answer = 0
    graph = []
    for idx, computer in enumerate(computers):
        temp = []
        for i in range(n):
            if i == idx:
                continue
            if computer[i] == 1:
                temp.append(i)
        graph.append(temp)

    visited = [False] * n

    def dfs(node, parent):
        for next_node in graph[node]:
            if not visited[next_node] and next_node != parent:
                visited[next_node] = True
                dfs(next_node, node)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, -1)

    return answer