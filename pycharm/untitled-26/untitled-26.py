def update_dictionary(d, key, value):
    if key in d:
        d_key = d[key]
        d_key.append(value)
    else:
        d[key] = []
        d_key = d[key]
        d_key.append(value)


def read(file_name):
    str = ''
    with open(file_name) as inp:
        for line in inp:
            list_line = [i for i in line.strip().split(';')]
            for item in list_line:
                update_dictionary(d, list_line[0], item)
