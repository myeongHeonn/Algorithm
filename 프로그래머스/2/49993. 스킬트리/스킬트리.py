def solution(skill, skill_trees):
    answer = len(skill_trees)

    for s in skill_trees:
        idx = 0

        for c in s:
            if c in skill:
                if c == skill[idx]:
                    idx += 1
                    continue
                else:
                    answer -= 1
                    break

    return answer