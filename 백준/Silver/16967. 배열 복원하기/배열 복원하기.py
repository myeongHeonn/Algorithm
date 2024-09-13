import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
arrayB = []

for _ in range(h+x):
    arrayB.append(list(map(int, input().split())))

arrayA = [[False] * w for _ in range(h)]

for i in range(h+x):
    for j in range(w+y):
        # 겹치는 범위가 아니면
        if i < x or i > h-x or j < y or j > w-y:
            if (h <= i and j <= y-1) or (w <= j and i <= x-1) :
                continue
            if 0 <= i <= h-1 and 0 <= j <= w-1:
                arrayA[i][j] = arrayB[i][j]
            else:
                arrayA[i-x][j-y] = arrayB[i][j]

for i in range(h+x):
    for j in range(w+y):
        if x <= i <= h-x and y <= j <= w-y:
            if not arrayA[i][j]:
                arrayA[i][j] = arrayB[i][j] - arrayA[i-x][j-y]

for row in arrayA:
    print(*row)