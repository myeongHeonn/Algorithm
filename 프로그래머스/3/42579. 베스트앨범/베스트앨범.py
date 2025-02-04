def solution(genres, plays):
    answer = []
    n = len(genres)
    # 해당 장르에 속한 고유번호들
    genre_num = {}
    # 장르별 재생횟수 합
    genre_sum = {}
    for i in range(n):
        if genres[i] in genre_num:
            genre_num[genres[i]].append(i)
        else:
            genre_num[genres[i]] = [i]

        if genres[i] in genre_sum:
            genre_sum[genres[i]] += plays[i]
        else:
            genre_sum[genres[i]] = plays[i]

    # 재생횟수 순서 기준으로 내림차순
    sorted_genre_sum = dict(sorted(genre_sum.items(), key=lambda item: item[1], reverse=True))

    for genre in sorted_genre_sum:
        # genre_num = {"classic":[1,2,3], "pop":[1,2]}
        # genre_num에 value 값을 재생횟수 순으로 정렬
        plays_dic = {}
        for no in genre_num[genre]:
            plays_dic[no] = plays[no]
        sorted_plays_dic = dict(sorted(plays_dic.items(), key=lambda item: item[1], reverse=True))

        # 재생횟수가 높은 상위 2개를 ans
        count = 0
        for no in sorted_plays_dic:
            if count == 2:
                break
            answer.append(no)
            count += 1

    return answer