def solution(id_list, report, k):
    # (나를 신고한 사람, 신고 당한 횟수) 저장
    id_list_dic = {}
    for id in id_list:
        id_list_dic[id] = [[], 0]
    # 중복 신고 제거
    report = list(set(report))

    for r in report:
        name_a = r.split()[0] # 신고한 사람
        name_p = r.split()[1] # 신고당한 사람
        id_list_dic[name_p][0].append(name_a)
        id_list_dic[name_p][1] += 1

    answer = {}
    for id in id_list:
        answer[id] = 0

    for key in id_list_dic:
        if id_list_dic[key][1] >= k:
            for id in id_list_dic[key][0]:
                answer[id] += 1

    return list(answer.values())