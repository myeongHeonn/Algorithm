def solution(numbers, target):
    answer = 0

    def dfs(depth, total):
        nonlocal answer
        if depth == len(numbers):
            if total == target:
                answer += 1
            return

        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])
        
    dfs(0, 0)

    return answer