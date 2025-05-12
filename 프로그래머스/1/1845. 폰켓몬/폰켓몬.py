def solution(nums):
    n, m = len(nums) // 2, len(set(nums))
    return n if m >= n else m