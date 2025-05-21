from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    m = len(numbers)
    numbers_list = [n for n in numbers]

    for i in range(1, m + 1):
        permutation_list = set(list(permutations(numbers_list, i)))

        for per in permutation_list:
            num = int("".join(per))
            if is_prime(num):
                answer.add(num)

    return len(answer)