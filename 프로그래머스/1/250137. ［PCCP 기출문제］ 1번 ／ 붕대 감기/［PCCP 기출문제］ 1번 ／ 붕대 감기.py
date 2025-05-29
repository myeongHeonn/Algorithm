from collections import deque

def solution(bandage, health, attacks):
    MAX = health
    time = 0
    sequence = 0
    attacks = deque(attacks)
    
    while attacks:
        time += 1
        
        if attacks and attacks[0][0] == time: # 공격 당할때
            _, damage = attacks.popleft()
            health -= damage
            sequence = 0
            
            if health <= 0:
                return -1
            
            continue
        else: # 공격 당하지 않을때
            sequence += 1
            health += bandage[1]
            if sequence == bandage[0]:
                sequence = 0
                health += bandage[2]
            if health > MAX:
                health = MAX
                
            
    return health