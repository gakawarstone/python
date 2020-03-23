def read(file_name):
    str = ''
    with open(file_name) as inp:
        for line in inp:
            str += line.strip()
    return str


def unzip_str(str_in):
    str_out = ''
    digit = ''
    cnt = 0
    write = True
    while cnt < len(str_in):
        if str_in[cnt].isalpha() and write:
            alpha = str_in[cnt]
            cnt += 1
        if str_in[cnt].isdigit():
            digit += str_in[cnt]
            cnt += 1
            if cnt < len(str_in) and str_in[cnt].isdigit():
                write = False
            else:
                write = True
        if write:
            str_out += alpha * int(digit)
            digit = ''
    return str_out


def file_write(file_name, str):
    with open(file_name, 'w') as out:
        out.write(str)


def main():
    input_source = read('input.txt')
    file_write('output.txt', unzip_str(input_source))


main()
