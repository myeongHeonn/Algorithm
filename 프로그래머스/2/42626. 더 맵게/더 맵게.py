import heapq

def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
        
    count = 0
    while heap:
        low_1 = heapq.heappop(heap)
        
        if low_1 >= K:
            return count
        
        if heap:
            low_2 = heapq.heappop(heap)
            value = low_1 + low_2 * 2
            heapq.heappush(heap, value)
            count += 1
        else:
            return -1