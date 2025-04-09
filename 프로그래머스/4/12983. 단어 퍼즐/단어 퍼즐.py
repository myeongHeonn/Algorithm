def solution(strs, t):
    n = len(t)
    dp = [float("INF")] * (n + 1)
    dp[0] = 0

    k = 5 if n > 5 else n

    for i in range(1, n + 1):
        for j in range(k, 0, -1):
            idx = (i - j) if (i - j) >= 0 else 0
            if t[idx:i] in strs:
                dp[i] = min(dp[i], dp[idx] + 1)

    return -1 if dp[-1] == float("INF") else dp[-1]