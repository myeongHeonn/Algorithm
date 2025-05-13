def solution(s):
    stack = []
    
    for c in s:
        if not stack:
            if c == ')':
                return False
            else:
                stack.append(c)
        else:
            if c == ')':
                stack.pop()
            else:
                stack.append(c)
    
    if stack:
        return False
    return True