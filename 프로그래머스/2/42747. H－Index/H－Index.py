def solution(citations):
    h = 0
    n = len(citations)
    
    for i in range(1, n + 1):
        count = 0
        for citation in citations:
            if citation >= i:
                count += 1
        if count >= i:
            h = i
    
    return h