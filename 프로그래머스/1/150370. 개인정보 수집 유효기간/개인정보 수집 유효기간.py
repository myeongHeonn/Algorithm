def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜를 년, 월, 일로 나눠서 리스트에 담아줌
    today_list = list(map(int, today.split('.'))) # [2022, 5, 19]
    # 약관 종류와 유효기간을 딕셔너리에 담아줌
    terms_dict = {}
    for term in terms:
        temp_term = term.split()
        terms_dict[temp_term[0]] = int(temp_term[1]) # {'A':'6'}
    num = 0 # 번호
    for privacy in privacies:
        num += 1
        temp = privacy.split()
        temp_date = list(map(int, temp[0].split('.'))) # [2021, 5, 2]
        temp_sort = temp[1] # A
        # 유효기간
        temp_date[1] += terms_dict[temp_sort]
        if temp_date[1] > 12:
            if temp_date[1] % 12 == 0:
                temp_date[0] += (temp_date[1]//12 -1)
                temp_date[1] = 12
            else:
                temp_date[0] += (temp_date[1] // 12)
                temp_date[1] = temp_date[1] % 12
        # 유효기간 지났는지 비교
        if today_list[0] > temp_date[0]:
            answer.append(num)
            continue
        elif today_list[0] == temp_date[0]:
            if today_list[1] > temp_date[1]:
                answer.append(num)
                continue
            elif today_list[1] == temp_date[1]:
                if today_list[2] >= temp_date[2]:
                    answer.append(num)

    return answer