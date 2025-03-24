def solution(word):
    answer = []
    result = []

    def dfs(cur_word):
        if cur_word == word:
            result.append(len(answer))

        for s in ['A', 'E', 'I', 'O', 'U']:
            if len(cur_word) >= 5:
                return

            cur_word += s
            answer.append(cur_word)
            dfs(cur_word)
            cur_word = cur_word[:-1]

    dfs('')

    return result[0]