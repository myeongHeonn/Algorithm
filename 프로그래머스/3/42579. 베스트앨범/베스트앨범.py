from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    dic_count = defaultdict(int)
    for idx in range(len(genres)):
        genre = genres[idx]
        play = plays[idx]
        dic[genre].append((play, idx))
        dic_count[genre] += play

    heap = []
    for g in dic_count:
        heapq.heappush(heap, (-dic_count[g], g))

    print(heap)

    while heap:
        count, genre = heapq.heappop(heap)

        heap1 = []
        for c, i in dic[genre]:
            heapq.heappush(heap1, (-c, i))

        cnt = 0
        while heap1:
            cnt += 1
            play_count, idx = heapq.heappop(heap1)
            answer.append(idx)

            if cnt == 2:
                break

    return answer