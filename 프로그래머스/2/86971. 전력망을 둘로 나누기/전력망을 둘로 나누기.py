def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node, parent):
        cnt = 1
        for child in graph[node]:
            if child != parent:
                cnt += dfs(child, node)
        return cnt
    
    answer = float("inf")
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        count_a = dfs(a, b)
        count_b = n - count_a
        
        answer = min(answer, abs(count_a - count_b))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer