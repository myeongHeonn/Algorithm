def solution(s):
    answer = 0
    is_x = 0
    is_not_x = 0
    for i in s:
        if is_x == is_not_x:
            answer += 1
            x = i
        if x == i:
            is_x += 1
        else:
            is_not_x += 1

    return answer