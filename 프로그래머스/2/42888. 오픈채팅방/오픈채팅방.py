def solution(record):
    answer = []
    dic = {}

    for r in record:
        action = r.split()[0]
        user_id = r.split()[1]

        if action == "Enter":
            nickname = r.split()[2]
            dic[user_id] = nickname
            answer.append(user_id + " 님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(user_id + " 님이 나갔습니다.")
        elif action == "Change":
            nickname = r.split()[2]
            dic[user_id] = nickname

    for i in range(len(answer)):
        user_id = answer[i].split()[0]
        nickname = dic[user_id]
        answer[i] = nickname + answer[i][len(user_id)+1:]
        
    return answer
