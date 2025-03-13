from collections import defaultdict

def dfs(node, graph, paths):
    while graph[node]:
        next_node = graph[node].pop()
        dfs(next_node, graph, paths)
    paths.append(node)

def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in tickets:
        graph[a].append(b)
    
    for key in graph:
        graph[key].sort(reverse=True)
        
    paths = []
    
    dfs("ICN", graph, paths)
    return paths[::-1]