def equal_str(str1, str2):
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str2[i] == '*':
            continue
        if str1[i] != str2[i]:
            return False

    return True

def solution(user_id, banned_id):
    candidates = []
    for b in banned_id:
        possible = []
        for u in user_id:
            if equal_str(u, b):
                possible.append(u)
        candidates.append(possible)

    print(candidates)
    result = set()
    
    def dfs(index, path):
        if index == len(banned_id):
            result.add(tuple(sorted(path)))
            return
        for user in candidates[index]:
            if user not in path:
                dfs(index + 1, path + [user])
                
    dfs(0, [])

    return len(result)