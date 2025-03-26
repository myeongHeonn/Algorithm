def solution(n):
    battery = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            battery += 1

    return battery