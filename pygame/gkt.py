import game_h as game
import img


# read from file and return list of lines
# lines - list of words
def read(file_name):
    d = []
    with open(file_name) as inp:
        for line in inp:
            l_str = line.strip().split(' ')
            d.append(l_str)
    return d


# search for 'tx:' and return list of all lines starts with it
def tx(d):
    list = []
    for l_str in d:
        str = ''
        if l_str[0] == 'tx:':
            # creat list without 'tx:'
            for i in range(len(l_str) - 1):
                str += l_str[i+1]
                str += ' '
            list.append(str)
    return list


def test():
    game.dream(img.school500, tx(read('text/test.gkt')))
