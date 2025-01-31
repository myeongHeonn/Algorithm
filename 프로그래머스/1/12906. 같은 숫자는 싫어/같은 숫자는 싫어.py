def solution(arr):
    stack = [arr[0]]

    for num in arr:
        if stack[-1] == num:
            continue
        else:
            stack.append(num)

    return stack