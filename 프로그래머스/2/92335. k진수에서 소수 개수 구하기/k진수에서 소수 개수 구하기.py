import math

def n_to_k(n, k):
    temp = []
    while n > 0:
        temp.append(str(n % k))
        n //= k
    return ''.join(temp[::-1])

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    number = n_to_k(n, k)
    candidates = number.split('0')
    answer = 0
    for num_str in candidates:
        if num_str == '':
            continue
        if is_prime(int(num_str)):
            answer += 1
    return answer