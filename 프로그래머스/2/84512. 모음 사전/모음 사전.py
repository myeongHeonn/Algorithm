def make():
    global temp

    if len(temp) == 5:
        return

    for word in vowel:
        temp += word
        dict.append(temp)
        make()
        temp = temp[:-1]

vowel = "AEIOU"
dict = []
temp = ""

def solution(word):
    make()
    answer = dict.index(word) + 1
    return answer