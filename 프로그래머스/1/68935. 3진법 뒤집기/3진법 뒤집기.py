def solution(n):
    reverse_3 = ''

    while n != 0:
        reverse_3 += str(n % 3)
        n //= 3

    reverse_3 = int(reverse_3)
    reverse_3 = str(reverse_3)
    k = len(reverse_3)

    answer = 0
    for num in reverse_3:
        k -= 1
        num = int(num)
        for _ in range(k):
            num *= 3
        answer += num
    return answer