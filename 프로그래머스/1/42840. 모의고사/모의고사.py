def solution(answers):
    answer = []
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]

    cnt1, cnt2, cnt3 = 0, 0, 0
    for idx in range(len(answers)):
        if answers[idx] == m1[idx%5]:
            cnt1 += 1
        if answers[idx] == m2[idx%8]:
            cnt2 += 1
        if answers[idx] == m3[idx%10]:
            cnt3 += 1

    max_cnt = max(cnt1, cnt2, cnt3)
    if max_cnt == cnt1:
        answer.append(1)
    if max_cnt == cnt2:
        answer.append(2)
    if max_cnt == cnt3:
        answer.append(3)

    return answer