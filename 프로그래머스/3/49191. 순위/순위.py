def solution(n, results):
    win = [[False for _ in range(n)] for _ in range(n)]

    for a, b in results:
        win[a - 1][b - 1] = True  # a가 b를 이겼음

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if win[i][k] and win[k][j]:
                    win[i][j] = True

    result = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j:
                if win[i][j] or win[j][i]:
                    count += 1
        if count == n - 1:
            result += 1

    return result