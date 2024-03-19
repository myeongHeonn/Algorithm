def solution(bandage, health, attacks):
    answer = 0
    # 최대 체력
    max_health = health
    # 몬스터의 마지막 공격 시간
    end_time = attacks[-1][0]
    # 연속 회복 성공 수
    heal_cnt = 0
    # 현재 시간
    current_time = 0

    while True: # 시간(time)이 끝나거나 현재체력이 0이 되면 stop
        # 현재 시간 1초 증가
        current_time += 1
        # 현재시간이 몬스터 공격 시간일때
        if attacks[0][0] == current_time:
            health -= attacks[0][1]
            attacks.pop(0)
            heal_cnt = 0
            # 체력이 0이 되면 break
            if health <= 0:
                answer = -1
                break
        # 몬스터 공격 시간이 아닐때
        else:
            health += bandage[1]
            heal_cnt += 1
            if heal_cnt == bandage[0]:
                health += bandage[2]
                heal_cnt = 0
            if health >= max_health:
                health = max_health
        # 몬스터의 마지막 공격이 끝나면 그만
        if current_time == end_time:
            answer = health
            break
    return answer