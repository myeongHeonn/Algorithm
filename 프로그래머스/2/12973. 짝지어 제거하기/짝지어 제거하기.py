def solution(s):
    stack = []
    for c in s:
        # 스택이 비어 있으면 문자열을 넣어야 함
        if not stack:
            stack.append(c)
        else:
            # 다음 문자열이 스택에 마지막 문자열과 같다면 짝 제거
            if c == stack[-1]:
                stack.pop()
            # 다르다면 스택에 추가
            else:
                stack.append(c)
                
    if not stack:
        return 1
    else:
        return 0