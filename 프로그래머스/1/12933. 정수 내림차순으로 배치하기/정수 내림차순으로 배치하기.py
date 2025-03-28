def solution(n):
    number = [int(x) for x in str(n)]
    number.sort(reverse=True)

    return int("".join(map(str, number)))