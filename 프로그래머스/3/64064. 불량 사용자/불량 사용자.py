'''
1. 응모자 아이디에서 불량 사용자 아이디 목록의 길이만큼 순열을 만든다.
2. 순열을 각 항과 불량 사용자를 비교해서 같은지 확인한다.
3. 같은 경우 set자료형으로 저장한다.
'''

from itertools import permutations

def check(users, banned_id):
    length = len(users)

    for i in range(length):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if users[i][j] != banned_id[i][j]:
                return False
            
    return True

def solution(user_id, banned_id):
    answer = []
    permutation_user_id = list(permutations(user_id, len(banned_id)))
    
    for users in permutation_user_id:
        if check(users, banned_id):
            users = set(users)
            if users not in answer:
                answer.append(users)

    return len(answer)