# 문자열을 입력 받으면 0을 제거해서 문자열로 반환하는 함수
def remove_zero(string):
    value = ""
    for s in string:
        if s != '0':
            value += "1"
    return value

# 문자열 10진수를 받아서 2진수로 변환 후 문자열로 반환하는 함수
def transform_binary(string):
    string = int(string)
    binary = []

    while (string // 2) != 0:
        remain = string % 2
        binary.append(remain)
        string = (string // 2)

    binary.append(string)

    result = str(''.join(map(str, binary[::-1])))
    return result

def solution(s):
    answer = []
    remove_zero_cnt = 0
    transform_cnt = 0

    while s != "1":
        len_s = len(s)
        s = remove_zero(s)
        n = len(s)
        remove_zero_cnt += (len_s - n)

        s = transform_binary(str(n))
        transform_cnt += 1

    answer.append(transform_cnt)
    answer.append(remove_zero_cnt)

    return answer