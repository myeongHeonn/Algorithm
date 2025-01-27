# 올바론 괄호 문자열인지 확인하는 함수
def is_corrent_s(s):
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c == ']':
            if stack and '[' == stack[-1]:
                stack.pop()
            else:
                return False
        elif c == '}':
            if stack and '{' == stack[-1]:
                stack.pop()
            else:
                return False
        elif c == ')':
            if stack and '(' == stack[-1]:
                stack.pop()
            else:
                return False

    return not stack

# 스택에서 맨 앞에 데이터를 꺼내서 맨 뒤로 삽입하는 함수
def func(stack):
    temp = stack.pop(0)
    stack.append(temp)
    return stack

# 메인함수
def solution(s):
    answer = 0
    stack = list(s)

    for _ in range(len(s)):
        stack = func(stack)
        if is_corrent_s(stack):
            answer += 1

    return answer