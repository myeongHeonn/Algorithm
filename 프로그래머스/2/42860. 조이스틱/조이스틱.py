def solution(name):
    answer = sum([min(ord(alpha) - ord('A'), 26 - (ord(alpha) - ord('A'))) for alpha in name])
    n = len(name)
    min_move = n - 1

    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            # 이동거리: 앞에서 i까지 + 뒤에서 남은 거 처리하는 방식
            distance = 2 * i + (n - next_i)
            min_move = min(min_move, distance)

            distance = i + 2 * (n - next_i)
            min_move = min(min_move, distance)

    return answer + min_move