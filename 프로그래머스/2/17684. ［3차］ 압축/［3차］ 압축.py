def solution(msg):
    answer = []
    dic = {chr(64+i): i for i in range(1, 27)}
    index = 27
    
    i = 0
    while i < len(msg):
        w = msg[i]
        while i+1 < len(msg) and w + msg[i+1] in dic:
            i += 1
            w += msg[i]
            
        answer.append(dic[w])
        if i+1 < len(msg):
            dic[w+msg[i+1]] = index
            index += 1
            
        i += 1

    return answer