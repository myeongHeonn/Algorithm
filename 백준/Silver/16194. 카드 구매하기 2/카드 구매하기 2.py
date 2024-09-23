import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
p = [0] + list(map(int, input().split()))
dp[1] = p[1]

for i in range(2, n+1):
    temp = []
    for j in range(i):
        temp.append(dp[j] + p[i-j])
    dp[i] = min(temp)

print(dp[-1])