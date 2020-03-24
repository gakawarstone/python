def update_dictionary(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 0
        d[key] += 1


def read(file_name):
    str = ''
    with open(file_name) as inp:
        for line in inp:
            str += line.strip()
            str += '\n'
    return str


def file_write(file_name, str):
    with open(file_name, 'w') as out:
        out.write(str)


def cnt_words(input_source):
    output_source = {}
    for item in input_source:
        update_dictionary(output_source, item)
    return output_source


def dict_output(d):
    for key in d:
        print(key, ':', sep='', end=' ')
        print(d[key])


def main():
    str = read('input.txt')
    d = cnt_words(str.lower().replace('\n', ' ').split(' '))
    c = True
    for key in d:
        if c:
            max_key = key
            c = False
        if d[max_key] == d[key] and key > max_key:
            max_key = key
        if d[max_key] < d[key]:
            max_key = key
    print(max_key, d[max_key], sep=' ')
#    dict_output(d)


main()
