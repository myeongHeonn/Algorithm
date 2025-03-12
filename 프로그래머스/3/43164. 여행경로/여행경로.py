from collections import defaultdict

def dfs(node, graph, path):
    while graph[node]:
        next_node = graph[node].pop()
        dfs(next_node, graph, path)
    path.append(node)

def solution(tickets):
    graph = defaultdict(list)

    for parent, child in tickets:
        graph[parent].append(child)

    for key in graph:
        graph[key].sort(reverse=True)

    path = []

    dfs("ICN", graph, path)
    return path[::-1]