def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]
        
        # 판매자로부터 차례대로 상위 노드로 이동하며 이익 분배
        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10

    return [total[name] for name in enroll]