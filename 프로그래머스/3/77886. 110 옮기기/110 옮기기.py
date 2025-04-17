def solution(s):
    answer = []
    for string in s:
        stack = []
        count = 0

        for char in string:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1

        rest = ''.join(stack)

        insert_idx = rest.rfind('0') + 1
        new_string = rest[:insert_idx] + '110' * count + rest[insert_idx:]
        answer.append(new_string)

    return answer