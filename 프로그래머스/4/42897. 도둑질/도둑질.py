def solution(money):
    n = len(money)

    dp = [[0, 0] for _ in range(n)]

    dp[0][0], dp[0][1] = 0, money[0]
    dp[1][0], dp[1][1] = money[0], money[0]
    for i in range(1, n - 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + money[i]
    result = max(dp[-2])

    dp = [[0, 0] for _ in range(n)]
    dp[1][0], dp[1][1] = 0, money[1]
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + money[i]
    result = max(result, max(dp[-1]))

    return result