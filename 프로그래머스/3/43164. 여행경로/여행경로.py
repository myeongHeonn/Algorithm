from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for parent, child in tickets:
        graph[parent].append(child)
        
    for key in graph:
        graph[key].sort(reverse=True)
        
    path = []
    
    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        path.append(node)
        
    dfs("ICN")
    return path[::-1]