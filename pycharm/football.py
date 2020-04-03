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


def chart(d, l_str):
        team_1 = l_str[0]
        team_2 = l_str[2]
        scr_team_1 = l_str[1]
        scr_team_2 = l_str[3]
        update_dictionary(d, team_1, 1, 'cnt')  # cnt matches team 1
        update_dictionary(d, team_2, 1, 'cnt')  # cnt matches team 2
        if scr_team_1 > scr_team_2:
            update_dictionary(d, team_1, 1, 'win')
            update_dictionary(d, team_1, 0, 'lose')
            update_dictionary(d, team_1, 0, 'draw')
            update_dictionary(d, team_2, 0, 'win')
            update_dictionary(d, team_2, 1, 'lose')
            update_dictionary(d, team_2, 0, 'draw')
        elif scr_team_1 < scr_team_2:
            update_dictionary(d, team_1, 0, 'win')
            update_dictionary(d, team_1, 1, 'lose')
            update_dictionary(d, team_1, 0, 'draw')
            update_dictionary(d, team_2, 1, 'win')
            update_dictionary(d, team_2, 0, 'lose')
            update_dictionary(d, team_2, 0, 'draw')
        else:
            update_dictionary(d, team_1, 0, 'win')
            update_dictionary(d, team_1, 0, 'lose')
            update_dictionary(d, team_1, 1, 'draw')
            update_dictionary(d, team_2, 0, 'win')
            update_dictionary(d, team_2, 0, 'lose')
            update_dictionary(d, team_2, 1, 'draw')


def points(d):
    for key in d:
        d_key = d[key]
        team_points = d_key['win'] * 3 + d_key['draw']
        update_dictionary(d, key, team_points, 'points')


def read(file_name):
    d = {}
    with open(file_name) as inp:
        for line in inp:
            l_str = line.strip().split(';')
            chart(d, l_str)
        points(d)
    return d


def main():
    dict_output(read('input.txt'))


main()
