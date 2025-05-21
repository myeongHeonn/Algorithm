def solution(answers):
    count = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for idx, answer in enumerate(answers):
        if p1[idx % 5] == answer:
            cnt1 += 1
        if p2[idx % 8] == answer:
            cnt2 += 1
        if p3[idx % 10] == answer:
            cnt3 += 1

    max_cnt = max(cnt1, cnt2, cnt3)
    if max_cnt == cnt1:
        count.append(1)
    if max_cnt == cnt2:
        count.append(2)
    if max_cnt == cnt3:
        count.append(3)

    return count