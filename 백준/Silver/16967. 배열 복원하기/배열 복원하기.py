import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
arrayB = []

for _ in range(h+x):
    arrayB.append(list(map(int, input().split())))

arrayA = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        arrayA[i][j] = arrayB[i][j]

for i in range(x,h):
    for j in range(y,w):
        arrayA[i][j] = arrayB[i][j] - arrayA[i-x][j-y]

for row in arrayA:
    print(*row)