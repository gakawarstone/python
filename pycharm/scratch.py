def funny(number):
    first = (number // 1000) % 10 + (number // 10000) % 10 + number // 100000
    second = number % 10 + (number // 10) % 10 + (number // 100) % 10
    if first == second:
        return True
    else:
        return False

ticket = int(input())

if funny(ticket):
    print('счастливый')

else:
    print('обычный')