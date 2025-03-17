from collections import defaultdict
from collections import deque

def solution(n, edge):
    distance = [0 for _ in range(n+1)]
    graph = defaultdict(list)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append((1, 0)) # (현재 노드, 부모 노드)

    while queue:
        node, parent = queue.popleft()
        k = distance[node]

        for next_node in graph[node]:
            if next_node != parent and distance[next_node] == 0:
                distance[next_node] = k + 1
                queue.append((next_node, node))

    max_len = max(distance)
    answer = 0
    for dist in distance:
        if dist == max_len:
            answer += 1

    return answer