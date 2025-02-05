def solution(orders, course):
    answer = []
    for count in course:
        orders_dic = {}
        arr = []
        for order in orders:
            if len(order) < count:
                continue
            s = []
            check = [False] * len(order)
            dfs(arr, order, count, 0, s, check)

        for a in arr:
            if a in orders_dic:
                orders_dic[a] += 1
            else:
                orders_dic[a] = 1

        max_order_count = 0
        if orders_dic:
            max_order_count = max(orders_dic.values())
        for key in orders_dic:
            if orders_dic[key] == max_order_count and orders_dic[key] > 1:
                answer.append(key)

    return sorted(answer)

# course개 만큼 만들수 있는 모든 조합
# 메뉴 k개 모든 조합
def dfs(arr, order, k, depth, temp, check):
    if len(temp) == k:
        temp = sorted(temp)
        arr.append(''.join(temp))
        return

    for i in range(depth, len(order)):
        if check[i]:
            continue
        check[i] = True
        temp.append(order[i])
        dfs(arr, order, k, i+1, temp, check)
        temp.pop()
        check[i] = False