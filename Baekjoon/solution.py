
def solution(phone_book):
    phone_book = sorted(phone_book, key = len)
    for i, value in enumerate(phone_book):
        length = len(value)
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:length] == value:
                return False
    return True



print(solution(['123','456','789']))
