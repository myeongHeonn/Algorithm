def solution(info, n, m):
    length = len(info)
    dp = [[float('INF')] * m for _ in range(length + 1)]
    dp[0][0] = 0

    for i in range(length):
        a_trace, b_trace = info[i]
        for b in range(m):
            if dp[i][b] == float('INF'):
                continue

            # A가 훔치는 경우
            if dp[i][b] + a_trace < n:
                dp[i + 1][b] = min(dp[i + 1][b], dp[i][b] + a_trace)

            # b가 훔치는 경우
            if b + b_trace < m:
                dp[i + 1][b + b_trace] = min(dp[i + 1][b + b_trace], dp[i][b])

    result = min(dp[length])
    return result if result != float('INF') else -1