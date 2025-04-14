def move(c):
    return min(ord(c) - ord('A'), 26 - (ord(c) - ord('A')))

def solution(name):
    answer = 0
    n = len(name)

    # 알파벳 바꾸는 비용 더하기
    for c in name:
        answer += move(c)

    # 커서 이동 최소 거리 계산
    min_move = n - 1  # 그냥 끝까지 가는 경우

    for i in range(n):
        next_i = i + 1
        # A 연속 구간 찾기
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        # 이동거리: 앞에서 i까지 + 뒤에서 남은 거 처리하는 방식
        distance = 2 * i + (n - next_i)  # 오른쪽 -> 왼쪽으로 우회
        min_move = min(min_move, distance)

        distance = i + 2 * (n - next_i)  # 왼쪽 -> 오른쪽으로 우회
        min_move = min(min_move, distance)

    return answer + min_move