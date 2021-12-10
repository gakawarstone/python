def find_it(seq):
    n = 1
    n_negative = -1

    while 1:
        if seq.count(n) % 2 == 1:
            return n
        else:
            n += 1

        if seq.count(n_negative) % 2 == 1:
            return n_negative
        else:
            n_negative -= 1
