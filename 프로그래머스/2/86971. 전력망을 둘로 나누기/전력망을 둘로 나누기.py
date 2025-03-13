from collections import defaultdict
import sys

def dfs(node, graph, visited):
    visited[node] = True
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        dfs(next_node, graph, visited)

def count_true(visited):
    count = 0
    for flag in visited:
        if flag:
            count += 1
    return count

def solution(n, wires):
    answer = sys.maxsize

    for i in range(len(wires)):
        graph = defaultdict(list)
        for idx, (a, b) in enumerate(wires):
            # 전력망을 하나 자름
            if i == idx:
                continue
            graph[a].append(b)
            graph[b].append(a)

        visited = [True] + [False for _ in range(n)]
        count = 0
        net = []

        for key in range(1, len(wires) + 1):
            if visited[key]:
                continue
            dfs(key, graph, visited)
            count += 1
            net.append(count_true(visited))

            if count == 2:
                if all(visited):
                    answer = min(answer, abs((net[1] - net[0]) - (net[0] - 1)))
                    break
                else:
                    break
    return answer