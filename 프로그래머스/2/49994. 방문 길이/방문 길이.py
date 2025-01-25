# 좌표평면을 벗어나는지 확인
def is_valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

# 다음 좌표 결정 함수
def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'R':
        nx, ny = x+1, y
    elif dir == 'L':
        nx, ny = x-1, y
    return nx, ny

# 메인함수
def solution(dirs):
    # 현재 위치
    x, y = 5, 5
    # 겹치는 좌표는 1개로 처리하기 위해 set() 사용
    answer = set()
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        # A에서 B로 간 경우 B에서 A도 추가해야 함
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
    return len(answer)/2