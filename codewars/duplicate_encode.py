def duplicate_encode(word):
    word = word.upper()

    outp = ['(' for i in range(len(word))]
    letters = {}
    for n, i in enumerate(word):
        if i not in letters:
            letters[i] = n
        else:
            outp[n] = ')'
            outp[letters[i]] = ')'

    outp_str = ''
    for i in outp:
        outp_str += i

    return outp_str
