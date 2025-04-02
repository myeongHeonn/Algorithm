def func2(file):
    value = ""
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    flag = False
    for c in file:
        if c in number:
            flag = True
            value += c
        else:
            flag = False
        if value != "" and not flag:
            break

    return int(value)

def func1(file):
    value = ""
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for c in file:
        if c not in number:
            value += c
        else:
            break
    return value.lower()

def solution(files):
    files = sorted(files, key=lambda file: (func1(file), func2(file)))
    return files