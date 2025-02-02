from collections import deque

def solution(cards1, cards2, goal):
    q_cards1 = deque(cards1)
    q_cards2 = deque(cards2)
    
    for word in goal:
        if q_cards1 and q_cards1[0] == word:
            q_cards1.popleft()
            continue
        elif q_cards2 and q_cards2[0] == word:
            q_cards2.popleft()
            continue
        else:
            return "No"
    
    return "Yes"