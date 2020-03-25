def update_dictionary(d, key, value):
    if key in d:
        d_key = d[key]
        d_key.append(value)
    else:
        d[key] = []
        d_key = d[key]
        d_key.append(value)


def read(file_name):
    d = {}
    with open(file_name) as inp:
        for line in inp:
            list_line = [i for i in line.strip().split(';')]
            for item in range(1, len(list_line)):
                if item == 0:
                    continue
                update_dictionary(d, list_line[0], int(list_line[item]))
    return d


def dict_output(d):
    for key in d:
        print(key, ':', sep='', end=' ')
        print(d[key])


def list_middle(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    middle = round(sum / len(l), 9)
    return middle


def main():
    d = read('input.txt')
    dict_output(d)
    print(list_middle(d['s']))


main()
