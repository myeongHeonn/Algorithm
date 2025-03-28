def solution(n):
    number = list(str(n))
    number.sort(reverse=True)
    return int("".join(number))