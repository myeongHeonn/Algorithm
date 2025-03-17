from collections import defaultdict
from collections import deque

def solution(n, edge):
    distance = [-1 for _ in range(n+1)]
    distance[1] = 0
    graph = defaultdict(list)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append(1)

    while queue:
        node = queue.popleft()
        k = distance[node]

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = k + 1
                queue.append(next_node)

    max_len = max(distance)
    answer = distance.count(max_len)

    return answer