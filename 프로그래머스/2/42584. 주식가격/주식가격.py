def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for idx, price in enumerate(prices):
        while stack and price < stack[-1][1]:
            answer[stack[-1][0]] = idx - stack[-1][0]
            stack.pop()

        stack.append((idx, price))

    for i in range(len(answer) - 1):
        if answer[i] == 0:
            answer[i] = len(answer) - 1 - i

    return answer