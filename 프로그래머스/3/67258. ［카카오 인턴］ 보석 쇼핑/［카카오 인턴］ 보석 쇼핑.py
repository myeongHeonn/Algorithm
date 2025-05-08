from collections import defaultdict

def solution(gems):
    total_types = len(set(gems))
    gem_count = defaultdict(int)
    min_length = float('inf')
    answer = [0, len(gems)]

    left = 0
    for right in range(len(gems)):
        gem_count[gems[right]] += 1

        while len(gem_count) == total_types:
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right + 1]
            
            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                del gem_count[gems[left]]
            left += 1

    return answer