def solution(citations):
    citations.sort(reverse=True)

    h = 0
    for citation in citations:
        if citation > h:
            h += 1
            continue
        else:
            break

    return h