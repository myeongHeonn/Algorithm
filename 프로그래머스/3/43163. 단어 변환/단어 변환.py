def can_trans(cur_word, next_word):
    count = 0
    for idx, c in enumerate(cur_word):
        if c == next_word[idx]:
            count += 1

    if count == len(cur_word) - 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = float("INF")
    n = len(words)
    visited = [False] * n

    def dfs(cur_word, depth):
        nonlocal answer
        if cur_word == target:
            answer = min(answer, depth)
            return

        for i in range(n):
            if not visited[i] and can_trans(cur_word, words[i]):
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False

    dfs(begin, 0)
    return 0 if answer == float("INF") else answer