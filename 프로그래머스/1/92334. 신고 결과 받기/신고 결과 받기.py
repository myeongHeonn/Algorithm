def solution(id_list, report, k):
    # dic[신고 당한 사람] = 신고한 사람 저장
    reported_user = {}
    # 중복 신고 제거
    report = list(set(report))

    for r in report:
        user_id, reported_id = r.split()
        if reported_id not in reported_user:
            reported_user[reported_id] = []
        reported_user[reported_id].append(user_id)

    count = {}
    for user_id in id_list:
        count[user_id] = 0

    for key in reported_user:
        if len(reported_user[key]) >= k:
            for user_id in reported_user[key]:
                count[user_id] += 1

    return list(count.values())