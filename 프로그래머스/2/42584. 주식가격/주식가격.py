def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]

    # 스택을 사용해 이전 가격과 현재 가격 비교
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            # 가격이 떨어졌을경우 이전 가격의 기간 계산
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    # 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer