d = {}


def update_dictionary(d, key, value):
    if key in d:
        d_key = d[key]
        d_key.append(value)
    elif 2 * key in d.keys():
        d_key2 = d[key * 2]
        d_key2.append(value)
    else:
        d[key * 2] = []
        d_key2 = d[key * 2]
        d_key2.append(value)


update_dictionary(d, 1, -1)
update_dictionary(d, 2, -2)

print(d)
