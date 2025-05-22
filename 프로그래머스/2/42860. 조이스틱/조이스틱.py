def solution(name):
    # 상하 이동 조작 횟수
    answer = sum(min(ord(c) - ord('A'), 26 - (ord(c) - ord('A'))) for c in name)

    # 좌우 이동 최솟값 계산
    move = len(name) - 1  # 기본은 오른쪽으로 쭉 가는 경우
    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        distance = i + len(name) - next_i + min(i, len(name) - next_i)
        move = min(move, distance)

    return answer + move