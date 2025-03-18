def solution(k, dungeons):
    answer = []
    n = len(dungeons)
    visited = [False for _ in range(n)]

    def dfs(k, count):
        if all(visited):
            answer.append(count)
            return

        for i in range(n):
            if visited[i]:
                continue

            if k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1)
                visited[i] = False
            else:
                visited[i] = True
                dfs(k, count)
                visited[i] = False

    dfs(k, 0)

    return max(answer)