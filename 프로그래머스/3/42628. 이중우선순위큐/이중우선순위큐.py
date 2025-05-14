import heapq

def solution(operations):
    heap = []

    for o in operations:
        if o[0] == 'I':
            num = int(o[2:])
            heapq.heappush(heap, num)
        else:
            if heap:
                if o == 'D -1':
                    heapq.heappop(heap)
                elif o == 'D 1':
                    v = max(heap)
                    heap.remove(v)

    if not heap:
        return [0, 0]
    else:
        return [max(heap), min(heap)]