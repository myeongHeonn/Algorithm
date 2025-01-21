def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            temp = numbers[i] + numbers[j]
            if temp in answer:
                continue
            answer.append(temp)

    answer.sort()

    return answer