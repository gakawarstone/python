def update_dictionary(d, key, value, mode='list'):
    if mode == 'list_up':
        if key in d:
            d[key] += 1
        else:
            d[key] = 0
            d[key] += 1

    elif mode == 'list':
        if key in d:
            d_key = d[key]
            d_key.append(value)
        else:
            d[key] = []
            d_key = d[key]
            d_key.append(value)

    else:
        if key in d:
            d_key = d[key]
            if mode in d_key:
                d_key[mode] += value
            else:
                d_key[mode] = value
        else:
            d[key] = {}
            d_key = d[key]
            d_key[mode] = value


def dict_output(d):
    for key in d:
        print(key, ':', sep='', end=' ')
        print(d[key])


def read(file_name):
    d = {}
    with open(file_name) as inp:
        for line in inp:
            l_str = line.strip().split(';')
            update_dictionary(d, l_str[0], 1, 'cnt')  # cnt matches team 1
            update_dictionary(d, l_str[2], 1, 'cnt')  # cnt matches team 2
            if l_str[1] > l_str[3]:
                update_dictionary(d, l_str[0], 1, 'win')
                update_dictionary(d, l_str[2], 1, 'lose')
            elif l_str[1] < l_str[3]:
                update_dictionary(d, l_str[0], 1, 'lose')
                update_dictionary(d, l_str[2], 1, 'win')
            else:
                update_dictionary(d, l_str[0], 1, 'draw')
                update_dictionary(d, l_str[2], 1, 'draw')
    return d


def main():
    dict_output(read('input.txt'))


main()
