def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 아직 제거 안 된 k가 남아있다면 뒤에서 자르기
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)