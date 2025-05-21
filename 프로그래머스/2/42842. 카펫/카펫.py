def solution(brown, yellow):
    answer = []
    k = 1
    while True:
        yellow_h = k
        if yellow % k != 0:
            k += 1
            continue
        yellow_w = yellow // k
        
        h = yellow_h + 2
        w = yellow_w + 2
        
        if h * w == brown + yellow:
            answer.append(w)
            answer.append(h)
            break
        else:
            k += 1
    
    return answer