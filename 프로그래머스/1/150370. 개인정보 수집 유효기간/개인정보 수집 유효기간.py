def solution(today, terms, privacies):
    answer = []
    dic_terms = {}
    for term in terms:
        dic_terms[term[0]] = term[2:]

    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:10])

    for idx, privacy in enumerate(privacies):
        col_day = privacy[:10]
        col_alpha = privacy[-1]
        col_term = int(dic_terms[col_alpha])

        col_year = int(col_day[:4])
        col_month = int(col_day[5:7])
        col_day = int(col_day[8:10])

        cmp_month = (col_month + col_term) % 12
        cmp_month = 12 if cmp_month == 0 else cmp_month
        cmp_year = col_year + ((col_month + col_term - 1) // 12)
        cmp_day = col_day

        if today_year > cmp_year:
            answer.append(idx + 1)
            continue
        elif today_year == cmp_year:
            if today_month > cmp_month:
                answer.append(idx + 1)
                continue
            elif today_month == cmp_month:
                if today_day >= cmp_day:
                    answer.append(idx + 1)
                    continue
        print(answer)

    return answer
