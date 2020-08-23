import game_h as game
import img


def read(file_name):
    d = []
    with open(file_name) as inp:
        for line in inp:
            l_str = line.strip().split(' ')
            d.append(l_str)
    return d


def tx(d):
    list = []
    for l_str in d:
        str = ''
        if l_str[0] == 'tx:':
            for i in range(len(l_str) - 1):
                str += l_str[i+1]
                str += ' '
            list.append(str)
    return list


def test():
    game.dream(img.school500, tx(read('text/test.gkt')))
