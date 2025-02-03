def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    count = 0

    for i in range(len(discount)-9):
        discount_dict = {}

        for j in range(i, i+10):
            if discount[j] in want_dict:
                discount_dict[discount[j]] = discount_dict.get(discount[j], 0) + 1

        if discount_dict == want_dict:
            count += 1
        
    return count