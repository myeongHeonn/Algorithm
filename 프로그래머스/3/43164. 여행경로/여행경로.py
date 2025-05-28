import copy
from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append([b, 0])

    for key in graph.keys():
        graph[key].sort()

    result = []
    def dfs(node):
        if len(answer) == len(tickets) + 1:
            temp = copy.deepcopy(answer)
            result.append(temp)
            return

        for idx, info in enumerate(graph[node]):
            next_node = info[0]
            visited = info[1]
            if visited == 1:
                continue

            graph[node][idx][1] = 1
            answer.append(next_node)
            dfs(next_node)
            graph[node][idx][1] = 0
            answer.pop()

    answer.append('ICN')
    dfs('ICN')

    return result[0]