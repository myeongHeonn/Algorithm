import sys
input = sys.stdin.readline

N = int(input())
dp=[0]*(N+1)
p=[0]+list(map(int,input().split()))

dp[1]=p[1]
for i in range(2,N+1):
    arr=[]
    for j in range(i):
        arr.append(dp[j] + p[i-j])
    dp[i]=max(arr)
print(dp[-1])