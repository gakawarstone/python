import random


def file_write(file_name, str):
    with open(file_name, 'w') as out:
        out.write(str)


def cnt_vowels(str):
    for i in range(len(str)):
        if i == 'а':
            cnt_a += 1
        if i == 'в':
            cnt_b += 1
        if i == 'с':
            cnt_c += 1
        if i == 'д':
            cnt_d += 1
        if i == 'е':
            cnt_e += 1


def main():
    number = int(input())
    my_str = ''
    for i in range(number):
        k = random.randint(1, 5)
        if k == 1:
            my_str += 'а '
        if k == 2:
            my_str += 'в '
        if k == 3:
            my_str += 'с '
        if k == 4:
            my_str += 'д '
        if k == 5:
            my_str += 'е '

    print(my_str)
    file_write('output.txt', my_str)


main()
