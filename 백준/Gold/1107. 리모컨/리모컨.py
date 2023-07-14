import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
breakButton = list(map(int,input().split()))

cnt = abs(100-N)

for num in range(1000001):
    num=str(num)

    for i in range(len(num)):
        if int(num[i]) in breakButton:
            break
        elif i == len(num)-1:
            cnt=min(cnt,abs(int(num)-N)+len(num))

print(cnt)