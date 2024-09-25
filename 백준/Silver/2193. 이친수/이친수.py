import sys
input = sys.stdin.readline

n = int(input())

dp = [[0,0] for _ in range(91)]

# n일때 [0으로 끝나는 개수, 1로 끝나는 개수]
dp[1] = [0,1]
dp[2] = [1,0]
dp[3] = [1,1]

for i in range(4,n+1):
    # 0이 붙는 경우는 이전 항이 0으로 끝날때랑 1로 끝날 때
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    # 1이 붙는 경우는 이전 항이 0으로 끝날때만
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))