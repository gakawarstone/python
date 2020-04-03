def update_dictionary(d, key, value, mode='list'):
    if mode == 'list_up':
        if key in d:
            d[key] += 1
        else:
            d[key] = 0
            d[key] += 1

    if mode == 'list':
        if key in d:
            d_key = d[key]
            d_key.append(value)
        else:
            d[key] = []
            d_key = d[key]
            d_key.append(value)


def dict_output(d):
    for key in d:
        print(key, ':', sep='', end=' ')
        print(d[key])


def read(file_name):
    d = {}
    with open(file_name) as inp:
        for line in inp:
            l_str = line.strip().split(';')
            update_dictionary(d, l_str[0], 1, 'list_up')  # cnt matches team 1
            update_dictionary(d, l_str[2], 1, 'list_up')  # cnt matches team 2
    return d


def main():
    dict_output(read('input.txt'))


main()
