import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

result = []
order = max(dp)
for i in range(n-1,-1,-1):
    if dp[i] == order:
        result.append(sequence[i])
        order -= 1

print(*result[::-1])