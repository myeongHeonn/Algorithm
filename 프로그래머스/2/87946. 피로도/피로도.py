def solution(k, dungeons):
    n = len(dungeons)
    visited = [False for _ in range(n)]

    def dfs(fatigue, cnt):
        max_answer = cnt

        for i in range(n):
            if not visited[i] and fatigue >= dungeons[i][0]:
                visited[i]= True
                max_answer = max(max_answer, dfs(fatigue - dungeons[i][1], cnt + 1))
                visited[i] = False

        return max_answer

    return dfs(k, 0)