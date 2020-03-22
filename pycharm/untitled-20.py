def modify_list(l):
    len_l = len(l)
    for cnt in range(len_l):
        if l[cnt] % 2 == 0:
            l[cnt] = int(l[cnt] / 2)
            cnt += 1
        else:
            l[cnt] = 'z'
            cnt += 1
    while 'z' in l:
        l.remove('z')
