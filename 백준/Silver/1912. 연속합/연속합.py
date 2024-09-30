import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = sequence[0]

for i in range(1,n):
    dp[i] = max(sequence[i], dp[i-1]+sequence[i])

print(max(dp))