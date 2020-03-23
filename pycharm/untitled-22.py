def update_dictionary(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 0
        d[key] += 1


def read():
    output_source = [i.lower() for i in input().split(' ')]
    return output_source


def cnt_words(input_source):
    output_source = {}
    for item in input_source:
        update_dictionary(output_source, item)
    return output_source


def main():
    d = read()
    my_dict = cnt_words(d)
    print(*my_dict)


main()
