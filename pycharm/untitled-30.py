import requests


def get_file_url(file_url):
    for i in range(-1, -len(file_url), -1):
        if file_url[i] == '/':
            return file_url[:i + 1]
            break


def file_write(file_name, str):
    with open(file_name, 'w') as out:
        out.write(str)


def main():
    my_input = input()
    url_body = get_file_url(my_input)
    r = requests.get(my_input)
    print(r.text)
    while r.text[0] != 'W':
        r = requests.get(url_body + r.text)
        print(r.text)
    file_write('output.txt', r.text)


main()
