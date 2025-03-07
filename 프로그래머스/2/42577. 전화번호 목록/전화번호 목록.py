def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        l = len(phone_book[i])
        if phone_book[i + 1][:l] == phone_book[i]:
            return False

    return True