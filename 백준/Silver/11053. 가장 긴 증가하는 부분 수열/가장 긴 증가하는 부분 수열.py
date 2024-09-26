import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int,input().split()))
# dp[i] : sequence[i]를 마지막 값으로 가지는 가장 긴 부분수열의 길이
dp = [1 for _ in range(n+1)]

for i in range(1,n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))