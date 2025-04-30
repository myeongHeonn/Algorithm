
def solution(n, w, number):
    if w == 1:
        return n - number + 1
    
    answer = 0
    container = [[] for _ in range(w)]
    container[0].append(1)

    idx = 1
    direction = [1, 0, -1, 0]
    d = 0

    for num in range(2, n + 1):
        container[idx].append(num)
        # 오른쪽으로 쌓다가 끝에 도달할 경우
        if d == 0 and num % w == 0:
            d = 1
        # 오른쪽 끝에 위에 하나 더 쌓은 경우
        if d == 1 and num % w == 1:
            d = 2
        # 왼쪽으로 쌓다가 끝에 도달한 경우
        if d == 2 and num % w == 0:
            d = 3
        # 왼쪽으로 끝에 위에 하나 더 쌓은 경우
        if d == 3 and num % w == 1:
            d = 0
        idx += direction[d]

    for col in container:
        if number in col:
            while col:
                answer += 1
                if number == col.pop():
                    return answer
