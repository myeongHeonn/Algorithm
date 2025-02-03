def solution(want, number, discount):
    n = len(want)
    count = 0

    for i in range(0, len(discount)-10+1):
        dic = {}
        for k in range(n):
            dic[want[k]] = number[k]

        for j in range(i, 10+i):
            # 해당 물품이 내가 원하는 물건이 아니거나
            # 이미 원하는 개수에 도달했으면 종료
            if discount[j] not in dic:
                break
            dic[discount[j]] -= 1

        # 딕셔너리 값이 모두 0이면 카운트
        flag = True
        for value in dic.values():
            if value:
                flag = False
                break

        if flag:
            count += 1

    return count