from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    # 모든 weak 지점을 시작점으로 설정하며 경우의 수 탐색
    for i in range(length):
        for friends in permutations(dist, len(dist)):
            cnt = 1
            # 현재 친구가 어디 지점까지 갈 수 있는지 저장
            position = weak[i] + friends[cnt - 1]

            # 현재 투입된 친구가 다음 weak 지점까지 갈 수 있는지 검사
            for j in range(i, i + length):
                # 다음 weak 지점까지 못 가면 친구 추가
                if position < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[j] + friends[cnt - 1]

            answer = min(answer, cnt)

    return answer if answer <= len(dist) else -1