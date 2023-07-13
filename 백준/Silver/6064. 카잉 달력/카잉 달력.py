import sys
input = sys.stdin.readline

T=int(input())

def cal(M,N,x,y):
    K = x
    while K <= M*N:
        if (K-x)%M==0 and (K-y)%N==0:
            return K
        K += M
    return -1

for _ in range(T):
        M, N, x, y = map(int, input().split())
        print(cal(M,N,x,y))