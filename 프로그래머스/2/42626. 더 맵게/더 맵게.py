import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer

        min2 = heapq.heappop(scoville)
        new_value = min1 + min2 * 2

        heapq.heappush(scoville, new_value)
        answer += 1

    # 마지막 남은 원소 확인
    return answer if scoville[0] >= K else -1