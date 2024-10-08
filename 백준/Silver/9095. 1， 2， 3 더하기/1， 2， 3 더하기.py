import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0, 1, 2, 4]

    for i in range(4, n + 1):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

    print(dp[n])