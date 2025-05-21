from collections import defaultdict

def solution(n, wires):
    answer = float("INF")

    tree = defaultdict(list)
    for parent, child in wires:
        tree[parent].append(child)
        tree[child].append(parent)

    for parent, child in wires:
        tree[parent].remove(child)
        tree[child].remove(parent)

        visited = [False] * (n + 1)
        count = 0

        def dfs(node):
            nonlocal count
            count = max(count, visited.count(True))

            for next_node in tree[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    dfs(next_node)

        dfs(list(tree.keys())[0])
        m = n - count
        answer = min(answer, abs(count - m))

        tree[parent].append(child)
        tree[child].append(parent)

    return answer