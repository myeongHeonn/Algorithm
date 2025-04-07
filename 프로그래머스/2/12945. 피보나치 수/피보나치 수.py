def solution(n):
    dp = [0] * 100001
    dp[1] = 1
    dp[2] = 1

    for k in range(3, n + 1):
        dp[k] = dp[k - 1] + dp[k - 2]

    return dp[n] % 1234567