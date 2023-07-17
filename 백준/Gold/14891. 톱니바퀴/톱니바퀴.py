import sys
input = sys.stdin.readline

# 톱니 시계방향 회전
def rotationR(arr):
    a = arr.pop()
    arr.insert(0,a)

# 톱니 반시계방향 회전
def rotationL(arr):
    a = arr.pop(0)
    arr.insert(7,a)

# 톱니 바퀴의 상태 0->N/1->S
gear=[]
for _ in range(4):
    gear.append(list(map(int,input().rstrip())))

# 톱니바퀴의 회전 횟수
K = int(input())

# 회전 시킬 톱니바퀴의 번호(1,2,3,4)
# 방향(1->시계, -1->반시계)
# n->번호, d->방향
for _ in range(K):
    n, d = map(int,input().split())

    if n==1:# 첫 번쨰 톱니바퀴인 경우
        case1_2 = gear[0][2]
        case2_6 = gear[1][6]

        if d==1:# 시계방향
            rotationR(gear[0])
        elif d==-1:# 반시계방향
            rotationL(gear[0])

        if case1_2 != case2_6: # 1,2번 톱니바퀴의 맞닿은 극이 다를 경우 회전
            case2_2 = gear[1][2]
            case3_6 = gear[2][6]

            if d == 1:  # 1번이 시계방향이면 2번은 반시계방향
                rotationL(gear[1])
            elif d == -1:  # 1번이 반시계방향이면 2번은 시계방향
                rotationR(gear[1])

            if case2_2 != case3_6:# 2,3번 톱니바퀴의 맞닿은 극이 다를 경우 회전
                case3_2 = gear[2][2]
                case4_6 = gear[3][6]

                if d == 1:  # 1번이 시계방향이면 3번은 시계방향
                    rotationR(gear[2])
                elif d == -1:  # 1번이 반시계방향이면 3번은 반시계방향
                    rotationL(gear[2])

                if case3_2 != case4_6:# 3,4번 톱니바퀴의 맞닿은 극이 다를 경우 회전
                    if d == 1:  # 1번이 시계방향이면 4번은 반시계방향
                        rotationL(gear[3])
                    elif d == -1:  # 1번이 반시계방향이면 4번은 시계방향
                        rotationR(gear[3])

    if n==2: #두 번째 톱니바퀴인 경우
        case2_6 = gear[1][6]
        case1_2 = gear[0][2]

        case2_2 = gear[1][2]
        case3_6 = gear[2][6]

        if d==1:# 시계방향
            rotationR(gear[1])
        elif d==-1:# 반시계방향
            rotationL(gear[1])

        if case2_6 != case1_2:# 1,2번 톱니 맞닿은 부분 비교
            if d == 1:  # 2번이 시계방향이면 1번은 반시계
                rotationL(gear[0])
            elif d == -1:  # 2번이 반시계방향이면 1번은 시계
                rotationR(gear[0])

        if case2_2 != case3_6: # 2,3번 톱니 비교
            case3_2 = gear[2][2]
            case4_6 = gear[3][6]

            if d == 1:  # 2번이 시계방향이면 3번은 반시계
                rotationL(gear[2])
            elif d == -1:  # 2번이 반시계방향이면 3번은 시계
                rotationR(gear[2])

            if case3_2 != case4_6:# 3,4번 톱니 비교
                if d == 1:  # 2번이 시계방향이면 4번은 시계방향
                    rotationR(gear[3])
                elif d == -1:  # 2번이 반시계방향이면 4번은 반시계방향
                    rotationL(gear[3])

    if n==3: #세 번째 톱니바퀴인 경우
        case3_6 = gear[2][6]
        case2_2 = gear[1][2]

        case3_2 = gear[2][2]
        case4_6 = gear[3][6]

        if d==1:# 시계방향
            rotationR(gear[2])
        elif d==-1:# 반시계방향
            rotationL(gear[2])

        if case3_2 != case4_6:# 3,4번 톱니 맞닿은 부분 비교
            if d == 1:  # 3번이 시계방향이면 4번은 반시계
                rotationL(gear[3])
            elif d == -1:  # 3번이 반시계방향이면 4번은 시계
                rotationR(gear[3])

        if case3_6 != case2_2: # 1,2번 톱니 비교
            case2_6 = gear[1][6]
            case1_2 = gear[0][2]

            if d == 1:  # 3번이 시계방향이면 2번은 반시계
                rotationL(gear[1])
            elif d == -1:  # 3번이 반시계방향이면 2번은 시계
                rotationR(gear[1])

            if case2_6 != case1_2:# 1,2번 톱니 비교
                if d == 1:  # 3번이 시계방향이면 1번은 시계방향
                    rotationR(gear[0])
                elif d == -1:  # 3번이 반시계방향이면 1번은 반시계방향
                    rotationL(gear[0])

    if n == 4:  # 네 번쨰 톱니바퀴인 경우
        case4_6 = gear[3][6]
        case3_2 = gear[2][2]

        if d == 1:  # 시계방향
            rotationR(gear[3])
        elif d == -1:  # 반시계방향
            rotationL(gear[3])

        if case4_6 != case3_2:  # 3,4번 톱니바퀴의 맞닿은 극이 다를 경우 회전
            case3_6 = gear[2][6]
            case2_2 = gear[1][2]

            if d == 1:  # 4번이 시계방향이면 3번은 반시계방향
                rotationL(gear[2])
            elif d == -1:  # 4번이 반시계방향이면 3번은 시계방향
                rotationR(gear[2])

            if case3_6 != case2_2:  # 2,3번 톱니바퀴의 맞닿은 극이 다를 경우 회전
                case2_6 = gear[1][6]
                case1_2 = gear[0][2]

                if d == 1:  # 4번이 시계방향이면 2번은 시계방향
                    rotationR(gear[1])
                elif d == -1:  # 4번이 반시계방향이면 2번은 반시계방향
                    rotationL(gear[1])

                if case2_6 != case1_2:  # 1,2번 톱니바퀴의 맞닿은 극이 다를 경우 회전
                    if d == 1:  # 4번이 시계방향이면 1번은 반시계방향
                        rotationL(gear[0])
                    elif d == -1:  # 4번이 반시계방향이면 1번은 시계방향
                        rotationR(gear[0])

score=0
if gear[0][0] == 1:
    score+=1
if gear[1][0] == 1:
    score+=2
if gear[2][0] == 1:
    score+=4
if gear[3][0] == 1:
    score+=8
print(score)