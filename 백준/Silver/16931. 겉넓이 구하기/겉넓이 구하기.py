import sys
input = sys.stdin.readline

n, m = map(int, input().split())
block = []
result = 0
tempSum1 = 0
tempSum2 = 0

for _ in range(n):
    block.append(list(map(int, input().split())))

# 위, 아래
result += (n * m) * 2

# 이전 값이 현재 값보다 작을때
# -> 현재 값 - 이전 값
# 이전 값이 현재 값과 같을때
# -> 패스
# 이전 값이 현재 값보다 클때
# -> 패스

# 서 -> 동
for i in range(n):
    value = block[i][0] # 첫 번째 블록 개수
    result += value
    for j in range(1, m):
        if block[i][j-1] < block[i][j]:
            result += (block[i][j] - block[i][j-1])

# 동 -> 서
for i in range(n):
    value = block[i][-1] # 첫 번째 블록 개수
    result += value
    for j in range(m-1,0,-1):
        if block[i][j-1] > block[i][j]:
            result += (block[i][j-1] - block[i][j])

for i in range(m):
    value = block[0][i]
    result += value
    for j in range(1,n):
        if block[j-1][i] < block[j][i]:
            result += (block[j][i] - block[j-1][i])

for i in range(m):
    value = block[-1][i]
    result += value
    for j in range(n-1,0,-1):
        if block[j-1][i] > block[j][i]:
            result += (block[j-1][i] - block[j][i])

print(result)